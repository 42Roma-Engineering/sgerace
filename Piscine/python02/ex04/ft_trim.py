# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_trim.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 09:30:46 by sgerace           #+#    #+#              #
#    Updated: 2023/12/22 16:45:46 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def trim(list1) -> None:
	if len(list1) > 0:
		del list1[0]
	if len(list1) > 1:
		del list1[-1]
	return None


def main():
	if len(sys.argv) < 3:
		print("Error! You must insert at least 2 values")
		return 1

	list1 = []
	i = 1
	while (i < len(sys.argv)):
		list1 += [sys.argv[i]]
		i += 1

	trim(list1)
	print(list1)

if __name__ == "__main__":
	main()