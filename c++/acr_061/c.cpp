#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;

    string tmp;

    int n = s.size() - 1;
    int sum = 0;

    for (int bit = 0; bit < (1<<n); ++bit) {
        tmp = s;
        /* bit で表される集合の処理を書く */


        /* きちんとできていることを確認してみる */
        // bit の表す集合を求める
        vector<int> S;
        for (int i = 0; i < n; ++i) {
            if (bit & (1<<i)) { // i が bit に入るかどうか
                // cout << i << endl;
                S.push_back(i);
            }
        }

        // // bit の表す集合の出力
        cout << bit << ": {";
        for (int i = (int)S.size(); i > 0; ++i) {
            tmp.insert(S[i]+1, "+", 1);
        }
        cout << tmp << endl;
        cout << "}" << endl;
    }

    return 0;
}