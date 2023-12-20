# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    write_words.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 07:27:59 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 07:45:28 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def main():
	if len(sys.argv) != 1:
		return 1
	try:
		leng = int(input("Insert an integer: "))
	except ValueError:
		return 1
	list1 = []
	file = open("words.txt", "r")
	content = file.read()
	i = 0
	string = ""
	while (content[i:]):
		if (content[i] == '\n'):
			if (len(string) > leng):
				list1 += [string + '\n']
			string = ""
		else:
			string += content[i]
		i += 1
	if len(string) > leng:
		list1 += [string]
	file.close()

	for i in list1:
		file = open("long_words.txt", "a")
		file.write(i)
		file.close()
	print(f"The words longer than {leng} have been written on \"long_words.txt\":")



if __name__ == '__main__':
	main()