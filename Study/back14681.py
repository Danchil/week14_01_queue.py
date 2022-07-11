#20220524
# position = ()
# for i in range(2):
#     position[i] = int(input())
# print(position)
# 튜플 삽입 불가능

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")

#     #설마시발...출력을 정수로 해서? 아니엿음 ㅎㅎ
#     #레전드.. 제3사분면을 둘 다 양수로 받을떄로 함 히ㅏ