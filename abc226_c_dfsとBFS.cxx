#include <bits/stdc++.h>

using namespace std;

#define rep(i, n)			for (int i = 0	; i < (int)(n); i++)
#define repA(i, s, n)		for (int i = (s); i < (int)(n); i++)
#define repB(i, n, p)		for (int i = 0	; i < (int)(n); i += p)
#define repAB(i, s, n, p)	for (int i = (s); i < (int)(n); i += p)

struct Struct {
	
	int i;int score;
	
	Struct() {}

	// 最後のconstを忘れると"instantiated from here"というエラーが出てコンパイルできないので注意
	bool operator<(const Struct& right ) const {
		//return true;
		return score < right.score;
	}
    
};

/*****************
 * プロトタイプ宣言 * 
******************/
void foreach_permutation(int n, std::function<void(int *)> f);	// nPnの順列に対して処理を実行する
void foreach_comb(int n, int k, std::function<void(int *)> f);	// nCkの組み合わせに対して処理を実行する
template <typename T> T gcd(T x, T y);							// ユークリッドの互除法で最大公約数を求める
template <typename T> long long baseT_to_long(string X, T t);	// T進数から10進数に変換する
template <typename T> string long_to_baseT(long long x, T t);	// 10進数からT進数に変換する

using Graph = vector<vector<int>>;
vector<bool> used;
void dfs(Graph &G, int v, long long& ans){
	
	ans += G[v][0]; //習得に要した時間を計上する
	used[v] = true; //習得済にする
	
	int ln = G[v].size();
	repA(next_v, 1, ln) {
		if (used[G[v][next_v]]) continue; //習得済みなら何もしない
		dfs(G, G[v][next_v], ans);//再帰的に別の技を習得する
	}
	
}

void BFS(Graph &G, int s, long long& ans) {
	int N = G.size();
	
	vector<int> dist(N, -1);//全頂点を「未訪問」に初期化
	queue<int> que;
	
	//初期条件(頂点sを初期頂点とする)
	dist[s] = 0;
	que.push(s); //sを初期頂点とする
	
	//BFS開始(キューが空になるまで探索を行う)
	while(!que.empty()) {
		int v = que.front();//キューから先頭点を取り出す
		que.pop();
		
		//新たな技なので時間を追加する
		ans += G[v][0];
		
		//vからたどれる頂点をすべて調べる
		int ln = G[v].size();
		repA(next_v, 1, ln) {
			//すでに発見済みの頂点は探索しない
			if (dist[G[v][next_v]] != -1) continue;
			
			//新たな頂点xについて距離情報を更新してキューに挿入
			dist[G[v][next_v]] = dist[v] + 1;
			que.push(G[v][next_v]);
			
		}
		
	}
	
}


/********
 * main * 
********/
int main() {
	
	int N; cin >> N;
	//メモ化用配列をfalseで初期化する
	used.assign(N+1, false);
	
	Graph G(N+1);
	
	//技は1から数えるため、G[0]にダミーの隣接リストを入れておく
	vector<int> dummy{-1};
	G.push_back(dummy);
	used[0] = true;
	
	rep(i, N) {
		
		long long T; cin >> T;
		G[i+1].push_back(T);
		
		int K; cin >> K;
		rep(_, K) {
			int a; cin >> a;
			G[i+1].push_back(a);
		}
		
	}
	
	long long ans = 0;
	//dfs(G, N, ans);
	BFS(G, N, ans);
	cout << ans << endl;
}

// nPnの順列に対して処理を実行する
void foreach_permutation(int n, std::function<void(int *)> f) {
  int indexes[n];
  for (int i = 0; i < n; i++) indexes[i] = i;
  do {
    f(indexes);
  } while (std::next_permutation(indexes, indexes + n));
}

// nCkの組み合わせに対して処理を実行する
void recursive_comb(int *indexes, int s, int rest, std::function<void(int *)> f) {
  if (rest == 0) {
    f(indexes);
  } else {
    if (s < 0) return;
    recursive_comb(indexes, s - 1, rest, f);
    indexes[rest - 1] = s;
    recursive_comb(indexes, s - 1, rest - 1, f);
  }
}
void foreach_comb(int n, int k, std::function<void(int *)> f) {
  int indexes[k];
  recursive_comb(indexes, n - 1, k, f);
}

// ユークリッドの互除法で最大公約数を求める
template <typename T>
T gcd(T x, T y) {
	return (x % y) ? gcd(y, x % y) : y;
}

// T進数から10進数に変換する
template <typename T>
long long baseT_to_long(string X, T t) {
	
	int ln = X.size();
	long long x = 0;
	rep(i, ln) {
		long long a = (long long)(int(X[i]-'0'));
		long long b = 1;
		//pow
		rep(j, ln-(i+1)) b *= t;
		x += a * b;
	}
	
	return x;
}

// 10進数からT進数に変換する
template <typename T>
string long_to_baseT(long long x, T t) {
	
	if (x == 0) return "0";
	
	string X = "";
	long long r = -1;
	while (x != 0) {
		r = x % t;
		x /= t;
		if (!(r == 0 && x == 0)) X = to_string(r) + X;
	}
	
	return X;
}
