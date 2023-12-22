# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_abs.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sgerace <sgerace@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/12/12 04:57:46 by sgerace           #+#    #+#              #
#    Updated: 2023/12/20 18:43:47 by sgerace          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def main():
	try:
		expr = input("Insert an expression: ")
		if expr == "":
			raise ValueError
		res = eval(expr)
		if res < 0:
			res = -res
		print("The result is:", float(res))
	except ValueError:
		return (1)
	except KeyboardInterrupt:
		return (1)
	except ZeroDivisionError:
		return (1)
if __name__ == '__main__':
	main()