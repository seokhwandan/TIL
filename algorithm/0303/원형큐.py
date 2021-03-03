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
        rear = (rear + 1) % SIZE
        Q[rear] = item
def deQueue():
    global front, rear
    # if isEmpty():
    #     print('Queue Empty')
    # else:
    #     front += 1
    #     return Q[front]
    if front != rear:
        front = (front + 1) % SIZE
        return Q[front]

def Qpeek():
    global front, rear
    if isEmpty():
        print('Queue Empty')
    else:
        return Q[front + 1 % SIZE]

enQueue(1)
print(deQueue())
enQueue(2)
print(deQueue())
enQueue(3)
print(deQueue())
enQueue(4)
enQueue(5)
enQueue(6)
print(Qpeek())
print(deQueue())