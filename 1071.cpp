// Introductory Problems
// https://cses.fi/problemset/task/1071/

#include <iostream>
using namespace std;
typedef long long ll;

int main() {
  int t, r, c;
  cin >> t;
  while (t--) {
    cin >> r >> c;
    int a = max(r, c);
    int b = min(r, c);
    ll s = ll(a - 1) * (a - 1);
    if (a == b) s += a;
    else if (a % 2) {
      if (c == a) s+= a * 2 - r;
      else s += c;
    } else {
      if (r == a) s += a * 2 - c;
      else s += r;
    }
    cout << s << endl;
  }
}
