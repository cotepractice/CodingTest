#include<iostream>
#include<vector>
#include<climits>
#include<algorithm>
using namespace std;

vector<int> v;
int ans = INT_MAX;

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int a;
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	int s = 0;
	int e = n - 1;
	int s_v = v[0];
	int e_v = v[n - 1];
	while (s < e)
	{
		int tmp = abs(v[s] + v[e]);
		if (ans > tmp)
		{
			ans = tmp;
			s_v = v[s];
			e_v = v[e];
			if (tmp == 0) {
				break;
			}
		}
		if (v[s] + v[e] > 0) {
			e--;
		}
		else {
			s++;
		}
	}
	cout << s_v << " " << e_v;

}