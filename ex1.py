#!/usr/bin/env python3.7

message = input("Enter the message: ")
count = input("Enter the #of repetition: ")

if count:
	count = int(count)
else:
	count = 1

def multi_echo(message, count):
	while count > 0:
		print(message)
	#	print("...................................")
	#	print(",,,,,,,,,,,,,,,,")
		count -= 1

multi_echo(message, count)