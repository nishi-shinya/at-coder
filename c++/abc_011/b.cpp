#include <bits/stdc++.h>
using namespace std;

int main () {
	char str[12];
  std::cin >> str;
	char *p;

	p = str;
  for (int i = 0; i < 12; i++) {
    if (!str[i]) {
      continue;
    }
    if (i == 0) {
      *p = toupper (*p);
    } else {
      *p = tolower (*p);
    }
		p++;
  }
	cout << str << endl;
}