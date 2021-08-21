'''
■編集距離
2つの文字列S, Tが与えられます。Sに以下の3通りの操作を繰り返し実施することで
Tに変換したいものとみなします。そのような一連の操作のうち、
操作回数の最小値を求めてください。
なお、この最小値をSとTとの編集距離とよびます。
    ●変更：S中の文字を1つ選んで任意の文字に変更する
    ●削除：S中の文字を1つ選んで削除する
    ●挿入：Sの好きな箇所に好きな文字を1文字挿入する
'''

INF = 10 ** 12

'''緩和処理'''
def chmin(a, b):
    if a > b:
        a = b
    return a

'''入力'''
S, T = map(str, input().split())
M = len(S)
N = len(T)

'''DPテーブル定義'''
dp = [ [INF] * (N + 1) for _ in range(M + 1)]

'''DP初期条件'''
dp[0][0] = 0;

'''DPループ'''
for i in range(M+1):
    for j in range(N+1):
        
        '''●変更操作(Sのi文字目とTのj文字目を対応させる)'''
        if i > 0 and j > 0:
            
            if S[i-1] == T[j-1]:
                '''同じ文字の場合はコストを増やさずに済む'''
                dp[i][j] = chmin(dp[i][j], dp[i-1][j-1])
            
            else:
                '''文字が違う場合は変更操作が必要となる'''
                dp[i][j] = chmin(dp[i][j], dp[i-1][j-1] + 1)
                
        '''●削除操作(Sのi文字目を削除)'''
        if i > 0:
            dp[i][j] = chmin(dp[i][j], dp[i-1][j] + 1)
        
        
        '''●挿入操作(Tのj文字目を削除)'''
        if j > 0:
            dp[i][j] = chmin(dp[i][j], dp[i][j-1] + 1)

for i in range(M+1):
    for j in range(N+1):
        print(dp[i][j], end=' ')
    print()

print()
'''答えの出力'''
print(dp[M][N])
