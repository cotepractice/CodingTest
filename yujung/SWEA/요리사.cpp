#include<iostream>
#include<vector>
#include<climits>
using namespace std;
#define MAX_N 16
int res = INT_MAX;
int map[MAX_N][MAX_N];
int n;
int visited[MAX_N];
int T;
int dfs2(vector<int> a) {
	int ans = 0;
	for (int i = 0; i < a.size(); i++) {
		for (int j = 0; j < a.size(); j++)
		{
			if (i == j)continue;
			ans += map[a[i]][a[j]];
		}
	}
	return ans;
}
int func(vector<int> a, vector<int> b)
{
	return abs(dfs2(a) - dfs2(b));
}
void dfs( int idx,int cnt) {
	if (cnt == n/2)
	{
		vector<int> a;
		vector<int> b;
		for (int i = 0; i < n; i++) {
			if (visited[i] == true) {
				a.push_back(i);
			}
			else {
				b.push_back(i);
			}
		}
		int r=func(a, b);
		if (r < res) {
			res = r;
		}
		return;
	}
	for (int i = idx; i < n; i++) {
		if (visited[i] == true)continue;
		visited[i] = true;
		dfs( i+1,cnt + 1);
		visited[i] = false;
	}
}

int main()
{
	cin >> T;
	for (int t = 1; t <= T; t++) {
		res = INT_MAX;
		cin >> n;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> map[i][j];
			}
		}
		dfs(0, 0);
		cout <<"#"<<t<<" "<< res<<"\n";
	}
	

}