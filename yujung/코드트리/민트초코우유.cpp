#include<iostream>
#include<vector>
#include<cstring>
#include<algorithm>
#define MAX_N 51
using namespace std;

int arr[MAX_N][MAX_N]; //종류
int map[MAX_N][MAX_N]; //신앙심
bool visited[MAX_N][MAX_N];
bool safe[MAX_N][MAX_N];
int n;

int dx[4] = { -1,1,0,0 }; //위, 아래 ,왼,오
int dy[4] = { 0,0,-1,1 };

int max_v = -1; //신앙심이 큰
int ccnt = 0; //주변 동료들의 개수
int mx = -1;
int my = -1;
bool visited2[MAX_N * MAX_N];

struct s
{

	int score;
	int x;
	int y;
};
struct s1
{
	int group;
	int score;
	int x;
	int y;
	int group_cnt; //주변 애들 개수
};
vector<pair<int,pair<int,int>>> tmp;
vector<s1> v; //실제 대표들이 들어감
bool cmp(s1 a, s1 b) {
	if (a.group != b.group) return a.group < b.group;
	 if (a.score != b.score) return a.score < b.score;
	if (a.x != b.x)return a.x < b.x;
	 return a.y < b.y;
}

bool cmp_s1(const s1& a, const s1& b) {
	if (a.score != b.score) return a.score < b.score;
	return a.group_cnt > b.group_cnt;
}
void visited_init()
{
	memset(visited, false, sizeof(visited));
}

bool is_range(int x, int y)
{
	return x >= 0 && y >= 0 && x<n && y < n;
}



//단일, 이중, 삼중
int group_check(int a)
{
	int cnt = 0;
	if (a & 1)cnt++;
	if (a & 2)cnt++;
	if (a & 4)cnt++;
	return cnt;
}

void dfs(int x, int y)
{
	ccnt++;
	visited[x][y] = true;
	tmp.push_back({ -map[x][y],{x,y} });
	for (int i = 0; i < 4; i++)
	{
		int nx=x + dx[i];
		int ny=y + dy[i];
		if(!is_range(nx,ny))continue;
		if (visited[nx][ny] == true)continue;
		if (arr[x][y] != arr[nx][ny])continue; //종료가 다르면 안됨
		dfs(nx, ny);
	}
}
void lunch()
{
	visited_init();
	v.clear();
	tmp.clear();
	v.clear();
;	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (visited[i][j])continue;
			
			ccnt = 0;
			tmp.clear();
			dfs(i, j);
			// 신앙심이 가장 높은 애가 들어감
			sort(tmp.begin(), tmp.end());
			v.push_back({ group_check(arr[i][j]),tmp[0].first- ccnt,tmp[0].second.first, tmp[0].second.second, ccnt });
		}
	}
	for (int i = 0; i < v.size(); i++)
	{
		int x = v[i].x;
		int y = v[i].y;
		map[x][y] += v[i].group_cnt;
	}
}
void evening()
{
	visited_init();
	sort(v.begin(), v.end(),cmp);

	for (int i = 0; i < v.size(); i++)
	{
		int x=v[i].x;
		int y = v[i].y;
		int score = map[x][y];
		int group = arr[x][y];
		int X = score - 1; //간절함
		int dir = score % 4;
		if (visited[x][y])continue; 
		int nx = x;
		int ny = y;
		while (1)
		{
			nx += dx[dir];
			ny += dy[dir];
			if (!is_range(nx, ny)) break;
			if (X == 0)break; //전파자는 전파할 방향으로 한칸씩 이동하면서 전파를 시도, 
			if (group == arr[nx][ny])continue; //전파 대상이랑 같으면 다음으로 진행
			else {
				int g_score = map[x][y]; //전파자의 신앙심
				
				if (X >map[nx][ny]) //강한 전파
				{
					map[x][y] -= map[nx][ny] + 1;
					X -= map[nx][ny] + 1; 
					map[nx][ny]++; //전파대상 증가
					arr[nx][ny] = arr[x][y]; //전파
					visited[nx][ny] = true;
				}
				else
				{
					map[x][y] = 1; 
					map[nx][ny] += X; //신앙심 증가
					X = 0; //간절함 0이 됨
					arr[nx][ny] |= arr[x][y]; //모두 신봉
					visited[nx][ny] = true;
				}
			}
		}
		map[x][y] = 1;

	}
}
void print_v()
{
	int tcm=0;
	int tc=0; //민초
	int tm=0; //민트 우유
	int  cm=0; //초코 우유
	int m=0; //우유
	int c=0; //초코
	int t=0; //민트
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (arr[i][j] == 7) tcm+=map[i][j];
			
			if (arr[i][j] == 6)tc+=map[i][j];
			
			if (arr[i][j] == 5)tm+=map[i][j];
			if (arr[i][j] == 4) t += map[i][j];
			if (arr[i][j] == 3)cm += map[i][j];
			if (arr[i][j]==2)c += map[i][j];
			if (arr[i][j] == 1) m += map[i][j];
		}
	}
	cout << tcm << " " << tc << " " << tm << " " << cm << " " << m << " " << c << " " << t << "\n";
}

int main()
{
	int t;
	
	cin >> n>>t;
	for (int i = 0; i < n; i++)
	{
		
			string c;
			cin >> c;
			for (int j = 0; j < n; j++)
			{
				if (c[j] == 'T')
				{
					arr[i][j] = 4;
				}
				if (c[j] == 'C')
				{
					arr[i][j] = 2;
				}
				if (c[j] == 'M')
				{
					arr[i][j] = 1;
				}
			}
		
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cin >> map[i][j];  // 신앙심 -> 변동 되니까 관리해야 함
		}
	}

	while (t--)
	{
		lunch();
		evening();
		print_v();
	}

}