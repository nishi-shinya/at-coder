#include <bits/stdc++.h>
using namespace std;

string board[60];

vector<int> dx = {1,1,0,-1,-1,-1,0,1};
vector<int> dy = {0,1,1,1,0,-1,-1,-1};

int main (void) {
  int x,y;
  cin >> x >> y;
  for (int i = 0; i < x; i++) cin >> board[i];

  for (int i = 0; i < x; i++) {
    for (int j = 0; j < y; j++){
      if(board[i][j] == '.') {
        int cnt = 0;
        for (int k = 0; k < 8; k++ ) {
          int x_t = i + dx[k];
          int y_t = i + dy[k];
          if (x_t >= 0 && x_t < x && y_t >= 0 && y_t < y && board[x_t][y_t] == '#') {
            cnt++;
          }
        }
        board[i][j] = '0' + cnt;
      }
    }
  }
  for (int i = 0; i < x; i++) cout << board[i] << endl;
  return 0;
}
