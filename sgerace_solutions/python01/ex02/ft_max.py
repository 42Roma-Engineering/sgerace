# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_max.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 04:57:56 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:03:48 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	if len(sys.argv) != 4:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
		return 1
	m = 0
	try:
		num1 = float(sys.argv[1])
		num2 = float(sys.argv[2])
		num3 = float(sys.argv[3])
		if num1 >= num2 and num1 >= num3:
			m = (num1)
		elif num2 >= num1 and num2 >= num3:
			m = (num2)
		else:
			m = (num3)
	except ValueError:
		return 1

	print("The max is: " + str(m))

if __name__ == '__main__':
	main()