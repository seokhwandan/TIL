SIZE = 100
Q = [0] * SIZE
front, rear = -1, -1
def isFull():
    global rear
    return rear == len(Q) - 1
def isEmpty():
    global front
    return front == rear
def enQueue(item):
    global rear
    if isFull():
        print('Queue Full')
    else:
        rear += 1
        Q[rear] = item
def deQueue():
    global front, rear
    # if isEmpty():
    #     print('Queue Empty')
    # else:
    #     front += 1
    #     return Q[front]
    if front != rear:
        front += 1
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print('Queue Empty')
    else:
        return Q[front + 1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print()