#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n, m, a, b, c;

  cin >> n >> m;

  if (m % 2 == 1) {
    b = 1;
    a = n - 1;
    c = 0;
    while (true) {
      if (a <= -1) {
        cout << "-1 -1 -1" << endl;
        break;
      }
      if ((2*a)+(3*b)+(4*c) == m) {
        cout << a << ' ' << b << ' ' << c << endl;
        break;
      }
      a-=1;
      c+=1;
    }
  } else {
    b = 0;
    a = n;
    c = 0;
    while (true) {
      if (a <= -1) {
        cout << "-1 -1 -1" << endl;
        break;
      }
      if ((2*a)+(3*b)+(4*c) == m) {
        cout << a << ' ' << b << ' ' << c << endl;
        break;
      }
      a-=1;
      c+=1;
    }
  }

  return 0;
}