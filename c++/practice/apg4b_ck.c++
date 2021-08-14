#include <bits/stdc++.h>
using namespace std;

int main () {
  string S;
  getline(cin,S);

  int res = 0;
  char p;
  for (int i = 0; i < S.size(); i++) {
    if (i % 2 == 1) {
      p = S.at(i);
    } else if (p == '+') {
      res++;
    } else if (p == '-') {
      res--;
    } else {
      res++;
    }
  }
  cout << res << endl;
}