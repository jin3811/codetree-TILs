#include <bits/stdc++.h>
#define ALL(X) X.begin(), X.end()
using namespace std;

int main() {
    string str;
    cin >> str;
    
    sort(ALL(str));
    str.erase(unique(ALL(str)), str.end());
    cout << (str.length() >= 2 ? "Yes" : "No");
}