#include <bits/stdc++.h>
using namespace std;

int main () {
    int N;

    int H = 0;
    int m = 0;
    int s = 0;

    cin >> N;

    if (N >= 3600) {
        H = (N / 3600);
        N %= 3600;
        if (N >= 60) {
            m = (N / 60);
            N %= 60;
        }
        s = N;
        cout << setfill('0') << right << setw(2) << H << ":" << setfill('0') << right << setw(2) << m << ":" << setfill('0') << right << setw(2) << s << endl;
        return 0;
    } else if (N >= 60) {
        m = (N / 60);
        N %= 60;
        s = N;
        cout << "00:" << setfill('0') << right << setw(2) << m << ":" << setfill('0') << right << setw(2) << s << endl;
        return 0;
    }

    s = N;
    cout << "00:00:" << setfill('0') << right << setw(2) << s << endl;
    return 0;
}