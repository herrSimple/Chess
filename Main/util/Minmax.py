from timeit import timeit

class Test:
	__foo = [1, 2, 3, 4, 5, 6]

	
	def foo(self, a, b=lambda a: "positive" if vars()["a"] == 0 else "negative"):
		print(a, "is", b)

bar = Test()
bar.foo(10)

a = 4

def on_board(pos):
        return 7 >= pos[0] >= 0 and 7 >= pos[1] >= 0

LEFT = (0, -1)
RIGHT = (0, 1)

print(LEFT == (0, -1))

alist = [[a, a] for a in range(8) for b in range(8)]
moves = []

for a, b in alist:
	pos = [a-1, b-1]
	moves.append(pos)
	pos = [0, 0]

print(moves)

KEY = ("WHITE_KING", (1, 1))
VALUE = [[0, 0], [2, 1]]
