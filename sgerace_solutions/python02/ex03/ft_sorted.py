# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sorted.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 09:14:33 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:21:58 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def	main():
	if len(sys.argv) < 3:
		print("Error! You must insert at least 2 numbers")
		return 1

	list1 = []
	length = len(sys.argv)
	tmp = 0
	i = 1
	while (i < length):
		try:
			list1 += [int(sys.argv[i])]
		except ValueError:
			return 1
		i += 1

	if (list1 == sorted(list1, reverse=True)):
		print("The inserted sequence is sorted!")
		return 0

	i = 0
	while (list1[i:]):
		if (i + 1 < length and list1[i] < list1[i + 1]):
			print("The inserted sequence is not sorted!")
			print("The correct order is:", sorted(list1, reverse=True))
			return 1
		i += 1
   
			

if __name__ == "__main__":
	main()