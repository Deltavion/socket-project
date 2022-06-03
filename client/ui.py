from tkinter import *

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("nsiCHAT2000")
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)

        # variables
        self.mode = True #true --> public
        self.creating_contact = False

        self.active_contact = None
        self.contacts_list = []

        # constantes
        self.PR = "74e5ff"
        self.BG = "#303a52"
        self.NETWORK = "192.168.1."

    def create_app(self):
        #---------------------------------------------------------------main widgets
        # Message to send input
        self.msg_input = Entry(self.root)
        self.msg_input.place(x=10,y=560,width=720,height=30)

        # Send button
        self.send_btn = Button(self.root, text="Send")
        self.send_btn.bind('<Button-1>', self.write_chat)
        self.send_btn.place(x=740,y=560,width=50,height=30)

        self.root.bind('<Return>', self.enter_key)

        # Public mode button
        self.public_btn = Button(self.root,text="Public", command=self.switch_mode, state="disable", relief="flat")
        self.public_btn.place(x=10,y=10,width=385,height=30)

        # Private mode button
        self.private_btn = Button(self.root, text="Private", command=self.switch_mode)
        self.private_btn.place(x=405,y=10,width=385,height=30)

        #---------------------------------------------------------------public chat
        self.public_frame = Frame(self.root)
        self.public_frame.place(x=10,y=50,width=790,height=500)

        scrollbar = Scrollbar(self.public_frame)
        scrollbar.place(x=770,y=0,width=20,height=500)

        self.public_chat = Listbox(self.public_frame, yscrollcommand = scrollbar.set,  borderwidth="1px", relief="groove", justify="left")
        self.public_chat.place(x=0,y=0,width=770,height=500)

        scrollbar.config(command = self.public_chat.yview)

        #---------------------------------------------------------------private chat
        self.private_frame = Frame(self.root)
        #chat.place(x=70,y=0,width=700,height=500)

        create_btn = Button(self.private_frame, text=f"+", command=self.open_contact_creater)
        create_btn.place(x=0,y=480,width=70,height=20)

        self.contact_chat_list = []
        self.contact_btn_list = []

        #---------------------------------------------------------------create contact
        self.contact_frame = Frame(self.private_frame, borderwidth="3px", relief="groove")

        title = Label(self.contact_frame, text="Enter IP adress :")
        title.place(x=0,y=0,width=240,height=20)

        self.contact_entry = Entry(self.contact_frame)
        self.contact_entry.place(x=0,y=20,width=200,height=20)

        add_btn = Button(self.contact_frame, text="Add", command=self.create_contact)
        add_btn.place(x=200,y=20,width=40,height=20)

        cls_btn = Button(self.contact_frame, text="x", command=self.close_contact_creater)
        cls_btn.place(x=225,y=0,width=15,height=15)

    def switch_mode(self):
        if self.creating_contact:
            self.error(3)
            return

        self.mode = not self.mode
        if self.mode:
            self.public_btn.config(state="disable", relief="flat")
            self.private_btn.config(state="normal", relief="raised")

            self.public_frame.place(x=10,y=50,width=790,height=500)
            self.private_frame.place_forget()

        else:
            self.public_btn.config(state="normal", relief="raised")
            self.private_btn.config(state="disable", relief="flat")

            self.public_frame.place_forget()
            self.private_frame.place(x=10,y=50,width=790,height=500)

            if self.active_contact == None:
                self.send_btn.config(state="disabled")

    def open_contact_creater(self):
        self.creating_contact = True

        self.send_btn.config(state="disabled")
        self.public_btn.config(state="disabled")

        for i in range(len(self.contact_chat_list)):
            self.contact_chat_list[i].place_forget()
        self.contact_frame.place(x=270,y=220,width=250,height=50)
        self.contact_entry.focus()
        self.contact_entry.delete(0, "end")
        self.contact_entry.insert('end', self.NETWORK)

    def close_contact_creater(self):
        self.creating_contact = False
        self.contact_frame.place_forget()
        self.public_btn.config(state="normal")
        self.msg_input.focus()
        if self.active_contact != None:
            self.contact_chat_list[self.active_contact].place(x=70,y=0,width=700,height=500)
            self.send_btn.config(state="normal")

    def create_contact(self):
        self.creating_contact = False
        ip = self.contact_entry.get()
        if ip != "":
            name = get_DNS(ip)
            if not name:
                self.error(1)
                self.close_contact_creater()
                return

            self.contact_entry.delete(0, "end")
            self.contact_frame.place_forget()

            contact_index = len(self.contact_btn_list)  # à chanegr par contact_dict après
            self.active_contact = contact_index
            self.contacts_list.append([ip, name])

            self.contact_chat_list.append(Listbox(self.private_frame, borderwidth="1px", relief="sunken", justify="left"))
            self.contact_chat_list[contact_index].insert('end', f"Chat avec {name}")
            self.contact_chat_list[contact_index].insert('end', 139*"-")
            self.contact_chat_list[contact_index].place(x=70,y=0,width=700,height=500)

            self.contact_btn_list.append(Button(self.private_frame, text=name))
            self.contact_btn_list[contact_index].config(command=lambda x=contact_index: self.swap_contact(x))
            self.contact_btn_list[contact_index].place(x=0,y=contact_index*20,width=70,height=20)

            self.send_btn.config(state="normal")

    def swap_contact(self, x):
        for i in range(len(self.contact_chat_list)):
            self.contact_chat_list[i].place_forget()
        self.contact_chat_list[x].place(x=70,y=0,width=700,height=500)
        self.active_contact = x

    def write_chat(self):
        msg = self.msg_input.get()

        if msg == "":
            return
        else:
            if self.mode:
                self.msg_input.delete(0, "end")
                self.public_chat.insert('end', msg)
                send(msg, "public")

            else:
                if self.creating_contact:
                    self.error(3)
                    return
                if self.active_contact == None:
                    self.error(2)
                    return

                self.msg_input.delete(0, "end")
                self.contact_chat_list[self.active_contact].insert('end', msg)
                send(msg, self.contacts_list[self.active_contact][0])

    def enter_key(self, event):
        if self.creating_contact:
            self.create_contact()
        else:
            self.write_chat()

    def error(self, x):
        if x == 1:
            print("contact not found")

        elif x == 2:
            print("there's any contact to chat with")

        elif x == 3:
            print("finish creating contact or cancel it")


dns = {"192.168.1.10": "matteo",
           "192.168.1.20": "romain",
           "192.168.1.30": "valentin",
           "192.168.1.40": "alexandre"}

def get_DNS(ip):
    if ip in dns:
        return dns[ip]

def send(msg, exp):
    print(f"[{exp}] {msg}")

if __name__ == "__main__":
    app = App()
    app.create_app()
    app.root.mainloop()
