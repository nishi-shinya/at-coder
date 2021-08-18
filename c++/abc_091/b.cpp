#include <bits/stdc++.h>
using namespace std;

int main () {
  int N,M; cin >> N;
  vector<string> S(N);
  set<string> st;
  string tmp;
  for (int i=0; i<N; i++) {
    cin >> tmp;
    S.at(i) = tmp;
    st.insert(tmp);
  };
  cin >> M;
  vector<string> T(M);
  for (int i=0; i<M; i++) cin >> T.at(i);
  
  for (int i=0; i<M; i++) {
    auto r = find(S.begin(), S.end(), T.at(i));
    if (r == S.end()) continue;
    const int wanted_index = distance(S.begin(), r);
    S.erase(S.begin() + wanted_index);
    N--;
  }

  int res = 0;
  int tmp_i = 0;
  for (const auto& e: st) {
    tmp_i = count(S.begin(),S.end(), e);
    if (res < tmp_i) {
      res = tmp_i;
    }
  }

  cout << res << endl;
}