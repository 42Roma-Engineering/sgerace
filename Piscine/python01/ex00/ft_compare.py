# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_compare.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 04:27:13 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 05:22:13 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def ft_strlen(string) -> int:
	i = 0
	while string[i:]:
		i += 1
	return i


def main():
	if ft_strlen(sys.argv) != 3:
		return 1
	
	try:
		num1 = float(sys.argv[1])
		num2 = float(sys.argv[2])
	except ValueError:
		return 1

	if num1 > num2:
		print(f"{num1} is greater than {num2}")
	elif num1 < num2:
		print(f"{num1} is less than {num2}")
	else:
		print(f"{num1} is equal to {num2}")
  
if __name__ == '__main__':
	main()