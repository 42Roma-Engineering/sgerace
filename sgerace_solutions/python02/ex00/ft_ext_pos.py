# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ext_pos.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 07:18:27 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 08:30:57 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def calc_min(nums):
	index = 0
	i = 0
	min = nums[0]
	for num in nums:
		if num < min:
			min = num
			index = i
		i += 1
	print("The min is:", min, "and is position is:", index)
	return


def calc_max(nums):
	index = 0
	i = 0
	max = nums[0]
	for num in nums:
		if num > max:
			max = num
			index = i
		i += 1
	print("The max is:", max, "and is position is:", index)
	return


def main():
	i = 1
	nums = []
	lenght = len(sys.argv)
	if lenght < 2:
		print("Error! Usage: python3 ft_ext_pos.py <x1> ... <xn>")
		return 1
	while (i < lenght):
		try:
			num = int(sys.argv[i])
		except ValueError:
			return 1
		nums += [num]
		i += 1
	calc_min(nums)
	calc_max(nums)
		

if __name__ == '__main__':
    main()