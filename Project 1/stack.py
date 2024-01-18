def push(value, stack):
    stack.append(value)

def pop(stack):
    if len(stack) == 0:
        print("NULL")
        return
    value = stack.pop()
    print(value)

if __name__ == '__main__':
    stack = []

    while True:
        str = input()

        if str.startswith("PUSH"):
            value = int(str.split(" ")[1])
            push(value, stack)
        elif str.startswith("POP"):
            pop(stack)
        else:
            break