Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> qs = ["What is your name?","What is your fav. color?","What is your quest?"]
>>> n = 0
>>> while True:
	print("Type q to quit")
	a = input(qs[n])
	if a == "q":
		break
	n = (n+1) % 3
	
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
=============================== RESTART: Shell ===============================
>>> 
