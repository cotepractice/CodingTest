#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

#define MAX_N 13

int map[MAX_N][MAX_N];
int n;
int res = 0;
vector<pair<int, int>> v;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int min_l = 987654321;
int max_core = -1;
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&& y < n;
}

void dfs(int cnt, int l, int core){ 
	if (cnt == v.size())
	{
		if (max_core < core) {
			max_core = core;
			min_l = l;
		}
		else if (max_core == core) {
			min_l = min(l, min_l);
		}
		return;
	}
	int x=v[cnt].first;
	int y = v[cnt].second;

	for (int i = 0; i < 4; i++) {
		int nx = x;
		int ny = y;
		int c = 0; //길이 
		while (1) {
			nx+=  dx[i];
			ny+= dy[i];

			if (!is_range(nx, ny))break;
			if (map[nx][ny]==1||map[nx][ny]==2)
			{
				c = 0;
				break;
			}
			c++;
		}
		if (c > 0 ) //c가 0보다 크면 
		{
			nx = v[cnt].first;
			ny = v[cnt].second;
			while (1) {

				nx += dx[i];
				ny += dy[i];

				if (!is_range(nx, ny))break;
				map[nx][ny] = 2;
			}
			dfs(cnt + 1, l + c, core+ 1);
			nx = v[cnt].first;
			ny = v[cnt].second;
			while (1)
			{
				nx += dx[i];
				ny += dy[i];
				if (!is_range(nx, ny))
				{
					break;
				}
				map[nx][ny] = 0;
			}
		}
	}

	dfs(cnt + 1, l, core);
}
int main() 
{
	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		v.clear();
		 min_l = 987654321;
		 max_core = -1;
		cin >> n;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> map[i][j];
				if (i == 0 || j == 0 || i == n - 1 || j == n - 1)
				{
					res++;
				}
				else if (map[i][j] == 1) {
					v.push_back({ i,j });
				}
			}
		}

		dfs(0, 0, 0);

		cout <<"#" << t<<" "<< min_l<<"\n";

	}
	

}