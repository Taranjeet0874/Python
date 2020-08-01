# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:48:38 2019

@author: Dell
"""

#convert decimal number to binary , octal ,hexadecimal using switcher case in object oriented python
class num:
	def __init__(self,numberr):
		self.numberr=numberr


while True:

	n = int(input("Enter the decimal number: "))
	a = num(n)
	number = a.numberr



	choice = int(input("Enter the choice: ")) 

	def decimal_to_binary(number):
		return bin(number)

	def decimal_to_octal(number):
		return oct(number)

	def decimal_to_hexa(number):
		return hex(number)

	binary = decimal_to_binary(number)
	octal = decimal_to_octal(number)
	hexa = decimal_to_hexa(number)

	def switcher(binary,octal,hexa,choice):
		switcher = {
		1: binary,
		2: octal,
		3: hexa
		}
		return switcher.get(choice)
	print(switcher(binary,octal,hexa,choice))


