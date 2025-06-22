#include <algorithm>
#include <iostream>
#include <utility>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

// 상수 정의
const int INF = 1e9 + 10;    // 무한대를 나타내는 상수
const int MAX_N = 60;         // 최대 그리드 크기 (50 + 10)
const int MAX_M = 310;        // 최대 전사 수 (300 + 10)

// 전역 변수 선언
int obstacleGrid[MAX_N][MAX_N];    // 장애물 그리드 (1: 장애물, 0: 자유로운 공간)
int distanceGrid[MAX_N][MAX_N];    // 각 셀에서 종료 지점까지의 거리
pii warriorPositions[MAX_M];        // 전사들의 현재 위치
int sightMap[MAX_N][MAX_N];        // 현재 시야 상태 (1: 시야 내, 0: 시야 외)
int warriorCountGrid[MAX_N][MAX_N]; // 각 셀에 있는 전사의 수

// 방향 배열: 위, 아래, 왼쪽, 오른쪽
const int DX[4] = { -1, 1, 0, 0 };
const int DY[4] = { 0, 0, -1, 1 };

/**
 * @brief 두 점 사이의 맨해튼 거리를 계산하는 함수
 *
 * @param a 첫 번째 점의 좌표 (x, y)
 * @param b 두 번째 점의 좌표 (x, y)
 * @return int 맨해튼 거리
 */
inline int calculateManhattanDistance(const pii& a, const pii& b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

/**
 * @brief BFS를 이용하여 종료 지점(startX, startY)에서 모든 도달 가능한 셀까지의 최단 거리를 계산하는 함수
 *
 * @param startX 시작 지점의 x 좌표 (종료 지점)
 * @param startY 시작 지점의 y 좌표 (종료 지점)
 * @param N 그리드의 크기 (N x N)
 */
void computeDistances(int startX, int startY, int N) {
    // 거리 그리드를 초기화: 장애물이 있는 셀은 INF, 그렇지 않으면 -1로 설정
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            distanceGrid[i][j] = obstacleGrid[i][j] ? INF : -1;
        }
    }

    queue<pii> q;               // BFS를 위한 큐
    q.push({ startX, startY });   // 시작 지점을 큐에 추가
    distanceGrid[startX][startY] = 0;  // 시작 지점의 거리는 0

    // BFS 알고리즘 실행
    while (!q.empty()) {
        int currentX = q.front().first;
        int currentY = q.front().second;
        q.pop();

        // 네 방향으로 이동
        for (int dir = 0; dir < 4; dir++) {
            int nextX = currentX + DX[dir];
            int nextY = currentY + DY[dir];

            // 그리드 경계를 벗어나는지 확인
            if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N)
                continue;
            // 이미 방문했거나 장애물이 있는지 확인
            if (distanceGrid[nextX][nextY] != -1)
                continue;

            // 다음 셀의 거리 업데이트 및 큐에 추가
            distanceGrid[nextX][nextY] = distanceGrid[currentX][currentY] + 1;
            q.push({ nextX, nextY });
        }
    }
}

// 시야 방향에 따른 함수 선언 (위, 아래, 왼쪽, 오른쪽)
int sightUp(int x, int y, int N, bool isTest);
int sightDown(int x, int y, int N, bool isTest);
int sightLeft(int x, int y, int N, bool isTest);
int sightRight(int x, int y, int N, bool isTest);

/**
 * @brief 최적의 시야 방향을 선택하여 시야를 설정하는 함수
 *
 * @param x 현재 플레이어의 x 좌표
 * @param y 현재 플레이어의 y 좌표
 * @param N 그리드의 크기
 * @return int 최대 커버리지 (시야로 커버된 전사의 수)
 */
int chooseBestSight(int x, int y, int N) {
    // 시야 맵을 초기화 (모든 셀을 시야 외로 설정)
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            sightMap[i][j] = 0;

    int maxCoverage = -1;    // 최대 커버리지를 저장할 변수
    int bestDirection = -1;   // 최적의 시야 방향 (0: 위, 1: 아래, 2: 왼쪽, 3: 오른쪽)

    // 시야 방향별 함수 포인터 배열
    typedef int (*SightFunc)(int, int, int, bool);
    SightFunc sightFunctions[4] = { sightUp, sightDown, sightLeft, sightRight };

    // 모든 시야 방향을 테스트하여 최대 커버리지를 찾음
    for (int dir = 0; dir < 4; dir++) {
        // 테스트를 위해 시야 맵을 초기화
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                sightMap[i][j] = 0;

        // 현재 방향으로 시야 설정하고 커버리지 계산
        int coverage = sightFunctions[dir](x, y, N, true);
        if (maxCoverage < coverage) {
            maxCoverage = coverage;
            bestDirection = dir;
        }
    }

    // 최적의 방향으로 실제 시야 설정
    sightFunctions[bestDirection](x, y, N, false);

    return maxCoverage;
}

/**
 * @brief 위쪽 방향으로 시야를 설정하는 함수
 *
 * @param x 현재 플레이어의 x 좌표
 * @param y 현재 플레이어의 y 좌표
 * @param N 그리드의 크기
 * @param isTest 테스트 모드 여부 (true: 테스트, false: 실제 적용)
 * @return int 시야로 커버된 전사의 수
 */
int sightUp(int x, int y, int N, bool isTest) {
    // 다이아몬드 형태로 위쪽 셀을 시야에 포함시킴
    for (int i = x - 1; i >= 0; i--) {
        int left = max(0, y - (x - i));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (x - i));      // 오른쪽 경계 계산
        for (int j = left; j <= right; j++) {
            sightMap[i][j] = 1;                   // 시야 설정
        }
    }

    // 장애물 처리: 시야 막힘 여부 확인
    bool obstructionFound = false;
    for (int i = x - 1; i >= 0; i--) {
        if (obstructionFound) {
            sightMap[i][y] = 0;                   // 장애물이 발견된 후에는 시야 제거
        }
        else {
            sightMap[i][y] = 1;                   // 장애물이 발견되지 않으면 시야 유지
        }

        if (warriorCountGrid[i][y]) {             // 전사가 있는 경우 장애물로 간주
            obstructionFound = true;
        }
    }

    // 장애물에 따라 시야 조정
    for (int i = x - 1; i >= 1; i--) {
        int left = max(0, y - (x - i));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (x - i));      // 오른쪽 경계 계산

        // 왼쪽 측면 조정
        for (int j = left; j < y; j++) {
            if ((!sightMap[i][j]) || warriorCountGrid[i][j]) {
                if (j > 0) sightMap[i - 1][j - 1] = 0; // 왼쪽 위 셀의 시야 제거
                sightMap[i - 1][j] = 0;            // 바로 위 셀의 시야 제거
            }
        }

        // 오른쪽 측면 조정
        for (int j = y + 1; j <= right; j++) {
            if ((!sightMap[i][j]) || warriorCountGrid[i][j]) {
                if (j + 1 < N) sightMap[i - 1][j + 1] = 0; // 오른쪽 위 셀의 시야 제거
                sightMap[i - 1][j] = 0;                // 바로 위 셀의 시야 제거
            }
        }
    }

    // 시야로 커버된 전사 수 계산
    int coverage = 0;
    for (int i = x - 1; i >= 0; i--) {
        int left = max(0, y - (x - i));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (x - i));      // 오른쪽 경계 계산
        for (int j = left; j <= right; j++) {
            if (sightMap[i][j]) {
                coverage += warriorCountGrid[i][j]; // 시야 내에 있는 전사의 수를 더함
            }
        }
    }

    // 테스트 모드인 경우 시야 맵을 원래대로 되돌림
    if (isTest) {
        for (int i = x - 1; i >= 0; i--) {
            int left = max(0, y - (x - i));
            int right = min(N - 1, y + (x - i));
            for (int j = left; j <= right; j++) {
                sightMap[i][j] = 0;                   // 시야 제거
            }
        }
    }

    return coverage;    // 커버리지 반환
}

/**
 * @brief 아래쪽 방향으로 시야를 설정하는 함수 (sightUp과 유사)
 *
 * @param x 현재 플레이어의 x 좌표
 * @param y 현재 플레이어의 y 좌표
 * @param N 그리드의 크기
 * @param isTest 테스트 모드 여부 (true: 테스트, false: 실제 적용)
 * @return int 시야로 커버된 전사의 수
 */
int sightDown(int x, int y, int N, bool isTest) {
    // 다이아몬드 형태로 아래쪽 셀을 시야에 포함시킴
    for (int i = x + 1; i < N; i++) {
        int left = max(0, y - (i - x));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (i - x));      // 오른쪽 경계 계산
        for (int j = left; j <= right; j++) {
            sightMap[i][j] = 1;                   // 시야 설정
        }
    }

    // 장애물 처리: 시야 막힘 여부 확인
    bool obstructionFound = false;
    for (int i = x + 1; i < N; i++) {
        if (obstructionFound) {
            sightMap[i][y] = 0;                   // 장애물이 발견된 후에는 시야 제거
        }
        else {
            sightMap[i][y] = 1;                   // 장애물이 발견되지 않으면 시야 유지
        }

        if (warriorCountGrid[i][y]) {             // 전사가 있는 경우 장애물로 간주
            obstructionFound = true;
        }
    }

    // 장애물에 따라 시야 조정
    for (int i = x + 1; i < N - 1; i++) {
        int left = max(0, y - (i - x));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (i - x));      // 오른쪽 경계 계산

        // 왼쪽 측면 조정
        for (int j = left; j < y; j++) {
            if ((!sightMap[i][j]) || warriorCountGrid[i][j]) {
                if (j > 0) sightMap[i + 1][j - 1] = 0; // 왼쪽 아래 셀의 시야 제거
                sightMap[i + 1][j] = 0;            // 바로 아래 셀의 시야 제거
            }
        }

        // 오른쪽 측면 조정
        for (int j = y + 1; j <= right; j++) {
            if ((!sightMap[i][j]) || warriorCountGrid[i][j]) {
                if (j + 1 < N) sightMap[i + 1][j + 1] = 0; // 오른쪽 아래 셀의 시야 제거
                sightMap[i + 1][j] = 0;                // 바로 아래 셀의 시야 제거
            }
        }
    }

    // 시야로 커버된 전사 수 계산
    int coverage = 0;
    for (int i = x + 1; i < N; i++) {
        int left = max(0, y - (i - x));           // 왼쪽 경계 계산
        int right = min(N - 1, y + (i - x));      // 오른쪽 경계 계산
        for (int j = left; j <= right; j++) {
            if (sightMap[i][j]) {
                coverage += warriorCountGrid[i][j]; // 시야 내에 있는 전사의 수를 더함
            }
        }
    }

    // 테스트 모드인 경우 시야 맵을 원래대로 되돌림
    if (isTest) {
        for (int i = x + 1; i < N; i++) {
            int left = max(0, y - (i - x));
            int right = min(N - 1, y + (i - x));
            for (int j = left; j <= right; j++) {
                sightMap[i][j] = 0;                   // 시야 제거
            }
        }
    }

    return coverage;    // 커버리지 반환
}

/**
 * @brief 왼쪽 방향으로 시야를 설정하는 함수 (sightUp과 유사)
 *
 * @param x 현재 플레이어의 x 좌표
 * @param y 현재 플레이어의 y 좌표
 * @param N 그리드의 크기
 * @param isTest 테스트 모드 여부 (true: 테스트, false: 실제 적용)
 * @return int 시야로 커버된 전사의 수
 */
int sightLeft(int x, int y, int N, bool isTest) {
    // 다이아몬드 형태로 왼쪽 셀을 시야에 포함시킴
    for (int i = y - 1; i >= 0; i--) {
        int top = max(0, x - (y - i));            // 상단 경계 계산
        int bottom = min(N - 1, x + (y - i));     // 하단 경계 계산
        for (int j = top; j <= bottom; j++) {
            sightMap[j][i] = 1;                    // 시야 설정
        }
    }

    // 장애물 처리: 시야 막힘 여부 확인
    bool obstructionFound = false;
    for (int i = y - 1; i >= 0; i--) {
        if (obstructionFound) {
            sightMap[x][i] = 0;                    // 장애물이 발견된 후에는 시야 제거
        }
        else {
            sightMap[x][i] = 1;                    // 장애물이 발견되지 않으면 시야 유지
        }

        if (warriorCountGrid[x][i]) {               // 전사가 있는 경우 장애물로 간주
            obstructionFound = true;
        }
    }

    // 장애물에 따라 시야 조정
    for (int i = y - 1; i > 0; i--) {
        int top = max(0, x - (y - i));             // 상단 경계 계산
        int bottom = min(N - 1, x + (y - i));      // 하단 경계 계산

        // 상단 측면 조정
        for (int j = top; j < x; j++) {
            if ((!sightMap[j][i]) || warriorCountGrid[j][i]) {
                if (j > 0) sightMap[j - 1][i - 1] = 0; // 왼쪽 위 셀의 시야 제거
                sightMap[j][i - 1] = 0;            // 바로 왼쪽 셀의 시야 제거
            }
        }

        // 하단 측면 조정
        for (int j = x + 1; j <= bottom; j++) {
            if ((!sightMap[j][i]) || warriorCountGrid[j][i]) {
                if (j + 1 < N) sightMap[j + 1][i - 1] = 0; // 왼쪽 아래 셀의 시야 제거
                sightMap[j][i - 1] = 0;                // 바로 왼쪽 셀의 시야 제거
            }
        }
    }

    // 시야로 커버된 전사 수 계산
    int coverage = 0;
    for (int i = y - 1; i >= 0; i--) {
        int top = max(0, x - (y - i));             // 상단 경계 계산
        int bottom = min(N - 1, x + (y - i));      // 하단 경계 계산
        for (int j = top; j <= bottom; j++) {
            if (sightMap[j][i]) {
                coverage += warriorCountGrid[j][i]; // 시야 내에 있는 전사의 수를 더함
            }
        }
    }

    // 테스트 모드인 경우 시야 맵을 원래대로 되돌림
    if (isTest) {
        for (int i = y - 1; i >= 0; i--) {
            int top = max(0, x - (y - i));
            int bottom = min(N - 1, x + (y - i));
            for (int j = top; j <= bottom; j++) {
                sightMap[j][i] = 0;                   // 시야 제거
            }
        }
    }

    return coverage;    // 커버리지 반환
}

/**
 * @brief 오른쪽 방향으로 시야를 설정하는 함수 (sightUp과 유사)
 *
 * @param x 현재 플레이어의 x 좌표
 * @param y 현재 플레이어의 y 좌표
 * @param N 그리드의 크기
 * @param isTest 테스트 모드 여부 (true: 테스트, false: 실제 적용)
 * @return int 시야로 커버된 전사의 수
 */
int sightRight(int x, int y, int N, bool isTest) {
    // 다이아몬드 형태로 오른쪽 셀을 시야에 포함시킴
    for (int i = y + 1; i < N; i++) {
        int top = max(0, x - (i - y));            // 상단 경계 계산
        int bottom = min(N - 1, x + (i - y));     // 하단 경계 계산
        for (int j = top; j <= bottom; j++) {
            sightMap[j][i] = 1;                    // 시야 설정
        }
    }

    // 장애물 처리: 시야 막힘 여부 확인
    bool obstructionFound = false;
    for (int i = y + 1; i < N; i++) {
        if (obstructionFound) {
            sightMap[x][i] = 0;                    // 장애물이 발견된 후에는 시야 제거
        }
        else {
            sightMap[x][i] = 1;                    // 장애물이 발견되지 않으면 시야 유지
        }

        if (warriorCountGrid[x][i]) {               // 전사가 있는 경우 장애물로 간주
            obstructionFound = true;
        }
    }

    // 장애물에 따라 시야 조정
    for (int i = y + 1; i < N - 1; i++) {
        int top = max(0, x - (i - y));             // 상단 경계 계산
        int bottom = min(N - 1, x + (i - y));      // 하단 경계 계산

        // 상단 측면 조정
        for (int j = top; j < x; j++) {
            if ((!sightMap[j][i]) || warriorCountGrid[j][i]) {
                if (j > 0) sightMap[j - 1][i + 1] = 0; // 오른쪽 위 셀의 시야 제거
                sightMap[j][i + 1] = 0;            // 바로 오른쪽 셀의 시야 제거
            }
        }

        // 하단 측면 조정
        for (int j = x + 1; j <= bottom; j++) {
            if ((!sightMap[j][i]) || warriorCountGrid[j][i]) {
                if (j + 1 < N) sightMap[j + 1][i + 1] = 0; // 오른쪽 아래 셀의 시야 제거
                sightMap[j][i + 1] = 0;                // 바로 오른쪽 셀의 시야 제거
            }
        }
    }

    // 시야로 커버된 전사 수 계산
    int coverage = 0;
    for (int i = y + 1; i < N; i++) {
        int top = max(0, x - (i - y));             // 상단 경계 계산
        int bottom = min(N - 1, x + (i - y));      // 하단 경계 계산
        for (int j = top; j <= bottom; j++) {
            if (sightMap[j][i]) {
                coverage += warriorCountGrid[j][i]; // 시야 내에 있는 전사의 수를 더함
            }
        }
    }

    // 테스트 모드인 경우 시야 맵을 원래대로 되돌림
    if (isTest) {
        for (int i = y + 1; i < N; i++) {
            int top = max(0, x - (i - y));
            int bottom = min(N - 1, x + (i - y));
            for (int j = top; j <= bottom; j++) {
                sightMap[j][i] = 0;                   // 시야 제거
            }
        }
    }

    return coverage;    // 커버리지 반환
}

/**
 * @brief 플레이어를 향해 전사들을 이동시키는 함수
 *
 * @param playerX 플레이어의 현재 x 좌표
 * @param playerY 플레이어의 현재 y 좌표
 * @param N 그리드의 크기
 * @param M 전사의 수
 * @return pii (총 이동한 전사 수, 플레이어에게 도달한 전사 수)
 */
pii moveWarriors(int playerX, int playerY, int N, int M) {
    int totalMoved = 0;   // 총 이동한 전사 수
    int totalHits = 0;    // 플레이어에게 도달한 전사 수

    // 전사의 이동 방향: 위, 아래, 왼쪽, 오른쪽
    const int moveDX[4] = { -1, 1, 0, 0 };
    const int moveDY[4] = { 0, 0, -1, 1 };

    // 모든 전사에 대해 이동 처리
    for (int i = 0; i < M; i++) {
        if (warriorPositions[i].first == -1)
            continue; // 이미 잡힌 전사는 건너뜀

        int warriorX = warriorPositions[i].first;
        int warriorY = warriorPositions[i].second;

        // 시야 내에 있는 전사는 이동하지 않음
        if (sightMap[warriorX][warriorY])
            continue;

        // 현재 플레이어와의 거리 계산
        int currentDistance = calculateManhattanDistance({ playerX, playerY }, { warriorX, warriorY });
        bool hasMoved = false;   // 이동 여부 플래그

        // 첫 번째 이동: 거리를 줄이기 위해 이동
        for (int dir = 0; dir < 4; dir++) {
            int nextX = warriorX + moveDX[dir];
            int nextY = warriorY + moveDY[dir];

            // 이동할 위치가 그리드 내에 있고 시야 내에 있지 않은지 확인
            if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N)
                continue;
            if (sightMap[nextX][nextY])
                continue;

            // 새로운 위치에서의 거리 계산
            int newDistance = calculateManhattanDistance({ playerX, playerY }, { nextX, nextY });
            if (newDistance < currentDistance) {
                warriorX = nextX;
                warriorY = nextY;
                hasMoved = true;
                totalMoved++;
                break; // 첫 번째 이동 후 루프 탈출
            }
        }

        // 두 번째 이동: 추가로 거리를 줄일 수 있는지 확인
        if (hasMoved) {
            int newDistance = calculateManhattanDistance({ playerX, playerY }, { warriorX, warriorY });
            for (int dir = 0; dir < 4; dir++) {
                // 반대 방향으로 이동 시도
                int nextX = warriorX + moveDX[(dir + 2) % 4];
                int nextY = warriorY + moveDY[(dir + 2) % 4];

                // 이동할 위치가 그리드 내에 있고 시야 내에 있지 않은지 확인
                if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N)
                    continue;
                if (sightMap[nextX][nextY])
                    continue;

                // 새로운 위치에서의 거리 계산
                int furtherDistance = calculateManhattanDistance({ playerX, playerY }, { nextX, nextY });
                if (furtherDistance < newDistance) {
                    warriorX = nextX;
                    warriorY = nextY;
                    totalMoved++;
                    break; // 두 번째 이동 후 루프 탈출
                }
            }
        }

        // 전사의 위치 업데이트
        warriorPositions[i] = { warriorX, warriorY };
    }

    // 플레이어에게 도달한 전사 수 계산
    for (int i = 0; i < M; i++) {
        if (warriorPositions[i].first == -1)
            continue; // 이미 잡힌 전사는 건너뜀

        if (warriorPositions[i].first == playerX && warriorPositions[i].second == playerY) {
            totalHits++;
            warriorPositions[i] = { -1, -1 }; // 전사를 잡힌 상태로 표시
        }
    }

    return { totalMoved, totalHits }; // 결과 반환
}

/**
 * @brief 현재 전사들의 위치를 기반으로 각 셀에 있는 전사의 수를 업데이트하는 함수
 *
 * @param N 그리드의 크기
 * @param M 전사의 수
 */
void updateWarriorCountGrid(int N, int M) {
    // 전사 수 그리드를 초기화
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            warriorCountGrid[i][j] = 0;

    // 각 전사의 위치를 확인하여 전사 수 그리드에 반영
    for (int i = 0; i < M; i++) {
        if (warriorPositions[i].first == -1)
            continue; // 이미 잡힌 전사는 건너뜀
        int x = warriorPositions[i].first;
        int y = warriorPositions[i].second;
        warriorCountGrid[x][y]++;
    }
}

int main()
{
    ios::sync_with_stdio(false); // 입출력 속도 향상을 위한 설정
    cin.tie(NULL);                // 입출력 연결 해제

    int N, M;                     // 그리드 크기 N, 전사 수 M
    cin >> N >> M;

    int startX, startY, endX, endY;   // 시작 지점과 종료 지점의 좌표
    cin >> startX >> startY >> endX >> endY;

    // 초기 전사 위치 입력
    for (int i = 0; i < M; i++) {
        cin >> warriorPositions[i].first >> warriorPositions[i].second;
    }

    // 장애물 그리드 입력
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> obstacleGrid[i][j];
        }
    }

    // 종료 지점으로부터 모든 셀까지의 거리를 계산
    computeDistances(endX, endY, N);

    // 시작 지점이 종료 지점에 도달할 수 없는 경우 종료
    if (distanceGrid[startX][startY] == -1) {
        cout << "-1\n";
        return 0;
    }

    int currentX = startX; // 현재 플레이어의 x 좌표
    int currentY = startY; // 현재 플레이어의 y 좌표

    // 메인 루프: 플레이어가 종료 지점에 도달할 때까지 반복
    while (true) {
        bool moved = false; // 플레이어가 이동했는지 여부

        // 현재 위치에서 종료 지점으로 향하는 방향으로 한 칸 이동
        //for (int dir = 0; dir < 4; dir++) {
        //    int nextX = currentX + DX[dir];
        //    int nextY = currentY + DY[dir];
        //    if (nextX < 0 || nextY < 0 || nextX >= N || nextY >= N)
        //        continue; // 그리드 경계를 벗어나면 무시
        //    if (distanceGrid[nextX][nextY] < distanceGrid[currentX][currentY]) {
        //        currentX = nextX;
        //        currentY = nextY;
        //        moved = true;
        //        break; // 이동 후 루프 탈출
        //    }
        //}

        // 종료 지점에 도달한 경우 종료
        if (currentX == endX && currentY == endY) {
            cout << "0\n"; // 종료 시 출력
            break;
        }

        // 현재 위치에 있는 전사들을 잡음 (시야로 인해)
        for (int i = 0; i < M; i++) {
            if (warriorPositions[i].first == currentX && warriorPositions[i].second == currentY) {
                warriorPositions[i] = { -1, -1 }; // 전사를 잡힌 상태로 표시
            }
        }

        // 현재 전사들의 위치를 기반으로 전사 수 그리드를 업데이트
        updateWarriorCountGrid(N, M);

        // 최적의 시야 방향을 선택하고 시야로 커버된 전사의 수를 계산
        int sightCoverage = chooseBestSight(currentX, currentY, N);

        // 전사들을 이동시키고 이동한 전사 수와 플레이어에게 도달한 전사 수를 얻음
        pii warriorResult = moveWarriors(currentX, currentY, N, M);

        // 결과 출력: 이동한 전사 수, 시야 커버리지, 플레이어에게 도달한 전사 수
        cout << warriorResult.first << " " << sightCoverage << " " << warriorResult.second << "\n";
    }

    return 0;
}
