#include <bits/stdc++.h>
using namespace std;

int main() {
    int N,k;
    vector<long> d(100);
    cin >> N >> k;
    for (int i = 1; i <= N; i++) cin >> d[i];

    vector<long> num(100);  // バケット
    for (int i = 1; i <= N; i++) {
        num[d[i]]++;  // d[i] が 1 個増える
    }

    sort(num.begin(), num.end());

    int mx = 0;
    int res = 0;

    for (long i = num.size(); i >= num.size() - N; i--) {
      if (mx >= k) {
        res = res + num[i];
      }
      if (num[i] != 0) {
        mx++;
      };
    }
    cout << res << endl;
}
