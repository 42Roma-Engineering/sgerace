# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_space_print.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 02:11:10 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 02:17:29 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def main():
	string = input("Insert a string: ")
	lenght = len(string)

	if lenght < 20:
		string = (" "*(20-lenght) + string)
	else:
		string = (string[-(20 - lenght):])

	print(string)

if __name__ == '__main__':
	main()