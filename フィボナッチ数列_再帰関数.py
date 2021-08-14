'''
■フィボナッチ数列を再帰関数で求める
'''

def fibo(N):
    
    '''再帰関数を呼び出したことを報告する'''
    print("fibo(" + str(N) + ")を呼び出しました")
    
    '''ベースケース'''
    if N == 0:
        return 0
    elif N == 1:
        return 1
        
    '''再帰的に答えを求めて出力する'''
    result = fibo(N - 1) + fibo(N - 2)
    print(str(N) + "項目 = " + str(result) )
    
    return result

fibo(6)
