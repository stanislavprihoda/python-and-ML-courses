def one_func():
	print("outcome of one_func from one.py")

print("top level in one.py")

if __name__ == '__main__':
	print("one.py run directlly")
else:
	print("one.py run after import")