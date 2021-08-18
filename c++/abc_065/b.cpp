#include <bits/stdc++.h>
using namespace std;

int main() {
  int N; cin >> N;
  vector<int> vec(N);
  for (int i = 0; i<N;i++) cin >> vec.at(i);

  int count = 0;
  int button = 0;
  while (true) {
    button = vec.at(button) - 1;
    count++;
    if (button == 1) {
      cout << count << endl;
      break;
    }
    if (count > N) {
      cout << "-1" << endl;
      break;
    }
  }
}