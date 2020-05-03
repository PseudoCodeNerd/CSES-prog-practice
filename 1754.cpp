// Introductory Problems : Coin Tiles
// https://cses.fi/problemset/task/1754/

#include <iostream>
using namespace std;
typedef long long ll;


int main() {
	ll t, a, b;
	cin >> t;
	for (int i=0;i<t;i++){
		cin >> a >> b;
		if (2*a-b>=0 && (2*a-b)%3==0 && 2*b-a>=0 && (2*b-a)%3==0){
			cout << "YES\n";
		} else {
			cout << "NO\n";
		}
	}
}
