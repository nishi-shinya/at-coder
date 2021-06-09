#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    double mt = 0;
    cin >> n;
    vector<pair<int,int> > arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i].first >> arr[i].second;
    }
    double tmp = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            tmp = sqrtf(pow(max(arr[i].first, arr[j].first) - min(arr[i].first, arr[j].first), 2) + pow(max(arr[i].second, arr[j].second) - min(arr[i].second, arr[j].second), 2));
            mt = max(mt, tmp);
        }
    }

    cout << printf("%.6f", mt) << endl;

    return 0;
}