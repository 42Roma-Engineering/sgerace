# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_summorial.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 05:21:44 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 05:32:34 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def ft_strlen(string) -> int:
	i = 0
	while string[i:]:
		i += 1
	return i


def ft_is_digit(char) -> bool:
	if char >= '0' and char <= '9':
		return True
	return False


def ft_define_num(char) -> int:
	dictionary = '0123456789'
	i = 0
	while i < 10:
		if char == dictionary[i]:
			return i
		i += 1


def ft_atoi(string) -> int:
	plus = False
	minus = False
	is_num = False
	length = ft_strlen(string)
	sign = 1
	result = 0
	i = 0

	try:
		while (string[i:]):
			if string[i] == ' ' or string[i] == '\t' or string[i] == '\n' or string[i] == '\v' or string[i] == '\f' or string[i] == '\r':
				i += 1
			elif string[i] == '-':
				if minus == True or is_num == True:
					raise ValueError
				minus = True
				sign = -1
				i += 1
				if (i < length and ft_is_digit(string[i]) == False):
					raise ValueError
			elif string[i] == '+':
				if plus == True or is_num == True:
					raise ValueError
				plus = True
				i += 1
				if (i < length and ft_is_digit(string[i]) == False):
					raise ValueError
			elif (ft_is_digit(string[i]) and is_num == False):
				while (ft_is_digit(string[i:])):
					result = result * 10 + ft_define_num(string[i]) - ft_define_num('0')
					i += 1
				is_num = True
			else:
				raise ValueError
	except ValueError:
		raise ValueError
	return result * sign


def main():
	res = 0
	if len(sys.argv) != 2:
		print("Error! Usage: python3 ft_summorial.py <n>")
		return 1
	try:
		num = ft_atoi(sys.argv[1])
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