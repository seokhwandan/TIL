## 큐의 구현

### 선형큐

- #### 1차원 배열을 이용한 큐

  - 큐의 크기 = 배열의 크기
  - front : 마지막에 꺼내진 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스



- #### 상태표현

  - 초기상태 : front = rear = -1
  - 공백상태 : front = rear
  - 포화상태 : rear = n - 1 ( n : 배열의 크기, n - 1: 배열의 마지막 인덱스)



- #### 삽입 : enQueue(item)

  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

    1) rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련

    2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장

    ```python
    def enQueue(item):
        global rear
        if isFull() : print('Queue_Full')
        else:
            rear <- rear + 1;
            Q[rear] <- item
    ```



- #### 삭제 : deQueue()

  - 가장 앞에 있는 원소를 삭제하기 위해

    1) front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소 이동

    2) 새로운 첫 번째 원소를 리턴 함으로써 삭제와 동일한 기능함

    ```python
    def deQueue():
        global front
        if isEmpty() : print('Queue_Empty')
        else:
            fornt <- front + 1
            return Q[front]
    ```



- #### 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  - 공백상태 : front = rear

  - 포화상태 : rear = n - 1 ( n : 배열의 크기, n - 1: 배열의 마지막 인덱스)

    ```python
    def isEmpty():
        return front == rear
    def isFull():
        return rear == len(Q) - 1
    ```



- #### 검색 : Qpeek()

  - 가장 앞에 있는 원소를 검색하여 반환하는 연산

  - 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

    ```python
    def Qpeek():
        if isEmpty(): print('Queue_Empty')
        else:
            return Q[front + 1]
    ```

    

### 원형 큐

- front 변수
  - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front 가 있는 자리는 사용하지 않고 항상 빈자리로 둠
- 삽입 위치 및 삭제 위치
  - 선형큐
    - 삽입 위치 : rear = rear + 1
    - 삭제 위치 : front = front + 1
  - 원형큐
    - 삽입 위치 : rear = (rear + 1) % n
    - 삭제 위치 : front = (front + 1) % n 
- 초기 공백 큐 생성
  - 크기 n 인 1차원 배열 생성
  - front 와 rear 를 0으로 초기화

- 공백상태 및 포화상태 검사 : isEmpty(), isFull()

  - 공백 상태 : front = rear

  - 포화 상태 : 삽입할 rear 의 다음 위치 = 현재 front

    - (rear + 1) % n = front

    ```python
    def isEmpty():
        return front == rear
    
    def isFull():
        return (rear + 1) % len(cQ) == front
    ```

- 삽입 : enQueue(item)

  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

    1) rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함 : rear <- (rear + 1) % n

    2) 그 인덱스에 해당하는 배열원소 cQ[rear] 에 item 을 저장

    ```python
    def enQueue(item):
        global rear
        if isFull() : print('Queue_Full')
        else:
            rear = (rear + 1) % len(cQ);
            cQ[rear] = item
    ```

- 삭제 : deQueue(), delete()

  - 가장 앞에 있는 원소를 삭제하기 위해

    1) front 값을 조정하여 삭제할 자리를 준비함

    2) 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능함

    ```python
    def deQueue():
        global front
        if isEmpty() : print('Queue_Empty')
        else:
            fornt = (front + 1) % len(cQ)
            return cQ[front]
    ```

    

### 연결 큐

- #### 단순 연결 리스트(Linked List)를 이용한 큐

  - 큐의 원소 : 단순 연결 리스트의 노드
  - 큐의 원소 순서 : 노드의 연결 순서. 링크로 연결되어 있음
  - front : 첫 번째 노드를 가리키는 링크
  - rear : 마지막 노드를 가리키는 링크

- #### 상태 표현

  - 초기 상태 : front = rear = None
  - 공백 상태 : front = rear = None