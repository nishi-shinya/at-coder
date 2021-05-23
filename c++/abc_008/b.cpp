#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n;

  cin >> n;

  vector <string> s(n, "0");

  string tmp;

  set<string> st;

  for (int i = 0; i < n; i++) {
    cin >> tmp;
    s[i] = tmp;
    st.insert(tmp);
  }

  int cnt = 0;
  int o = 0;
  for (auto x : st) {
    o = count(s.begin(), s.end(), x);
    if (cnt <= o) {
      cnt = o;
      tmp = x;
    }
  }

  cout << tmp << endl;

  return 0;
}