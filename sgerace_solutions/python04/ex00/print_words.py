# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_words.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 07:14:05 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 07:40:32 by sgerace          ###   ########.fr        #
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
	file = open("words.txt", "r")
	content = file.read()
	print(f"The words longer than {leng} are the following:")
	i = 0
	string = ""
	while (content[i:]):
		if (content[i] == '\n'):
			if (len(string) > leng):
				print(string)
			string = ""
		else:
			string += content[i]
		i += 1
	if len(string) > leng:
		print(string)
	file.close()



if __name__ == '__main__':
	main()