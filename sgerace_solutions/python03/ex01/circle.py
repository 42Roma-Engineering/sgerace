# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    circle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 10:38:43 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 03:37:26 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Circle():
	def __init__(self, center, radius):
		try:
			x, y = center
			self.center = Point(x, y)
		except TypeError:
			self.center = center
		self.radius = radius
	def __str__(self):
		return(f"Circle of center ({self.center.x}, {self.center.y}) and radius {self.radius}")


def ft_strlen(string):
	i = 0
	for c in string:
		i += 1
	return i



def main():
	if ft_strlen(sys.argv) != 1:
		return 1

	p = Point(150, 100)
	c = Circle(p, 75)
	print(c)


if __name__ == '__main__':
	main()