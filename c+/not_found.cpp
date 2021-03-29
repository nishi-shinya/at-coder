#include <bits/stdc++.h>
using namespace std;

string S;
vector<char> alf;

int main(void) {
  char moji;
  for (moji = 'a'; moji <= 'z'; ++moji) {
    alf.push_back(moji);
  }
  cin >> S;
  sort(S.begin(), S.end());
  string res = "";

  for (char x : alf) {
    if (S.find(x) == string::npos) {
      res = x;
      break;
    }
  }

  if (res == "") {
    cout << "None" << endl;
  } else {
    cout << res << endl;
  }
  return 0;
}
