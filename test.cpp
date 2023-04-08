#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
/*
    code by Raehwan
    & refactored by Junee
*/

int w, h, location[64][64], timeArray[64][64], dirx[4] = { 1, 0, -1, 0 }, diry[4] = { 0, 1, 0, -1 };
priority_queue<pair<int, pair<int, int>>> pq;

void getInput() {
    cin >> w >> h;
    for (int i = 0; i < h; i++)
    {
        for (int j=0;j<w;j++)
        {
            cin >> location[i][j];
        }
    }
}

void initTime() {
    for (int i = 0; i < h; i++)
    {
        for (int j=0;j<w;j++)
        {
            timeArray[i][j] = 9999999;
        }
    }
}

void dijkstra() {
    while (!pq.empty())
    {
        int curTime = -pq.top().first, hereX = pq.top().second.first, hereY = pq.top().second.second;
        for (int k = 0; k < 4; k++)
        {
            int thereX = hereX + dirx[k], thereY = hereY + diry[k];
            bool isInRange = (thereX >= 0 && thereX < w && thereY >= 0 && thereY < h);

            if (!isInRange || curTime > timeArray[thereY][thereX])
            {
                continue;
            }

            int newTime;
            if (location[thereY][thereX] != -1)
            {
                newTime = curTime + location[thereY][thereX] + 1;
            }
            else
            {
                newTime = curTime + 1;
            }

            if(newTime < timeArray[thereY][thereX])
            {
                timeArray[thereY][thereX] = newTime;
                pq.push( make_pair(-newTime, make_pair(thereX, thereY)) );
            }
        }
        pq.pop();
    }
}

int getAnswer() {
    for(int i = 0; i < h; i++)
    {
        for(int j = 0; j < w; j++)
        {
            if(location[i][j] == -1 && timeArray[i][j] != 0)
            {
                return timeArray[i][j];
            }
        }
    }
}

int main()
{
    getInput();
    initTime();
    bool solved = false;
    for(int i=0;i<h;i++)
    {
        for(int j=0;j<w;j++)
        {
            if(location[i][j]==-1)
            {
                timeArray[i][j]=0;
                pq.push(make_pair(0,make_pair(j,i)));
                dijkstra();
                solved = true;
                break;
            }
        }
        if (solved)
        {
            break;
        }
    }
    cout << getAnswer();
}