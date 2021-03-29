#include <bits/stdc++.h>
using namespace std;

set<int> d;

int main (void) {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    int tmp;
    cin >> tmp;
    d.insert(tmp);
  }

  cout << d.size() << endl;
}
