#include <bits/stdc++.h>
using namespace std;

int main () {
  string s;
  getline(cin, s);
  char p;
  int sum = 0;
  int count = 0;

  vector< string> v;

  stringstream ss{s};
  string buf;
  while (std::getline(ss, buf, ' ')) {
    v.push_back(buf);
  }

  sum = v[0] + v[2];

  // for (int i = 0; i < v.size(); i++) {
  //   if (i == 1) {
  //     if (v[i] == "+") {

  //     } else {

  //     }
  //   }
  // }
  // cout << sum << endl;
}