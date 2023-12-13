# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dump_word_dict.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/13 07:53:40 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 08:07:52 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import pickle


def main():
	if len(sys.argv) != 1:
		return 1

	try:
		file = open("words.txt", "r")
		content = file.read()
	except:
		return 1

	word_dict = {}
	i = 0
	word = ""
	while (i < len(content)):
		if content[i] != ' ' and content[i] != '\n':
			word += content[i]
		else:
			length = len(word)
			if length in word_dict:
				word_dict[length] += 1
			else:
				word_dict[length] = 1
			word = ""
		i += 1

	if word:
		length = len(word)
		if length in word_dict:
			word_dict[length] += 1
		else:
			word_dict[length] = 1

	with open("word_count.pickle", "wb") as pickle_file:
			pickle.dump(word_dict, pickle_file)

	file.close()


if __name__ == '__main__':
	main()
