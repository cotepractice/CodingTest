#include<iostream>
#include<vector>
#define MAX_N 25
using namespace std;
int N, M;
int T;
vector<pair<int, int>> v;
vector<int> tmp;
int cnt = 0;
bool visited[MAX_N];
int con[MAX_N][MAX_N];

bool check(int idx, vector<int> t) {
	for (int i = 0; i < t.size();i++) {
		if (con[idx][t[i]] == 1)return false;
	}
	return true;
}
void dfs(int idx) {
	cnt++;
		for (int i = idx; i <= N; i++)
		{
		
			if (!check(i, tmp))continue;
			tmp.push_back(i);
			dfs(i + 1 );
			tmp.pop_back();
		}
}
int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 25; i++) {
			for (int j = 0; j < 25; j++) {
				con[i][j] = 0;
			}
		}
		cnt = 0;
		cin >> N >> M;
		for (int i = 0; i < M; i++) {
			int a, b;
			cin >> a >> b;

			con[a][b] = 1;
			con[b][a] = 1;
		}
		dfs(1);
		cout <<"#"<<t<<" "<< cnt<<"\n";
	}
	

}