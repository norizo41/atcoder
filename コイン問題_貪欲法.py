'''
■コイン問題
500円玉, 100円玉, 50円玉, 5円玉, 1円玉がそれぞれ
a_0, a_1, a_2, a_3, a_4, a_5枚あります。
これらを用いてX円を支払いたいとします。ここで、支払いに用いる
コインの合計枚数をなるべく少なくしたいと考えています。
最小で何枚のコインを支払うことができるでしょうか。
ただし、
そのような支払い方が少なくとも1つは存在するものとします。 
'''

'''
方針：
「大きな額のコインから優先的に使う」という素朴な直感に基づく
以下の解法で最適解を導くことができる。
    1. まずX円を超えない範囲で500円玉をできるだけ多く使います
    2. 残った金額に対して100円玉をできるだけ多く使います
    3. 残った金額に対して50円玉をできるだけ多く使います
    4. 残った金額に対して10円玉をできるだけ多く使います
    5. 残った金額に対して5円玉をできるだけ多く使います
    6. 最後に、残った金額に対して1円玉を用いて支払います
'''

'''コインの金額'''
V = [500, 100, 50, 10, 5, 1]

'''入力'''
X = int(input())
A = list(map(int, input().split()))

'''貪欲法'''
result = 0
for i in range(len(V)):
    
    '''枚数制限がない場合の枚数'''
    add = X // V[i]
    
    '''枚数制限を考慮'''
    if add > A[i]:
        add = A[i]
    
    '''残り金額を求めて、答えに枚数を加算する'''
    X -= V[i] * add
    result += add

'''出力'''
print(result)
