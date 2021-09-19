#include <stdio.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

//十分大きい値とする
const int INF = 1000000000;

int main() {
	
	vector<string> ary(3);
	for (int i = 0; i < 3; ++i) cin >> ary[i];
	string T;
	cin >> T;
	
	string ans = "";
  int tSize = T.size();
	for (int i = 0; i < tSize; ++i) {
		int x = int(T[i]-'0');
		ans += ary[x-1];
	}
	cout << ans << endl;
	
}
