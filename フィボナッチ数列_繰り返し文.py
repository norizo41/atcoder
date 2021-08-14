'''
■フィボナッチ数列をfor文による反復で求める
'''

'''
50項目を再帰関数で求めようとすると、
計算量が爆発してしまう
'''
F = []

''' F[0] = 0 '''
F.append(0)
''' F[1] = 1 '''
F.append(1)

for N in range(2, 50):
    F.append(F[N - 1] + F[N - 2])
    print(str(N) + "項目：" + str(F[N]))
