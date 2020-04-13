import backend
import time

if __name__ == '__main__':
	start_time = time.time()
	backend.getDadJokes()
	print(time.time()-start_time)