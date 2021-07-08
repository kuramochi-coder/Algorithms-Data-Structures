#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  assert(n>=1 && n<=10);
  int num;
  double rate = 0.0;
  for (int i=0; i<n; ++i) {
    cin >> num;
    assert(num>=1 && num<=100);
    rate += 1.0/num;
  }
  assert(scanf("%d", &num)<=0);
  printf("%d\n", (int)round(60.0/rate));
  return 0;
}
