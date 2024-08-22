#include <bits/stdc++.h>
#define ALL(X) X.begin(), X.end()
using namespace std;


int main() {
	cin.tie(0)->sync_with_stdio(0);
	int n, k;
	vector<int> v;

	cin >> n >> k;
	v.resize(n);
	for (int& x : v) cin >> x;
	nth_element(v.begin(), v.begin() + k - 1, v.end());
	cout << v[k - 1];
}