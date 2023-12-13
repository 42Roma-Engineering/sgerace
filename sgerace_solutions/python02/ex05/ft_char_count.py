# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_char_count.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 09:37:59 by sgerace           #+#    #+#              #
#    Updated: 2023/12/12 10:13:18 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys


def main():
	if len(sys.argv) < 2:
		print("Error! No string given")
		return 1
	
	uppercase_to_lowercase = {
        'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm',
        'N': 'n', 'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
    }

	string = sys.argv[1]
	char_count = dict()

	for char in string:
		if char in uppercase_to_lowercase:
			char = uppercase_to_lowercase[char]
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	i = 0
	keys = list(char_count.keys())
	while (i < len(keys) - 1):
		j = 0
		while (j < len(keys) - i - 1):
			if keys[j] > keys[j + 1]:
				keys[j], keys[j + 1] = keys[j + 1], keys[j]
			j += 1
		i += 1

	print("Char count:")
	for key in keys:
		print(f"{key}: {char_count[key]}")

if __name__ == '__main__':
	main()