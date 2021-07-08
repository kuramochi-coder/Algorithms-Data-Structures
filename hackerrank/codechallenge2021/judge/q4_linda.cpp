#include <bits/stdc++.h>
using namespace std;

typedef double D;

const int MAX_PTS = 1002;
struct Point {
  int x, y;
  bool operator==(const Point& rhs)
  {
    return x==rhs.x && y==rhs.y;
  }
  bool operator!=(const Point& rhs)
  {
    return !(*this==rhs);
  }
};

#include "convexhull.cpp" // convexHull function from rosetta code

Point pa, pb;
static int nh; //num of hull pts, output
static vector<Point> hullpts; //convex hull pts, output

static inline int distSq(Point p1, Point p2) {
    return (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y);
}
static D dist(Point p1, Point p2) {
  return hypot(p1.x-p2.x, p1.y-p2.y);
}
static D getdist(int& i, Point& pa, Point& pb) {
  D total = 0.0;
  while (hullpts[i]!=pa) {
    if (hullpts[i]==pb){
      swap(pa, pb);
      break;
    }
    total += dist(hullpts[i], hullpts[i+1]);
    ++i;
    assert(i<nh); //at least pa or pb will be part of combined hull
  }
  return total;
}
static D getdist(int& i, Point pb) {
  D total = 0.0;
  while (hullpts[i]!=pb) {
    total += dist(hullpts[i], hullpts[i+1]);
    ++i;
    if (i>=nh) return -1.0;
  }
  return total;
}
static D getdist(int i) { //dist from index i to index 0 of hull pts
  D total = 0.0;
  for (; i<nh; ++i) {
    total += dist(hullpts[i], hullpts[i+1]);
  }
  return total;
}

static D solve() {
    hullpts.push_back(hullpts[0]); //repeat first pt
    int i = 0;
    D dist0a = getdist(i, pa, pb); //dist from p0 to pa or pb, swap pa/pb if pb comes first
    D distab = getdist(i, pb);
    if (distab < 0.0) return dist(pa, pb); //pb not part of combined hull
    D distb0 = getdist(i);
    return min(distab, dist0a + distb0);
}
int main(void) {
  int np; //num of pts in polygon
  scanf("%d", &np);
  vector<Point> p(np+2); //polygon pts with 2 extra pts
  for (int i=0; i<np; ++i) {
    scanf("%d %d", &p[i].x, &p[i].y);
  }
  int m;
  scanf("%d", &m);
  for (int i=0; i<m; ++i) { //add point a and b
    scanf("%d %d", &pa.x, &pa.y);
    scanf("%d %d", &pb.x, &pb.y);
    assert(pa!=pb);
    p[np] = pa;
    p[np+1] = pb;
    hullpts = convexHull(p);
    nh = hullpts.size();
    printf("%.2lf\n", solve());
  }
  return 0;
}
