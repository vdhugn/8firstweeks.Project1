from queue import Queue

def push(value, queue):
    queue.put(value)
def pop(queue):
    if queue.empty():
        print("NULL")
        return
    value = queue.get()
    print(value)

if __name__ == '__main__':
    queue = Queue()

    while True:
        str = input()

        if str.startswith("PUSH"):
            value = int(str.split(" ")[1])
            push(value, queue)
        elif str.startswith("POP"):
            pop(queue)
        else:
            break