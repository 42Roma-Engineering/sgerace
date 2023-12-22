# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 08:32:02 by sgerace           #+#    #+#              #
#    Updated: 2023/12/20 20:52:35 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def is_palindrome(string) -> bool:
	l = len(string)

	i = 0
	word = ""
	while i < l:
		if ((string[i] != ' ') and (string[l - 1] != '\t')):
			word += string[i]
		i += 1
	

	i = 0
	rword = ""
	while l > 0:
		if ((string[l - 1] != ' ') and (string[l - 1] != '\t')):
			rword += string[l - 1]
		l -= 1

	if (rword == word[::1]):
		return True
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