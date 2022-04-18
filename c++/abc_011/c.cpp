#include <bits/stdc++.h>
using namespace std;

int main () {
  int N;
  cin >> N;

  vector<int> v;
  int tmp;

  for (int i = 0; i < 3; i++) {
    cin >> tmp;
    v.push_back(tmp);
  }

  int flg = false;

  if (*find(v.begin(), v.end(), N) == 0) {
    for (int i = 0; i < 100; i++) {
      if (*find(v.begin(), v.end(), N - 3) == 0 && (N - 3) >= 0) {
        N -= 3;
      } else if (*find(v.begin(), v.end(), N - 2) == 0 && (N - 2) >= 0) {
        N -= 2;
      } else if (*find(v.begin(), v.end(), N - 1) == 0 && (N - 1) >= 0) {
        N -= 1;
      }
      if (N == 0) {
        flg = true;
        break;
      }
    }
  }
  
  if (flg) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}