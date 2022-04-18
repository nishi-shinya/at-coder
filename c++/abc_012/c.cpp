#include <bits/stdc++.h>
using namespace std;

int main () {
    int N;

    cin >> N;

    if (1944 <= N && N <= 2024) {
        int s;
        s = 2025 - N;

        for (int i = 1; i <= 9; i++) {
            if (s % i == 0) {
                if (s / i <= 9) {
                    cout << i << " x " << s / i << endl;
                }
            }
        }
    }

    return 0;
}