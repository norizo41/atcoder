'''
■ナップサック問題
N個の品物があり、i(=0,1,...,N-1)番目の品物の重さはweight_i, 
価値はvalue_iで与えられます。

このN個の品物から、重さの総和がWを超えないように、いくつか選びます。
選んだ品物の価値の総和として考えられる最大値を求めてください。
(ただし、Wやweight_iは0以上の整数とします)
'''

'''
■動的計画法の部分問題の作り方の基本パターン
N個の対象物{0, 1, ... ,N-1}に関する問題に対して、
最初のi個の対象物{0, 1, ... ,i-1}に関する部分問題として考えます。
'''

'''
■ナップサック問題に対する動的計画法
dp[i][w] ← 最初のi個の品物{0, 1, ... ,i-1}
までの中から重さがwを超えないように選んだときの、
価値の総和の最大値
'''

N = int(input())
W = int(input())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0] * (W+1) for _ in range(N+1)]

def chmax(a, b):
    if a < b:
        a = b
    return a

for i in range(N):
    
    for w in range(W+1):
    
        '''i番目の品物を選ぶ場合'''
        if w - weight[i] >= 0:
            dp[i+1][w] = chmax(dp[i+1][w], dp[i][w - weight[i]] + value[i])
        
        '''i番目の品物を選ばない場合'''
        dp[i+1][w] = chmax(dp[i+1][w],dp[i][w])
    

'''最適値の出力'''
print(dp[N][W])
