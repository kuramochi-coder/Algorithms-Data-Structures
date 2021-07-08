#include <bits/stdc++.h>
using namespace std;

int nr, nc;
int maxnum[81];

int count_commas(const char* str) {
  int cnt = 0;
  while (*str!='\n') {
    if (*str==',') ++cnt;
    ++str;
  }
  return cnt;
}

void solve()
{
  char buf[nr][nc+1];
  memset(buf, ' ', sizeof(buf));
  for (int j=0; j<nc; ++j) {
    for (int i=nr-maxnum[j]; i<nr; ++i)
      buf[i][j] = '+';
  }
  for (int i=0; i<nr; ++i)
    buf[i][nc] = '\n';
  fwrite(buf, sizeof(buf), 1, stdout);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  char buf[5*80];
  fgets(buf, sizeof(buf), stdin); //first line
  nc = count_commas(buf) + 1;
  nr = 0;
  //cerr << nc << ' ' <<buf << endl;
  char* ptr = buf;
  for (int j=0; j<nc; ++j) {
    maxnum[j] = (int)strtol(ptr, &ptr, 10);
    nr = max(nr, maxnum[j]);
    ++ptr;
  }
  for (int i=1; fgets(buf, sizeof(buf), stdin); ++i) {
    char* ptr = buf;
    for (int j=0; j<nc; ++j) {
      int val = (int)strtol(ptr, &ptr, 10);
      maxnum[j] = max(maxnum[j], val);
      nr = max(nr, val);
      ++ptr;
      //cerr << j << ' ' << maxnum[j] << ' ' << val << endl;;
    }
  }
  solve();
  return 0;
}
