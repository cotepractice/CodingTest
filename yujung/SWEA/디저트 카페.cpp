#include<iostream>
#include<vector>
#include<map>
#define MAX_N 21
using namespace std;

int arr[MAX_N][MAX_N];
int N;
vector<pair<int, int>> v;
int ans=-1;
vector<int> tmp;
vector<int> t;
int dx[4] = { 1,1,-1,-1 };
int dy[4] = { 1,-1,-1,1 };
int T;

int visited[101];
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < N&& y < N;
}
void dfs(int cnt) {
	for (int i = 2; i < N; ++i) {
		for (int j = 2; j < N; ++j) {
			v.push_back({ i, j });
		}
	}
}

bool rect(int x, int y, int n, int m) {
	t.clear();
	map<int, int> A;
	
	memset(visited, 0, sizeof(visited));
		int nx = x;
		int ny = y;
		for (int j = 0; j < n-1; j++)
		{
			nx += dx[0];
			ny += dy[0];

			if (!is_range(nx, ny)||visited[arr[nx][ny]]>=1) {
				return false;
			}
			visited[arr[nx][ny]]++;
			t.push_back(arr[nx][ny]);
		}
		for (int j = 0; j < m-1; j++)
		{
			nx += dx[1];
			ny += dy[1];

			if (!is_range(nx, ny) || visited[arr[nx][ny]] >= 1) {
				return false;
			}
			visited[arr[nx][ny]]++;
			t.push_back(arr[nx][ny]);

		}
		for (int j = 0; j < n-1; j++)
		{
			nx += dx[2];
			ny += dy[2];

			if (!is_range(nx, ny) || visited[arr[nx][ny]] >= 1) {
				return false;
			}
			visited[arr[nx][ny]]++;
			t.push_back(arr[nx][ny]);

		}
		for (int j = 0; j < m-1; j++)
		{
			nx += dx[3];
			ny += dy[3];

			if (!is_range(nx, ny) || visited[arr[nx][ny]] >= 1) {
				return false;
			}
			visited[arr[nx][ny]]++;
			t.push_back(arr[nx][ny]);
		}
	
	return true;
}

void solution() {

	for (int k = 0; k < v.size(); k++)
	{
		int n=v[k].first;
		int m = v[k].second;
		
		for (int i = 0; i <= N - n - m + 1; i++)
		{
			for (int j = m-1; j <= N - n; j++)
			{
				if (rect(i, j, v[k].first, v[k].second) == true)
				{
					int c = t.size();
					if (ans < c) {
						ans = t.size();
					}
				}
			}
		}
		

	}
	
}
int main() 
{
	cin >> T;
	for (int ti = 1; ti <= T; ti++)
	{
		ans = -1;
		cin >> N;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> arr[i][j];
			}
		}
		v.clear();
		dfs(0);

		solution();
		cout <<"#"<<ti<<" "<< ans<<"\n";
	}
}

