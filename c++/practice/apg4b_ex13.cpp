#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, ave, tmp; cin >> n;
  vector<int> vec(n);
  for (int i = 0; i < n; i++) cin >> vec.at(i);

  tmp = 0;
  for (int i = 0; i < n; i++) {
    tmp += vec.at(i);
  }
  ave = floor(tmp / n);

  for (int i = 0; i < n; i++) {
    cout << abs(ave - vec.at(i)) << endl; 
  }
}