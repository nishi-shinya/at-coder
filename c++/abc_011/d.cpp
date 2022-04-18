#include <bits/stdc++.h>
using namespace std;

int dfs (int count, int nowX, int nowY) {
    if (count == N) {
        return 1;
    } else {
        return 0;
    }
}

int main () {
    int N, range, X, Y;
    cin >> N >> range;
    cin >> X >> Y;

    int MyX, MyY;

    double goalX, goalY;

    dfs()
    
    // if (X % range == 0 && Y % range == 0) {
    //     goalX = X / range;
    //     goalY = Y / range;

    //     double tmp, res;
    //     if ((N - goalX - goalY) == 0) {
    //         tmp = 1;
    //         res = (tmp) / (N * 4);
    //     } else {
    //         tmp = (N - goalX - goalY) / 2;
    //         res = (goalX * goalY) + (tmp * 4) / N * 4;
    //     }
    //     cout << res << endl;
    //     // cout << (N * 4) << endl;
    //     // for (int j = 0; j < 4; j++) {
    //     //     MyX = 0;
    //     //     MyY = 0;
    //     //     for (int i = 0; i < N; i++) {
    //     //         if (X != MyX) {
    //     //             if (MyX < X) {
    //     //                 MyX += range;
    //     //             } else {
    //     //                 MyX -= range;
    //     //             }
    //     //         } else if (Y != MyY) {
    //     //             if (MyY < Y) {
    //     //                 MyY += range;
    //     //             } else {
    //     //                 MyY -= range;
    //     //             }
    //     //         }
    //     //         if (MyX == X && MyY == Y) {
    //     //             cnt += 1;
    //     //         }
    //     //     }
    //     // }

    // } else {
    //     cout << "0.0" << endl;
    // }

}
