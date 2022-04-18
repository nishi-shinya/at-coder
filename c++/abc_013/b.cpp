#include <bits/stdc++.h>
using namespace std;

int main () {
    int A, B;
    cin >> A;
    cin >> B;

    vector<int> display;

    // [1,2,3,4,5,6,7,8,9]

    for (int i = 0; i <= 9; i++) display.push_back(i);

    int A_i, B_i;
    for (int i = 0; i <= 9; i++) {
        if (display[i] == A) {
            A_i = i;
        }
        if (display[i] == B) {
            B_i = i;
        }
    }

    if (A_i > B_i) {
        cout << min(A_i - B_i, 10 - (A_i - B_i)) << endl;
    } else {
        cout << min(B_i - A_i, 10 - (B_i - A_i)) << endl;
    }
}