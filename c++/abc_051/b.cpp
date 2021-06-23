#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; ++i)
using ll = long long;
using P = pair<int,int>;

int main() {
  int k,s,cnt;
  cnt = 0;
  cin >> k >> s;

  for (int x = 0; x <= k; x++) {
    for (int y = 0; y <= k; y++) {
      int z = s - x - y;
      if (z >= 0 && z <= k) {
        cnt++;
      }
    }
  }

  cout << cnt << endl;

  return 0;
}