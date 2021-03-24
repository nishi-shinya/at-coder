#include <bits/stdc++.h>
using namespace std;

int main () {
  int n, i, res;
  int tmp = 0;
  int tmp_2 = 0;
  cin >> n;
  vector<int> v(n);
  for (i = 0;i < n; i++ ){
    cin >> v[i];
  }
  for (i = 2; i < 1000; i++) {
    tmp = 0;
    for (int j = 0; j < n; j++){
      if (v[j] % i == 0) {
        tmp++;
      }
    }
    if (tmp_2 < tmp) {
      tmp_2 = tmp;
      res = i;
    }
  }
  cout << res << endl;
}
