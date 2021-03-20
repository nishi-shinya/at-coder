#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

string a[1000000], n;

int str_search (int j, string key) {
  int sum = 0;
  j--;
  while (j >= 0) {
    if (key == a[j]) {
      return 1;
    }
    j--;
  }
  return 0;
}


int main () {
  int i, n, key, sum = 0;
  int count = 0;
  int count_2 = 0;
  vector<string> res_arr(n);

  scanf("%d", &n);
  for (i = 0; i < n; i++) {
    int res = 0;
    string command;
    string stri;
    cin >> command >> stri;
    if (command == "insert") {
      a[count] = stri;
      count++;
    } else if (command == "find") {
      res = str_search(count, stri);
      if (res == 1) {
        res_arr[count_2] = "yes";
      } else {
        res_arr[count_2] = "no";
      }
      count_2++;
    }
  }

  for (i = 0; i < count_2; i++) {
    cout << res_arr[i] << endl;
  }

  return 0;
}
