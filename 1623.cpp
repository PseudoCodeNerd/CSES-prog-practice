// CSES Creating Strings (just use std::next_permutation)
// Template.cpp last updated 6/7/18
#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef long double ld;
typedef complex<ld> cd;

typedef pair<int, int> pi;
typedef pair<ll,ll> pl;
typedef pair<ld,ld> pd;

typedef vector<int> vi;
typedef vector<ld> vd;
typedef vector<ll> vl;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<cd> vcd;

template <class T> using Tree = tree<T, null_type, less<T>, rb_tree_tag,tree_order_statistics_node_update>;

#define FOR(i, a, b) for (int i=a; i<(b); i++)
#define F0R(i, a) for (int i=0; i<(a); i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)

#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound
#define all(x) x.begin(), x.end()
// change these numbers
const int MOD = 1000000007;
const ll INF = 1e18;
const int MX = 100001;

ll n, t, min_local, min_all;
vl p, x;

void solve(ll i){
	if(i==n){
		
	}
	p.pb(i)
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n;
	for(int i=0; i<n;++1){
		cin >> t;
		p.pb(t);
	}
	solve(0);
	cout << min_all;
    return 0;
}

// read the question correctly (ll vs int)
// template by bqi343 and iNum
// used by pseudocodenerd
// functions go before int main() silly

