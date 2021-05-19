#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int t, n, m;

  cin >> t >> n;

  int a[n], tmp;

  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  cin >> m;

  int b[m];
  for (int i = 0; i < m; i++) {
    cin >> b[i];
  }

  int tmp_1, tmp_2, cnt;
  cnt = 0;
  bool flg = false;
  if (m <= n) {
    for (int i = 0; i < n; i++) {
      tmp_1 = a[i];
      tmp_2 = a[i] + t;
      for (int j = 0; j < m; j++) {
        if (tmp_1 <= b[j] && b[j] <= tmp_2) {
          cnt++;
          b[j] = 0;
          break;
        } else if (b[j] < tmp_1) {
          continue;
        }
      }
      if (m <= cnt) {
        break;
      }
    }
    if (m == cnt) {
      flg = true;
    }
  }

  if (flg) {
    cout << "yes" << endl;
  } else {
    cout << "no" << endl;
  }

  return 0;

}