# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_summorial.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 05:21:44 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:10:16 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def main():
	res = 0
	if len(sys.argv) != 2:
		print("Error! Usage: python3 ft_summorial.py <n>")
		return 1
	try:
		num = int(sys.argv[1])
	except ValueError:
		return 1

	if num < 0:
		print("Error! n must be >= 0")
		return 1
	while (num > 0):
		res += num
		num -= 1
  
	print("The sum is:", res)

if __name__ == '__main__':
	main()