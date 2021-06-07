import itertools

def permutations(string, n):
	""" Not lexicographically sorted """
    return ["".join(item) for item in set(itertools.permutations(string, n))]

def combs(s, r):
    if not r:
        yield ''
    elif s:
        for comb in combs(s[1:], r-1):
            yield s[0] + comb  # use first char ...
        yield from combs(s[1:], r)  # ... or don't

def perms(s, r):
    if not r:
        yield ''
    else:
        for comb in combs(s, r):
            for i, char in enumerate(comb):
                rest = comb[:i] + comb[i+1:] 
                for perm in perms(rest, r-1):
                    yield char + perm

def main():
	print(list(perms('abcdef', 4)))
	# print(list(combs('abcdef', 4)))
	print(permutations('abcdef', 4))

if __name__ == '__main__':
	main()
