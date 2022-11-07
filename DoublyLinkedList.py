class Node:
    def __init__(self, data):
        self.data = data # 처음에 노드를 생성하면 self의 data에 넣는다.
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0

    def __len__(self):  # print(len(l))으로 길이를 출력할 수 있다.
        return self.데이터수

    def __str__(self):  # 노드 값들을 리스트처럼 보이게 한다.
        현재노드 = self.head # 현재노드에 init값이 들어감
        현재노드 = 현재노드.next # init값은 필요없기 때문에 현재노드.next 값부터 시작
        s = ''

        for i in range(self.데이터수):
            s += f'{현재노드.data}, '  # s에 현재노드 값들을 누적
            현재노드 = 현재노드.next
        return f'[{s[:-2]}]' # 마지막에 콤마하고 스페이스를 없애기 위해 슬라이싱

    def __iter__(self): # for문으로 요소들을 출력할 수 있게 한다.
        현재노드 = self.head.next # init값 필요없어서 init의 다음 값을 현재노드로 설정
        while 현재노드:
            yield 현재노드.data
            현재노드 = 현재노드.next

    def append(self, data): 
        새로운노드 = Node(data) # 데이터가 들어왔을 때 새로운 노드를 생성
        # 마지막 노드(self.tail)의 next값 None를 새로운 노드로 바꿔서 마지막 노드가 새로운 노드를 가리키게 한다.
        self.tail.next = 새로운노드 # init -> None에서 init -> 10이 된다.
        새로운노드.prev = self.tail
        self.tail = 새로운노드
        self.데이터수 += 1

    def insert(self, input_index, input_data): 
        현재노드 = self.head # init
        # [10, 20, 30, 40, 50, 15] 일때
        # index 3위치에 data 12를 집어넣기
        for i in range(input_index): # 3번 반복
            현재노드 = 현재노드.next # init -> 10, 10 -> 20, 20 -> 30, 현재노드는 30

        신규노드 = Node(input_data) # 값 12인 노드 생성
        신규노드.next = 현재노드.next # 12의 next를 30의 next인 40으로 변경 12 -> 40
        현재노드.next = 신규노드 # 30의 next를 40에서 12로 변경 30 -> 12 -> 40

        self.데이터수 += 1

    def pop(self):
        마지막값 = self.tail.data
        현재노드 = self.head # init

        for i in range(self.데이터수):
            if 현재노드.next is self.tail: # 현재노드.next 값이 self.tail 이면
                self.tail = 현재노드 # LinkedList의 마지막 값을 현재노드로 변경
                break # 현재노드가 마지막 값이면 멈춘다.
            현재노드 = 현재노드.next
        
        self.데이터수 -= 1
        return 마지막값 # 마지막 값을 반환하고 없앤다.

    def find(self, data):
        index = -1 # init노드가 맨 앞에 있기 때문에 0이 아닌 -1 부터 시작
        현재노드 = self.head # init

        for i in range(self.데이터수+1): # init노드가 맨 앞에 있기 때문에 +1
            if 현재노드.data == data: # 현재노드의 값과 매개변수로 받은 값이 같으면 인덱스 리턴, 현재노드.data는 init부터 시작
                return index
            index += 1
            현재노드 = 현재노드.next

        return -1 # 못찾으면 -1 리턴

dl = DoublyLinkedList()
dl.append(10)
dl.append(20)
dl.append(30)
dl.append(40)
dl.append(50)
dl.append(60)

print(dl)