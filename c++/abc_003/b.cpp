#include <bits/stdc++.h>
using namespace std;
 
const static char WILD_CARD = '@';
const static set<char> WILD_CARD_SET = { 'a', 't', 'c', 'o', 'd', 'e', 'r', '@' };
 
int main() {
  string s,t;
  cin >> s >> t;

  bool result = true;
  for (int i = 0; i < s.length(); i++) {
    if (s[i] == WILD_CARD) {
			if (WILD_CARD_SET.end() == WILD_CARD_SET.find(t[i])) {
				result = false;
				break;
			}
    } else if (t[i] == WILD_CARD) {
			if (WILD_CARD_SET.end() == WILD_CARD_SET.find(s[i])) {
				result = false;
				break;
			}
    } else if (s[i] != t[i]) {
        result = false;
        break;
    }
  }
  
  if (result) {
    cout << "You can win" << endl;
  } else {
    cout << "You will lose" << endl;
  }
  return 0;
}

