'''
■部分和問題を再帰関数で解く

部分和問題：
N個の正の整数 a_0, a_1, ..., a_N-1 と正の整数Wが与えられます。
a_0, a_1, ..., a_N-1 の中から何個かの整数を選んで
総和をWとすることができるかどうかを判定してください。

方針：
●N-1個の整数 a_0, a_1, ..., a_N-2 から W を作れるかどうか
●N-1個の整数 a_0, a_1, ..., a_N-2 から W - a_N-1 を作れるかどうか
という2つの少問題に帰着させ、少なくとも一方が正しいか否かを確かめる。
'''

'''入力'''
N, W = map(int, input().split())
a = list(map(int, input().split()))

'''
部分和問題を解く再帰関数：
bool fnc(int i, in w) ← a_0, a_1, ..., a_N-1のうちの
最初のi個 (a_0, a_1, ..., a_i-1)から何個か選んで、
総和をwにできるかどうかをブール値で返す関数
'''
def fnc(i, w):
     
    '''ベースケース'''
    if i == 0:
        if w == 0:
            return True
        else:
            return False   
    
    '''a[i-1]を選ばない場合'''
    if fnc(i-1, w):
        return True
    
    '''a[i-1]を選ぶ場合'''
    if fnc(i-1, w-a[i-1]):
        return True
    
    return False
            
if fnc(N, W):
    print("Yes")
else:
    print("No")
