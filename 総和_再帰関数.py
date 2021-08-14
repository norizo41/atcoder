'''
１からNまでの総和を計算する再帰関数
'''

def fnc(N):
    
    '''
    再帰関数を呼び出したことを報告する
    '''
    print("fnc(" + str(N) + ")を呼び出しました")
    
    if N == 0:
        return 0
    
    '''
    再帰的に答えを呼び出して出力する
    '''
    result = N + fnc(N - 1)
    print(str(N) + "までの和 = " + str(result))
    
    return result
    
fnc(5)
