# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_min.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 05:04:13 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 05:19:56 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def my_min(x=0, y=0, z=0) -> int:
	if x <= y and x <= z:
		return(x)
	elif y <= x and y <= z:
		return(y)
	else:
		return(z)


def main():
	if len(sys.argv) != 4:
		print("Error! Usage: python3 ft_max.py <x> <y> <z>")
		return 1
	try:
		num1 = float(sys.argv[1])
		num2 = float(sys.argv[2])
		num3 = float(sys.argv[3])
	except ValueError:
		return 1
	res = my_min(num1, num2, num3)
	print("The min is:", res)

if __name__ == "__main__":
	main()