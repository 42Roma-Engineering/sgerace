# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    point.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 10:15:26 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:35:26 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y


def ft_strlen(string):
	i = 0
	for c in string:
		i += 1
	return i


def main():
	if ft_strlen(sys.argv) != 1:
		return 1
	
	p1 = input("Insert the coordinates of the first point: ")
	p2 = input("Insert the coordinates of the second point: ")

	i = 0
	x = ""
	y = ""
	while (p1[i:]):
		if (',' in p1):
			while (p1[i] != ','):
				x += p1[i]
				i += 1
			i += 1
			while (p1[i:]):
				y += p1[i]
				i += 1
		i += 1

	try:
		point1 = Point(float(x), float(y))
	except ValueError:
		return 1

	i = 0
	x = ""
	y = ""
	while (p2[i:]):
		while (p2[i] != ','):
			x += p2[i]
			i += 1
		i += 1
		while (p2[i:]):
			y += p2[i]
			i += 1
		i += 1

	try:
		point2 = Point(float(x), float(y))
	except ValueError:
		return 1

	expression = f"(({point1.x} - {point2.x}) ** 2 + ({point1.y} - {point2.y}) ** 2) ** 0.5"
	print("Their distance is:", eval(expression))

if __name__ == '__main__':
	main()