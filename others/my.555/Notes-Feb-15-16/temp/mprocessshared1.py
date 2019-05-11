import multiprocessing as mp

result = []

def do_square(sequence):
	global result
	for n in sequence:
		result.append(n*n)
	print(mp.current_process().name,"::in:: ",result)

if __name__ == '__main__':
    numbers = [3,5,7]
    pp = mp.Process(target=do_square, args=(numbers,))
    pp.start()
    pp.join()
    print(mp.current_process().name,"::out:: ",result)
