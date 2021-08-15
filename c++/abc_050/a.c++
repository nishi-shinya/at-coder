#include <bits/stdc++.h>
using namespace std;

int main () {
  string s;
  getline(cin, s);
  char p;
  vector<string> v;
  stringstream ss{s};
  string buf;
  while (std::getline(ss, buf, ' ')) {
    v.push_back(buf);
  }

  p = v.at(1).at(0);
  if (p == '+') {
    cout << stoi(v.at(0)) + stoi(v.at(2)) << endl;
  } else {
    cout << stoi(v.at(0)) - stoi(v.at(2)) << endl;
  }
}