#include <algorithm>
#include <iostream>
#include <map> 
#include <stdio.h>
#include <string>
#include <sstream>
#include <unordered_set>
#include <vector>
using namespace std;

//十分大きい値とする
const int INF = 1000000000;

struct data_t {
	
    string str;
    string toSort;
    
    data_t(string str, vector<char> chs) { 
		this->str = str;
		string tmp = "";
		int chsSize = chs.size();
		for (int i = 0; i < chsSize; ++i) {
			std::vector<char>::iterator iter = std::find(chs.begin(), chs.end(), str[i]);
			int index = std::distance(chs.begin(), iter);
			tmp += char(index + 97);
		}
		this->toSort = tmp;
	}

    // 最後のconstを忘れると"instantiated from here"というエラーが出てコンパイルできないので注意
    bool operator<( const data_t& right ) const {
        return toSort == right.toSort ? toSort < right.toSort : toSort < right.toSort;
    }
    
};


int main() {
	
	string X;
	cin >> X;
	int xSize = X.size();
	vector<char> chs(xSize);
	for (int i = 0; i < xSize; ++i) chs[i] = X[i];
	
	int N;
	cin >> N;
	vector<data_t> S;
	for (int i = 0; i < N; ++i) {
		string str;
		cin >> str;
		S.push_back(data_t(str, chs));
	}
	
	std::sort(S.begin(), S.end());
	
	for (int i = 0; i < N; ++i) {
		cout << S[i].str << endl;
	}
}
