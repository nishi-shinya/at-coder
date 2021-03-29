#include <bits/stdc++.h>
using namespace std;

vector <int> vec;

int main (void) {
  int n,m;
  int a,b;
  cin >> n >> m;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    vec.push_back(a);
    vec.push_back(b);
  }

  for (int i = 1; i <= n; i++) {
    cout << count(vec.begin(),vec.end(), i) << endl;
  }
  return 0;
}
