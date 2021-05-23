#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n, tmp; cin >> n;
  vector <int> a;
  for (int i = 0;i<n;i++) { 
    cin >> tmp;
    auto result = find(a.begin(), a.end(), tmp);
    if (result == a.end()) {
      a.push_back(tmp);
    }
  }

  sort(a.begin(), a.end(), greater<int>());

  cout << a[1] << endl;

  return 0;
}