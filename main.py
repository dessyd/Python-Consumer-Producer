# SuperFastPython.com
# example of one producer and one consumer with threads
from pylorem import LoremIpsum
from queue import Queue
from random import random
from threading import Thread
from time import sleep


def producer(queue):
    print("Producer: Running")
    for i in range(10):
        value = random()
        sleep(value)
        item = (i, value, LoremIpsum.sentence())
        queue.put(item)
        print(f"> {item[2]}")
    queue.put(None)
    print("Producer: Done")


def consumer(queue):
    print("Consumer: Running")
    while True:
        item = queue.get()
        if item is None:
            break
        sleep(item[1])
        print(f"< {item[2]}")
    print("Consumer: Done")


def main():
    queue = Queue()
    consumer_thread = Thread(target=consumer, args=(queue,))
    consumer_thread.start()
    producer_thread = Thread(target=producer, args=(queue,))
    producer_thread.start()
    producer_thread.join()
    consumer_thread.join()


if __name__ == "__main__":
    main()
