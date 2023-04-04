#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

queue<int> qx, qy;
int dirx[4] = { 0, 1, 0, -1 }, diry[4] = { 1, 0, -1, 0 };

int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int f[64][64], visited[64][64] = { 0, };
    int w, h;
    cin >> w >> h;
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            cin >> f[i][j];
        }
    }

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            if (f[i][j] == -1)
            {
                int size = 1, dist = 0;
                qx.push(j), qy.push(i);
                while (!qx.empty())
                {
                    int herex = qx.front(), herey = qy.front();
                    visited[herey][herex] = 1;
                    for (int i = 0; i < 4; i++)
                    {
                        int therex = herex + dirx[i], therey = herey + diry[i];
                        if (therex >= 0 && therex < w && therey >= 0 && therey < h)
                        {
                            if (visited[therey][therex] != 1 && f[therey][therex] == -1)
                            {
                                cout << dist + 1;
                                return 0;
                            }
                            if (visited[therey][therex] != 1 && f[therey][therex] == 0)
                            {
                                qx.push(therex);
                                qy.push(therey);
                            }
                        }
                    }
                    qx.pop();
                    qy.pop();
                    size--;
                    if (size == 0) {
                        dist++;
                        size = qx.size();
                    }
                }
            }
        }
    }
}