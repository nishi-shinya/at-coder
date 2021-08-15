#include <bits/stdc++.h>
using namespace std;

int main () {
  int n; cin >> n;
  vector<int> math(n);
  vector<int> english(n);

  for (int i = 0; i < n; i++) cin >> math.at(i);
  for (int i = 0; i < n; i++) cin >> english.at(i);

  for (int i = 0; i < n; i++) {
    cout << math.at(i) + english.at(i) << endl;
  }
}