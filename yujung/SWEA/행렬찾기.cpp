#include<iostream>
#include<queue>
#include<algorithm>
#include<climits>
#include<vector>
#include<cstring>
#define MAX_N 101
using namespace std;

bool visited[MAX_N][MAX_N];
int map[MAX_N][MAX_N];
int n;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };

pair<int, int> max_v;
pair<int, int> min_v;

int cnt = 0;
int T;
void init()
{
	max_v = { -1,-1 };
	min_v = { INT_MAX, INT_MAX };
}
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&& y < n;
}


vector<pair<int,pair<int,int>>> v;



void bfs(int x, int y)
{
	queue < pair<int, int>> q;
	q.push({ x, y });
	visited[x][y] = true;

	while (!q.empty())
	{
		int cx=q.front().first;
		int cy = q.front().second;
		q.pop();

		max_v.first = max(max_v.first, cx); // 최대 행 찾기
		min_v.first = min(min_v.first, cx); //최소 행 찾기
		max_v.second = max(max_v.second, cy); //최대 열 찾기
		min_v.second = min(min_v.second, cy); //최소 열 찾기
		for (int i = 0; i < 4; i++)
		{
			int nx = cx + dx[i];
			int ny = cy + dy[i];
			if (!is_range(nx, ny))continue;
			if (visited[nx][ny])continue;
			if (map[nx][ny] == 0)continue; // 0이 아닌 것들만 찾기
			
			visited[nx][ny] = true;
			q.push({ nx, ny });

		}
	}

}

void solution()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (!map[i][j])continue;
			if (visited[i][j]) continue;
			init();
			bfs(i, j);
			int r = abs(max_v.first - min_v.first)+1;
			int c = abs(max_v.second - min_v.second)+1;
			v.push_back({ r * c,{r,c} });
			cnt++;
		}
	}
	sort(v.begin(), v.end());


}

void print_v(int t)
{
	cout << "#"<<t<<" "<<cnt << " ";
	for(int i = 0; i < v.size(); i++)
	{
		cout << v[i].second.first << " " << v[i].second.second<<" ";
	}
	cout << endl;
}
int main()
{
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cnt = 0;
		v.clear();
		memset(visited, 0, sizeof(visited));
		cin >> n;

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cin >> map[i][j];
			}
		}

		solution();
		print_v(t);
	}

	
	
}
