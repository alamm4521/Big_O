"""
Time complexity: O(N + M)
Description: The first loop is O(N) and the second loop is O(M).
 Since N and M are independent variables
	(which means the not affect each other),
Therefore Time complexity of the given problem will be O(N+M).
"""

import random
L = 1
I = 1


def rand(num):

    num = random.randint(0, 10)

    return num


def func(n, m):

    a = 0
    b = 0

    for i in range(n):
        a = a + int(random.randint(1, 10))

    for i in range(m):
        b = b + int(random.randint(1, 10))

    return m, n


def func_1(n):
	for i in range(n):
		for j in range(n):
			if j < I:
				break


"""def func_2(L):
    v = 0


for v in L:
	# helper func time complexity is O(n)
    helper_func(v)
"""


def func_3(n):
    j = n

    while j > 0:
        j = j // 2

    while j < n:
        j = j + 3
        n = n - 5

    return j


"""def func_10(n):
	total = 0
	while n > 5:
		n = n // 2
		# Remember the time complexity of the sum and range methods
		total += sum(range(n))

        return total"""


def func_4(n):
	for i in range(2, n):
		if n % i == 0:
			return True
		if i > n/i:
			return False


def func_5(n):
	for i in range(n):
		for j in range(i):
			if j * j > i:
				break


"""def func_6(n):

	k = 0

	for i in range(n//2, n):
		j = 1


    while j <= n:
		k += 1
		j *= 2

        return k
"""


def func_7(n):
	if n == 2:
		return 0
	else:
		return helper_func(n - 1) + helper_func(n - 2)


def helper_func_8(n):
	for i in range(n**2):
	        print(i)


def func_9_1(n):
	    for i in range(n**2):
		    print(helper_func(100))

    return 0


def main():

    nm = func(1, 2)

    n = nm[0]
    m = nm[1]

    r = func_1(n)
    print(r)
    r = func_2(n)
    print(r)
    r = func_3(n)
    print(r)
    r = func_4(n)
    print(r)
    r = func_5(n)
    print(r)
    r = func_6(n)
    print(r)
    r = func_7(n)
    print(r)
    r = func_8(n)
    print(r)
    r = func_9(n)
    print(r)

    return r


if __name__ == "__main__":
    main()
