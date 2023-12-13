# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum_list.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 05:33:21 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 07:20:11 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def sum_list(nums) -> int:
	res = 0
	for num in nums:
		res += num
	return res


def main():
	nums = []
	if len(sys.argv) != 1:
		return 1
	loop = True
	while (loop):
		try:
			num = int(input("Insert integer: "))
		except ValueError:
			return 1
		except KeyboardInterrupt:
			return 1
		if (num == 0):
			loop = False
		else:
			nums += [num]

	print("The sum is:", sum_list(nums))


if __name__ == '__main__':
	main()