#include <bits/stdc++.h>
using namespace std;

// nPnの順列に対して処理を実行する
void foreach_permutation(int n, std::function<void(int *)> f) {
  int indexes[n];
  for (int i = 0; i < n; i++) indexes[i] = i;
  do {
    f(indexes);
  } while (std::next_permutation(indexes, indexes + n));
}
 
int main() {
  int n;

  cin >> n;
  
  vector<int> c(n,0);

  for (int i = 0; i < n; i++) cin >> c[i];




  return 0;
}