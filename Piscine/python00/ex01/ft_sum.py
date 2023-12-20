# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/11 22:46:35 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 01:28:33 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def main():
	try:
		first_int = input("Insert your first integer: ")
		second_int = input("Insert your second integer: ")
		try:
			if first_int == "" or second_int == "":
				raise ValueError
			first_int = int(first_int)
			second_int = int(second_int)
			result = first_int + second_int
		except ValueError:
			return 1
		except MemoryError:
			return 1
	except KeyboardInterrupt:
		return 1

	print("Result: ", result, sep="")

if __name__ == '__main__':
	main()