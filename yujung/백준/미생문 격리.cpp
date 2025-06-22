#include<iostream>
#include<cstring>
#include<vector>
#define MAX_N 101
using namespace std;

/**
함수내에 큰 배열 쓰는 거 주의 시간 초과 남
stack을 호출하기 때문에 전역 배열 사용하는 것이 좋음
**/
struct s
{
	int x, y, v, d;
};
vector<s> tmp[MAX_N][MAX_N];
int n, m, k;
s map[MAX_N][MAX_N];
//1 2  , 2 1  3 4 , 4 3
// 1+3/4     
int dx[5] = { 0,-1,1,0,0 }; //상, 하, 좌, 우
int dy[5] = { 0,0,0,-1,1 };
int T;

int move_dir(int d)
{
	if (d == 1)
	{
		return 2;
	}
	if (d == 2)
	{
		return 1;
	}
	if (d == 3)
	{
		return 4;
	}
	if (d == 4)
	{
		return 3;
	}
}
bool is_border(int x, int y)
{
	return x == 0 || x == n - 1 || y == 0 || y == n - 1;
}

void init()
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			tmp[i][j].clear();
		}
	}
}


vector<s> v;

void func(int m)
{
	while (m--)
	{
		init();
		vector<s> tmp_pos;
		for (int i = 0; i < v.size(); i++)
		{
			int cx = v[i].x;
			int cy = v[i].y;
			int hp = v[i].v;
			int d = v[i].d;

			int nx = cx + dx[d];
			int ny = cy + dy[d];
			if (is_border(nx, ny))
			{
				d = move_dir(d);
				hp /= 2;
			}
			if (hp != 0)
			{
				tmp[nx][ny].push_back({ nx,ny,hp,d });
			}

		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (tmp[i][j].size() > 1)
				{
					int sum = 0;
					int max_v = -1;
					int max_idx = -1;
					for (int k = 0; k < tmp[i][j].size(); k++)
					{
						sum += tmp[i][j][k].v; //sum값이 더 커짐
						if (max_v < tmp[i][j][k].v)
						{
							max_v = tmp[i][j][k].v;
							max_idx = k;
						}
					}

					if (sum != 0)
					{
						tmp_pos.push_back({ i,j,sum ,tmp[i][j][max_idx].d });
					}


				}
				else if (tmp[i][j].size() == 1)
				{
					tmp_pos.push_back({ i,j,tmp[i][j][0].v,tmp[i][j][0].d });
				}
			}
		}
		v = tmp_pos;

	}
}
int main()
{
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> n >> m >> k;
		v.clear();
		for (int i = 0; i < k; i++)
		{
			int a, b, c, d;
			cin >> a >> b >> c >> d;
			v.push_back({ a,b,c,d });
		}
		func(m);
		int ans = 0;

		for (int i = 0; i < v.size(); i++)
		{
			ans += v[i].v;
		}

		cout << "#" << t << " " << ans << "\n";
	}


}