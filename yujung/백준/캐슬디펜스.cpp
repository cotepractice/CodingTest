#include<iostream>
#include<vector>
#include<algorithm>
#define MAX_N 16
#define MAX_M 300
using namespace std;

//[r1-r2] | [c1-c2] 

//같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다.
vector<pair<int,int>> v;
vector<pair<int, int>> vv;
vector<pair<int,int>> zuck;
vector<pair<int, int>> save_zuck;
int n, m, d;
int map[MAX_N][MAX_N];
bool is_alive[MAX_M];
int ans = 0;
bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x < n&& y < m;
}
int distance(int x, int y, int x2, int y2)
{
	return abs(x - x2) + abs(y - y2);
}

bool cmp(pair<int, int> a, pair<int, int> b)
{
	return a.second < b.second;
}
bool all_die()
{
	for (int i = 0; i < zuck.size(); i++)
	{
		if (is_alive[i] == true)
		{
			return false;
		}
	}
	return true;
}


void down(vector<pair<int,int>> a)
{
	for (int i = 0; i < zuck.size(); i++)
	{
		if (is_alive[i] == false)continue;

		int cx = zuck[i].first;
		int cy = zuck[i].second;
		if (!is_range(cx+1, cy)) {
			is_alive[i] = false;
			continue;
		}
		zuck[i].first += 1;
	}

}
int func(vector<pair<int,int>> a)
{
	int sum = 0;
	while (1)
	{
		if (all_die())break;

		int cnt = 0;
		vector<int> tmp;
		for (int i = 0; i < a.size(); i++)
		{
			int r = a[i].first;
			int c = a[i].second;
			int max_v = 10000000;
			int max_idx = -1;
			for (int j = 0; j < zuck.size(); j++)
			{
				if (is_alive[j] == false)continue;
				int dist = distance(r, c, zuck[j].first, zuck[j].second);
				if (dist > d )continue;
				if (max_v > dist || (dist == max_v && zuck[j].second < zuck[max_idx].second))
				{
					max_v = dist;
					max_idx = j;
				}
			}
			if (max_v != 10000000)
			{
				tmp.push_back(max_idx);
			}
		}
		for (int i = 0; i < tmp.size(); i++)
		{
			if (is_alive[tmp[i]] == false)continue;
			is_alive[tmp[i]] = false;
			cnt++;
		}

		down(a);
		sum += cnt;
	}
	
	return sum;
	

}




void dfs(int idx, int cnt)
{
	if (3 == cnt)
	{
		zuck.clear();

		for (int i = 0; i < save_zuck.size(); i++)
		{
			zuck.push_back(save_zuck[i]);
		}
		for (int i = 0; i < MAX_M; i++)
		{
			is_alive[i] = true;
		}
		int t=func(vv);
		if (t > ans)
		{
			ans = t;
		}
		
	}

	for (int i = idx; i < v.size(); i++)
	{
		
		vv.push_back(v[i]);
		dfs(i + 1, cnt + 1);
		vv.pop_back();
	}
}

int main()
{
	//궁수를 배치한 이후의 게임 진행은 정해져 있다.
	cin >> n >> m >> d;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cin >> map[i][j];
			if (map[i][j] == 1)zuck.push_back({ i,j });
			if (map[i][j] == 1)save_zuck.push_back({ i,j });
		}
	}
	for (int i = 0; i < MAX_M; i++)
	{
		is_alive[i] = true;
	}
	for (int i = 0; i < m; i++)
	{
		v.push_back({ n,i });
	}

	dfs(0, 0);

	cout << ans;



}