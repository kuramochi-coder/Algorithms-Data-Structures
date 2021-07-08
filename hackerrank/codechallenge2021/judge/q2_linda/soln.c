#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int nr, nc;
int maxnum[81];

int max(int num1, int num2) {
  return (num1 > num2 ) ? num1 : num2;
}

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
  char buf[5*80];
  fgets(buf, sizeof(buf), stdin); //first line
  nc = count_commas(buf) + 1;
  nr = 0;
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
    }
  }
  solve();
  return 0;
}
