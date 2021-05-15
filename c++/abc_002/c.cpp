#include <iostream>
#include <string>
#include <algorithm> 
#include <iomanip>
#include <limits>
using namespace std;


int main(){
    double xa, ya, xb, yb, xc, yc;

    cin >> xa >> ya >> xb >> yb >> xc >> yc;

    xb -= xa;
    xc -= xa;
    yb -= ya;
    yc -= ya;

    cout << fixed << setprecision(2) << abs((xb * yc) - (xc * yb)) / 2 << endl;

    return 0;
}