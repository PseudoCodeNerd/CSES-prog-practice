// Introductory Problems
// https://cses.fi/problemset/task/1068/

#include <iostream>
// #include <list>
using namespace std;

typedef long long lolo;

int main(){
    lolo n;
    cin >> n;
    while (n != 1) {
        cout << n << " ";
        if (n%2) n = n*3+1;
        else n/=2;
    }
    cout << "1\n";
}
