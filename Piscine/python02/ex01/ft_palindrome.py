# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 08:32:02 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 08:39:16 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def is_palindrome(string) -> bool:
	if string[::-1] == string:
		return True
	else:
		return False


def main():
	if len(sys.argv) != 2:
		print("Error! Insert just 1 string!")
		return 1
	if (is_palindrome(sys.argv[1])):
		print(f"The string {sys.argv[1]} is palindrome")
	else:
		print(f"The string {sys.argv[1]} is not palindrome")


if __name__ == "__main__":
	main()