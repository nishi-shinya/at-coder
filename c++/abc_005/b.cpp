#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n, tmp;

  cin >> n;

  int t[n];

  for (int i = 0; i < n; i++) {
    cin >> tmp;
    t[i] = tmp;
  }

  sort(t, t+n);

  cout << t[0] << endl;

  return 0;
}
