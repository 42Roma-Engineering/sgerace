# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_matrix.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 08:40:01 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:19:15 by sgerace          ###   ########.fr        #
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
		print("Error! Usage: python3 ft_matrix.py <n> <m>")
		return 1
	i = 0
	c_sum = 0
	matrix = []
	list1 = []
	list_r = []
	try: 
		n = int(sys.argv[1])
		m = int(sys.argv[2])
	except ValueError:
		return 1
	while (i < n):
		j = 0
		while (j < m):
			try:
				num = float(input(f"Insert the element in position ({i}, {j}): "))
			except ValueError:
				return 1
			list1 += [num]
			j += 1
		matrix += [list1]
		list1 = []
		i += 1
	print("The inserted matrix is:")
	for ma in matrix:
		print(ma)
		r_sum = 0
		for num in ma:
			r_sum += num
		list_r += [r_sum]
	print("The sum over rows is:")
	print(list_r)

	list_c = []
	m = len(matrix[0])
	n = len(matrix)
	for j in range(m):
		c_sum = 0
		for i in range(n):
			c_sum += matrix[i][j]
		list_c += [c_sum]
	print("The sum over columns is:")
	print(list_c)


if __name__ == "__main__":
	main()