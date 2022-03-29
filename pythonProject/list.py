P = input("파티에 몇명이 참석하나요? :")
guests = []
for steps in range(int(P)):
    L = input("초대 할 사람의 이름을 입력해주세요")
    guests.append(L)
    guests.sort()
    print(guests)
