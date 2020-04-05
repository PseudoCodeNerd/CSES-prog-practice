// Introductory Problems
// https://cses.fi/problemset/task/1083/

#include <iostream>
using namespace std;
typedef long long lolo;
int main(){
    int n, a;
    cin >> n;
    lolo sum = 0;
    for (int i = 0; i < n-1; i++) {
        cin >> a;
        sum += a;
    }
    cout << lolo(n) * (n+1)/2 - sum << endl;
}