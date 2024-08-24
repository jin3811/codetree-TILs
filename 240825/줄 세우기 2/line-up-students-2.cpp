#include <bits/stdc++.h>
#define ALL(X) X.begin(), X.end()
#define endl '\n'
using namespace std;
using ti3 = tuple<int,int,int>;

int main() {
	cin.tie(0)->sync_with_stdio(0);
	int w, h, n;
	vector<ti3> v;
	cin >> n;
	v.resize(n);
	for(int i = 0; i < n; i++) {
		auto& [h, w, num] = v[i];
		cin >> h >> w;
		w = -w;
		num = i + 1;
	}
	sort(ALL(v));
	for(auto& [h, w, num] : v) {
		cout << h << ' ' << -w << ' ' << num << endl;
	}
}