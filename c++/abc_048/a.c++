#include <bits/stdc++.h>
using namespace std;

int main() {
  string line, S;
  getline(cin, line);
  S = "";

  S.push_back(line.at(0));
  for (int i = 1; i < line.size() - 1; i++) {
    if (line.at(i) == ' ') {
      S.push_back(line.at(i+1));
    }
  }
  cout << S << endl;
}