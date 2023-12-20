# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_print.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 01:38:09 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 02:09:54 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_strlen(string) -> int:
	i = 0
	while string[i:]:
		i += 1
	return i


def main():
	string = input("Insert a string: ")
	integer = input("Insert an integer: ")

	if integer == "":
		return (1)
	try:
		integer = int(integer)
	except ValueError:
		return (1)

	if integer < 0:
		integer = integer*(-1)

	if integer > ft_strlen(string):
		print("Error: index out of range")
		return (1)

	if integer == 1:
		first = string[integer:]
	else:
		first = string[integer:-integer+1]

	print(first)

if __name__ == '__main__':
	main()