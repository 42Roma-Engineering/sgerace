# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    circle.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 23:12:02 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 23:25:09 by sgerace          ###   ########.fr        #
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
	
	def contains(self, point) -> bool:
		distance = ((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2) ** 0.5
		if (distance <= self.radius):
			return True
		else:
			return False

def ft_strlen(string):
	i = 0
	for c in string:
		i += 1
	return i


def main():
	if ft_strlen(sys.argv) != 3:
		return 1

	try:
		x = float(sys.argv[1])
		y = float(sys.argv[2])
	except ValueError:
		return 1

	c = Circle((0, 0), 1)
	p = Point(x, y)
	if c.contains(p):
		print(f"The point ({x}, {y}) lies in the Circle of center (0, 0) and radius 1")
	else:
		print(f"The point ({x}, {y}) lies out of the Circle of center (0, 0) and radius 1")

if __name__ == "__main__":
	main()