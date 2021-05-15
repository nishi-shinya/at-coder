#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
    string w;

    cin >> w;

    char chars[] = "aiueo";

    for (unsigned int i = 0; i < strlen(chars); ++i)
    {
        w.erase (std::remove(w.begin(), w.end(), chars[i]), w.end());
    }
    cout << w << endl;

    return 0;
}