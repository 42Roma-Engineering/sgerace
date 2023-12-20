# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_print.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 00:09:07 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 01:36:39 by sgerace          ###   ########.fr        #
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

	if integer > ft_strlen(string):
		print("Error: index out of range")
		return (1)

	print(string[integer], string[-integer])

if __name__ == '__main__':
	main()