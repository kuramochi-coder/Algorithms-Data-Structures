#include <stdio.h>
#include <math.h>

int main() {
  int n;
  scanf("%d", &n);
  int num;
  double rate = 0.0;
  for (int i=0; i<n; ++i) {
    scanf("%d", &num);
    rate += 1.0/num;
  }
  printf("%d\n", (int)round(60.0/rate));
  return 0;
}
