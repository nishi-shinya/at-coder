#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n;
  int tmp;
  string s;
  map<string,int> mp{};

  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> s;
    if (mp.count(s)) {
      tmp = mp[s];
      tmp++;
      mp[s] = tmp;
    } else {
      mp.emplace(s,1);
    }
  }

  int m;
  cin >> m;

  for (int i = 0; i < m; i++) {
    cin >> s;
    if (mp.count(s)) {
      tmp = mp[s];
      tmp--;
      mp[s] = tmp;
    }
  }

  int mx = 0;

  for (auto i = mp.begin(); i != mp.end(); i++) {
    mx = max(i->second,mx);
  }

  cout << mx << endl;
  return 0;
}
