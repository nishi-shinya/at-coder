#include <iostream>
#include <stdio.h>

int binary_search(int a[],int n, int key) {
  int left, mid = 0;
  int right = n;

  while (left < right) {
    mid = (left + right) / 2;
    if (a[mid] == key) {
      return 1;
    } else if (key < a[mid]) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }
  return 0;
}


int main () {
  int i, n, a[10000+1], q, key, sum = 0;

  scanf("%d", &n);
  for ( i = 0; i < n; i++ ) scanf("%d", &a[i]);

  scanf("%d", &q);
  for (i = 0; i < q; i++ ) {
    scanf("%d", &key);
    if (binary_search(a,n,key)) sum++;
  }
  printf("%d\n", sum);

  return 0;
}
