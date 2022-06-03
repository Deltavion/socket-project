import threading
import time

def t():
	time.sleep(3)
	print("coucou")

thread = threading.Thread(target=t)
thread.start()

s = input()
print(s)

