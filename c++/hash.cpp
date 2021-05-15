#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

#define M 1046527
#define NIL (-1)
#define L 14

char H[M][L];

// 文字列から数値に変換
int getChar (char ch) {
  if (ch == "A") return 1;
  else if (ch == "C") return 2;
  else if (ch == "G") return 3;
  else if (ch == "T") return 4;
  else return 0;
}

// 文字列から数値に変換してkeyを作成する。
long long getKey (char str[]) {
  long long sum = 0, p = 1, i;
  for (i = 0; i < strlen(str); i++ ){
    sum += p*(getChar(str[i]));
    p *= 5;
  }
  return sum;
}
