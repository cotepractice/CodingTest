#include <iostream>
using namespace std;

#define MAX_N 51

int N, K;
int map[MAX_N][MAX_N];
bool visited[MAX_N][MAX_N];
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
int ans = 0;

bool is_range(int x, int y) {
	return x >= 0 && y >= 0 && x < N&& y < N;
}

void dfs(int x, int y, int cnt, int res) {
	ans = max(ans, res);  // 현재 길이로 갱신

	for (int i = 0; i < 4; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (!is_range(nx, ny) || visited[nx][ny]) continue;

		if (map[nx][ny] < map[x][y]) {
			visited[nx][ny] = true;
			dfs(nx, ny, cnt, res + 1);
			visited[nx][ny] = false;
		}
		else if (cnt == 0) {
			for (int cut = 1; cut <= K; cut++) {
				if (map[nx][ny] - cut < map[x][y]) {
					map[nx][ny] -= cut;
					visited[nx][ny] = true;
					dfs(nx, ny, 1, res + 1);
					visited[nx][ny] = false;
					map[nx][ny] += cut;  // 복구
				}
			}
		}
	}
}

int find_max() {
	int maxv = -1;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			maxv = max(maxv, map[i][j]);
	return maxv;
}

void solution() {
	int max_v = find_max();

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] == max_v) {
				visited[i][j] = true;
				dfs(i, j, 0, 1);  // 경로 길이 1부터 시작
				visited[i][j] = false;
			}
		}
	}
}

int main() {
	cin >> N >> K;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> map[i][j];

	solution();
	cout << ans << "\n";
	return 0;
}
