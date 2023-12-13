# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    student.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 23:27:02 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:46:27 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def __str__(self):
		return f"{self.fname} {self.lname}"


class Student(Person):
	def __init__(self, fname, lname, dcourse=None):
		Person.__init__(self, fname, lname)	
		self.dcourse = dcourse
	
	def __str__(self):
		if self.dcourse == "":
			return f"{self.fname} {self.lname}"
		elif self.dcourse is not None:
			return f"{self.fname} {self.lname} is registered to {self.dcourse}"
		else:
			return f"{self.fname} {self.lname} is not registered to any course"

def ft_strlen(string):
	i = 0
	for c in string:
		i += 1
	return i


def main():
	if ft_strlen(sys.argv) != 1:
		return 1
	
	try:
		fname = input("Insert first name: ")
		lname = input("Insert last name: ")
		answer = input("Are you a student? (y/n)")
		while (answer != "y" and answer != "n"):
			answer = input("Please type \"y\" or \"n\": ")
		if answer == "y":
			dcourse = input("Please insert your degree course: ")
			student = Student(fname, lname, dcourse)
		else:
			student = Student(fname, lname, "")
	except KeyboardInterrupt:
		return 1
	print(student)

if __name__ == "__main__":
	main()