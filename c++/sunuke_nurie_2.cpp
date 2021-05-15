#include <bits/stdc++.h>
using namespace std;

int main (void) {
  int x1 = 0;
  int y1 = 0;
  int w,h,n;
  cin >> w >> h >> n;
  int y2 = h;
  int x2 = w;
  for (int i = 0; i < n; i++) {
    int x;
    int y;
    int a;
    cin >> x >> y >> a;
    if (a == 1) {
      x1 = x;
    } else if (a == 2) {
      x2 = x;
    } else if (a == 3) {
      y1 = y;
    } else {
      y2 = y;
    }
  }
  int res = 0;
  res = (x2 - x1) * (y2 - y1);
  if (res < 0) {
    cout << 0 << endl;
  } else {
    cout << res << endl;
  }
  return 0;
}
