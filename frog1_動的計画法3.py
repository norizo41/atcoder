'''
■AtCoder Educational DP Contest A - Frog 1
N個の足場があって、(i=0,1,...,N-1)番目の
足場の高さはhiで与えられます。最初0番目の足場にカエルがいて、
以下のいずれかの行動を繰り返してN-1番目の足場を目指します。
    ●足場iから足場i+1へと移動する(コストは|h_i-h_i+1|)
    ●足場iから足場i+2へと移動する(コストは|h_i-h_i+2|)
カエルがN-1番目の足場にたどり着くまでに
要するコストの総和の最小値を求めてください。
'''

'''
入力
'''
N = int(input())
h = list(map(int, input().split()))

'''
緩和処理を実現するための関数chminを定義する
'''
def chmin(a, b):
    if a > b:
        a = b
    return a

'''
十分大きな値とする
'''
INF = 2 ** 60
'''
配列dpを定義(配列全体を無限大に表す値に初期化)
'''
dp = [INF] * N
'''
初期条件
'''
dp[0] = 0;

'''
今回は、Frog問題を「配る遷移方式」で解く
'''
for i in range(N):
    if i+1 < N:
        dp[i+1] = chmin(dp[i+1], dp[i] + abs(h[i] - h[i+1]));
    if i+2 < N:
        dp[i+2] = chmin(dp[i+2], dp[i] + abs(h[i] - h[i+2]));

'''
答えを出力
'''
print(dp[N-1])
