#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, y;

    cin >> n >> y;

    for (int a = 0; a <= n; a++) {
        for (int b = 0; b <= n; b++) {
            int c = n - a - b;
            if (0 <= c && ((10000*a) + (5000*b) + (1000*c)) == y) {
                cout << a << ' ' << b << ' ' << c << endl;
                return 0;
            }
        }
    }

    cout << "-1 -1 -1" << endl;
    
    return 0;
}