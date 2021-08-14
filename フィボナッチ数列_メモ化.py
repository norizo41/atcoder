'''
■フィボナッチ数列を求める再帰関数をメモ化
'''

N = 50

'''
fibo(N)の答えをメモ化する配列
-1で初期化する
'''
memo = [-1] * N

def fibo(N):
    
    '''ベースケース'''
    if N == 0:
        return 0
    elif N == 1:
        return 1
    
    '''
    メモをチェック
    (すでに計算済みならば答えをリターンする)
    '''
    if memo[N] != -1:
        return memo[N]
    
    '''答えをメモしながら、再帰呼び出し'''
    memo[N] = fibo(N - 1) + fibo(N - 2)
    return memo[N]

'''fibo(N-1)を呼び出す'''
fibo(N-1) 

'''memo[0], ..., memo[49]に答えが格納されている'''
for i in range(2, N):
    print(str(i) + " 項目：" + str(memo[i]))   
    
