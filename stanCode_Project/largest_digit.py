"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n < 0:
		n *= -1
	last_num = n % 10
	return find_largest_digit_helper(n, last_num)


def find_largest_digit_helper(n, ans):
	new_n = n // 10
	num = n % 10
	if num > ans:
		ans = num
	if new_n < 1:
		return ans
	else:
		return find_largest_digit_helper(new_n, ans)



if __name__ == '__main__':
	main()
