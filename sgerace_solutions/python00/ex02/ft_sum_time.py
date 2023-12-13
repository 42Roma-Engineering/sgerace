# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_sum_time.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/11 23:54:20 by sgerace           #+#    #+#              #
#    Updated: 2023/12/13 01:33:52 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def main():

	try:
		hours = input("Insert hours: ")
		minutes = input("Insert minutes: ")
		seconds = input("Insert seconds: ")
		try:
			if hours == "" or minutes == "" or seconds == "":
				raise ValueError
			hours = float(hours) * 3600
			if hours < 0:
				raise ValueError
			minutes = float(minutes) * 60
			if minutes < 0:
				raise ValueError
			seconds = float(seconds)
			if seconds < 0:
				raise ValueError
			result = int(hours + minutes + seconds)
		except ValueError:
			return 1
		except MemoryError:
			return 1
	except KeyboardInterrupt:
		return 1

	print("Total seconds: ", result, sep="")

if __name__ == '__main__':
	main()
