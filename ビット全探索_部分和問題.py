'''
部分和問題
N個の整数a0, a1, ... ,aN-1と正の整数Wが与えられます。
a0, a1, ... , aN-1の中から何個か整数を選んで総和をWとすること
ができるかどうかを判定してください。
'''
N, W = map(int, input().split())
A = list(map(int, input().split()))
B = [format(x, '0'+ str(N) +'b') for x in range(1,N ** 2)]

exist = False;
for bits in B:
    sm = 0;
    for i in range(N):
        bit = int(bits[i])
        sm += A[i] * bit
    if sm == W:
        exist = True
if exist:
    print('Yes')
else:
    print('No')
