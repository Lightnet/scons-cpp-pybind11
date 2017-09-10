import wrap

def test_add():
	assert(wrap.add(3, 4) == 7)
	print("test")
	print(wrap.add(3, 4))

if __name__ == '__main__':
    test_add()