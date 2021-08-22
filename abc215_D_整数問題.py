'''
AtCoder Beginner Contest 215
D - Coprime 2

■解説
gcd(a, b) != 1であるとは、aとbとが何らかの共通の素因数を持っているということです。
このことから、エラトステネスの篩の要領の、以下の解法が成立します。
    ●集合Sに1からMまでの全ての整数を入れる
    ●iが1からNまで、以下を繰り返す
        ・A_iを素因数分解する素因数の集合をPとする
        ・Pに含まれる全ての素因数kについて、
            「Sからkの倍数のすべてを削除するという操作を行う」
        ・なお、全体を通して同じ素因数に関して2ど以上操作を行う必要がないことを
            利用して、計算量を改善できる
            (この部分を行わないとTLEします)
    ●操作終了後にSに残った整数が解である
とる方針により計算量は変化しますが、素因数分解をO(sqrt(max A))で行うことにより、
遅くとも時間計算量O(N * sqrt(max A))の解法が達成されます。
'''

N, M = map(int, input().split())
A = list(map(int, input().split()))

def pfact(x):
    res = []
    i = 2
    while i ** 2 <= x:
        while x % i == 0:
            x //= i
            res.append(i)
        i += 1
    if x != 1:
        res.append(x)
    return res

SIZE = (10 ** 5) + 5
fl = [True] * SIZE

for i in range(N):
    a = A[i]
    v = pfact(a)
    for nx in v:
        if fl[nx]:
            for j in range(nx, SIZE, nx):
                fl[j] = False

cnt = 0
ans = ''
for i in range(1, M+1):
    if fl[i]:
        cnt += 1
        ans += str(i) + '\n'

print(cnt)
print(ans)
