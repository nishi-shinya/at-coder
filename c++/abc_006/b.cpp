#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n;
  cin >> n;

  vector<long int> a(n,0);
  a[2]=1;

  for (int i = 3; i < n; i++) {
    a[i]=(a[i-3]+a[i-2]+a[i-1])%10007;
  }

  cout << a[n-1] << endl;

  return 0;
}