#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int n, tmp;

  cin >> n;

  int card[6] = {1,2,3,4,5,6};

  n = n % 30;

  for (int i = 0; i < n; i++) {
    tmp = card[i%5];
    card[i%5] = card[i%5+1];
    card[i%5+1] = tmp;
  }

  for (int x : card) {
    cout << x;
  }

  cout << endl;

  return 0;
}
