#include <bits/stdc++.h>
using namespace std;

int main(){
  int N, M; cin >> N >> M;
  vector<int> vec(M*2);

  for (int i = 0; i < M*2; i++) cin >> vec.at(i);

  for (int i = 1; i < N+1;i++) {
    cout << count(vec.begin(), vec.end(), i) << endl;
  }
}