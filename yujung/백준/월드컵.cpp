#include<iostream>
using namespace std;

int map[4][18];
int ans[4];
int main() {
	int a;
	for (int i = 0; i < 4; i++) {
		ans[i] = true;
	}
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 18; j++)
		{
			
				cin >> map[i][j];
			
		}
		int a=0;
		int b = 0;
		for (int j = 0; j < 18; j += 3) {
			a += map[i][j];
		}
		for (int j = 2; j < 18; j += 3) {
			b += map[i][j];
		}
		
		if(a!=b) {
			ans[i] = false;
		}

		
			int sum = 0;
			for (int j = 0; j < 18; j+=3)
			{
				sum = 0;
				sum += map[i][j];
				sum += map[i][j + 1];
				sum += map[i][j + 2];
				if (sum != 5) {
					ans[i] = false;
					break;
				}
			}
			
		
		
		int start = 1;
		int end = 4;

		while (end <= 16)
		{
			if (map[i][start] > map[i][end])
			{
				map[i][start] = map[i][start] - map[i][end];
				map[i][end] = 0;
				if (end <= 16)
				{
					end += 3;
				}
			}
			else if(map[i][start]<map[i][end])
			{
				start = end;
				end += 3;
			}
			else
			{
				map[i][start] = 0;
				map[i][end] = 0;
				start = end + 3;
				end = start + 3;
			}

		}

		for (int j = 1; j <= 18; j += 3)
		{
			if (map[i][j] > 0) {
				ans[i] = false;
			}
		}
	}
	for (int i = 0; i < 4; i++)
	{
		cout << ans[i] << " ";

	}


}