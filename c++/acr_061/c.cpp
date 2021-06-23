#include <bits/stdc++.h>
#include <sstream> // std::stringstream
#include <istream> // std::getline
using namespace std;
typedef long long ll;

int main(){
    string s;
    cin >> s;

    string tmp;

    int n = s.size() - 1;
    ll sum = 0;

    for (int bit = 0; bit < (1<<n); ++bit) {
        tmp = s;

        ll sm = 0;
        ll a = s[0] - '0';

        for (int i = 0; i < n; ++i) {
            if (bit & (1<<i)) {
                sm += a;
                a = 0;
            }
            a = a * 10 + s[i + 1] - '0';
        }

        sm += a;
        sum += sm;

    }

    cout << sum << endl;

    return 0;
}