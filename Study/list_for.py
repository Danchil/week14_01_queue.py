def insert_data(num, add):
    katok.append(None)
    print(katok)
    for i in range(len(katok)-1, num, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
        print(katok)

    print()
    katok[num] = add

def del_data(num):
    # katok[num] = None

    for i in range(num, len(katok)-1, 1):
        katok[i] = katok[i+1]
        katok[i+1] = None
        print(katok)
    del(katok[len(katok)-1])

katok = ['가', '나', '다', '라', '마']

del_data(0)
print(katok)
del_data(3)
# insert_data(2, '하')
print(katok)