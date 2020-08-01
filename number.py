# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:48:38 2019

@author: Dell
"""

#convert decimal number to binary , octal ,hexadecimal using switcher case in object oriented python
class num():
    
	def decimal_to_binary(self,n):
		return bin(n)

	def decimal_to_octal(self,n):
		return oct(n)

	def decimal_to_hexa(self,n):
		return hex(n)
	


n = int(input("Enter the decimal number: "))
a = num()
	
while True:

	
	


	choice = int(input("Enter the choice: ")) 


	binary = a.decimal_to_binary(n)
	octal = a.decimal_to_octal(n)
	hexa = a.decimal_to_hexa(n)

	def switcher(binary,octal,hexa,choice):
		switcher = {
		1: binary,
		2: octal,
		3: hexa
		}
		return switcher.get(choice)
	print(switcher(binary,octal,hexa,choice))


