#include<iostream>
#include<vector>
#include<queue>
#define MAX_N 100
using namespace std;

queue<pair<int, int>>q;
int visited[MAX_N][MAX_N];

int map[MAX_N][MAX_N];
int n,m;

int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
vector<pair<int, int>> v;

int  cnt = 0;
int tmp = 0;

bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&& y < m;
}
void bfs(int x, int y) {

	map[x][y] = 2;
	q.push({ x,y });
	while (!q.empty()) {
		int cx=q.front().first;
		int cy = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (!is_range(nx, ny) || map[nx][ny]!=0)continue;
			q.push({ nx,ny });
			map[nx][ny] = 2;
		}
	}
}
void func() {
	while (1) {
		tmp = v.size();
		v.clear();
		int flag = -1;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				int f = false;
				if (map[i][j] == 1)
				{
					for (int k = 0; k < 4; k++)
					{
						int nx = i + dx[k];
						int ny = j + dy[k];
						if (map[nx][ny] == 2)
						{
							f = true;
							break;
						}
					}
					if (f == true)
					{
						v.push_back({ i,j });
					}
				}
			}
		}
		if (v.size() == 0)break;
		cnt++;
		for (int i = 0; i<v.size(); i++)
		{
			map[v[i].first][v[i].second] = 0;
		}

		for (int i = 0; i < v.size(); i++)
		{
			bfs(v[i].first, v[i].second);
		}
		

		
		
	}
	
}
int main()
{
	cin >> n>>m;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
		}
	}
	bfs(0,0);
	func();
	cout << cnt << "\n";
	cout << tmp << "\n";

	
}