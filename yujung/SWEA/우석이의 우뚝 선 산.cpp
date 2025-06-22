#include<iostream>
#include<cstring>
#define MAX 50010
typedef long long ll;
using namespace std;

int n;
int map[MAX];
ll answer;
int T;
void solution()
{
	int in = 0;
	int de = 0;
	for (int i = 0; i < n - 1; i++)
	{
		int prev = map[i];
		int next = map[i + 1];
		if (prev < next)
		{
			if (de == 0)
			{
				in++;
			}
			else {
				answer = answer + in * de;
				de = 0;
				in = 1;
			}

		}
		else
		{
			if (in != 0)
			{
				de++;
			}

			
		}
	}
	answer = answer + in * de;
}


int main()
{
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> n;
		memset(map, 0, sizeof(map));
		answer = 0;
		for (int i = 0; i < n; i++)cin >> map[i];
		solution();
		cout << "#" << t << " " << answer << "\n";
	}

}