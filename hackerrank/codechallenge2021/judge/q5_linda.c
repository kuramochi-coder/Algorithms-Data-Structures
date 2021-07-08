#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef long long i64;

struct Data {
  double sortval;
  int score;
  int ptype;
};

i64 max(i64 num1, i64 num2) {
  return (num1 > num2 ) ? num1 : num2;
}
i64 min(i64 num1, i64 num2) {
  return (num1 < num2 ) ? num1 : num2;
}

i64 max_ptype_0_or_2(const struct Data* arrdata, int startix, int endix) {
  int ans = -1;
  for (int i = startix; i < endix; ++i) {
    if (arrdata[i].ptype != 1) {
      ans = max(ans, arrdata[i].score);  
    }
  }
  return (i64)ans;
}

i64 min_ptype_0_or_1(const struct Data* arrdata, int startix, int endix) {
  int ans = 20000000;
  for (int i = startix; i < endix; ++i) {
    if (arrdata[i].ptype != 2) {
      ans = min(ans, arrdata[i].score);  
    }
  }
  return (i64)ans;
}

i64 sum_score(const struct Data* arrdata, int startix, int endix) {
  i64 total = 0;
  for (int i = startix; i < endix; ++i) {
    total += (i64)arrdata[i].score;
  }
  return total;
}

struct Line {
  char name[24];
  int score;
};
int cmpline(const void* a, const void* b) {
  const struct Line* ia = (const struct Line*)a;
  const struct Line* ib = (const struct Line*)b;
  return strcmp((*ia).name, (*ib).name);
}
int cmpdata_sortval(const void* a, const void* b) {
  if ((*(struct Data*)a).sortval < (*(struct Data*)b).sortval) return -1;
  else if ((*(struct Data*)a).sortval > (*(struct Data*)b).sortval) return 1;
  return 0;
}

struct Data data[250000];
void add_data(int i, double sortval, int score, int ptype) {
  data[i] = (struct Data){sortval, score, ptype};
}

int main() {
  int n, m;
  scanf("%d %d\n", &n, &m);
  struct Line line[n];
  for (int i = 0; i < n; ++i) {
    scanf("%s %d\n", line[i].name, &(line[i].score));
  }
  qsort(line, n, sizeof(struct Line), cmpline);
  for (int i = 0; i < n; ++i) {
    int score = line[i].score;
    char lastchar = line[i].name[strlen(line[i].name)-1];
    if (lastchar == '1') {
      int partner_score = data[i-1].score;
      if (partner_score <= score) {
	add_data(i, score*2.0, score, 0);
      } else {
     	double sortval = (double)(score + partner_score) + (score*1e-7) + (i*1e-8);
	data[i-1].sortval = sortval; //update sortval of partner
        data[i-1].ptype = 1; //update ptype of partner
    	add_data(i, sortval+2e-9, score, 2);
      }
    } else {
      add_data(i, score*2.0, score, 0);
    }
  }

  i64 answer;
  if (m == 1) {
    answer = min_ptype_0_or_1(data, 0, n);
  } else if (m == n) {
    answer = sum_score(data, 0, n);
  } else {
    qsort(data, n, sizeof(struct Data), cmpdata_sortval);
    answer = sum_score(data, 0, m);
    if (data[m-1].ptype == 1) {
      i64 answer1 = answer - (i64)data[m-1].score + min_ptype_0_or_1(data, m-1, n);
      i64 answer2 = answer + (i64)data[m].score - max_ptype_0_or_2(data, 0, m-1);
      answer = min(answer1, answer2);
    }
  }
  printf("%lld\n", answer);
}
