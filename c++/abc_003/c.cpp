#include <bits/stdc++.h>
using namespace std;
 
 int main() {
   int n,k,tmp;
   cin >> n >> k;

   double vec[n];
  
   for (int i = 0; i < n; i++) {
     cin >> tmp;
     vec[i] = tmp;
   }

   sort(vec, vec+n);

   double result = 0;

   for (int i = n-k; i < n; i++) {
     result = (result + vec[i]) / 2;
   }

   cout << fixed << setprecision(9) << result << endl;

   return 0;
 }