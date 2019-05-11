import multiprocessing as mp

def consumer(input_q):
    while True:
        # get an item from the queue
        item = input_q.get()
        # process the item
        print(mp.current_process().name, ":: ",item)
        # signal completion
        input_q.task_done()


def producer(sequence, output_q):
	for item in sequence:
		# put item on the queue
		output_q.put(item)

if __name__ == '__main__':
    # create the queue
    qq = mp.JoinableQueue()
    # launch the consumer process
    consumer_p = mp.Process(target=consumer, args=(qq,))
    consumer_p.daemon = True 
    consumer_p.start()
    #run the producer function on some data
    sequence = range(50)
    producer(sequence, qq)
    # wait for consumer to finish
    qq.join()
    # finally terminate the daemon process
    consumer_p.terminate()
