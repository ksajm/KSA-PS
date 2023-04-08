#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;


int main()
{
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int w, h, f[64][64], time[64][64], dirx[4]={1,0,-1,0}, diry[4]={0,1,0,-1};
    priority_queue<pair<int, pair<int, int>>> pq;
    cin>>w>>h;
    for (int i=0;i<h;i++)
    {
        for (int j=0;j<w;j++)
        {
            cin>>f[i][j];
        }
    }
    for (int i=0;i<h;i++)
    {
        for (int j=0;j<w;j++)
        {
            time[i][j]=9999999;
        }
    }
    for (int i=0;i<h;i++)
    {
        for (int j=0;j<w;j++)
        {
            if (f[i][j]==-1)
            {
                time[i][j]=0;
                pq.push(make_pair(0,make_pair(j,i)));
                while (!pq.empty())
                {
                    int curtime=-pq.top().first, herex=pq.top().second.first, herey=pq.top().second.second;
                    for (int k=0;k<4;k++)
                    {
                        int therex=herex+dirx[k], therey=herey+diry[k];
                        if (therex<0||therex>=w||therey<0||therey>=h||curtime>time[therey][therex])
                        {
                            continue;
                        }
                        int newtime;
                        if (f[therey][therex]!=-1)
                        {
                            newtime=curtime+f[therey][therex]+1;
                        }
                        else
                        {
                            newtime=curtime+1;
                        }
                        if (newtime<time[therey][therex])
                        {
                            time[therey][therex]=newtime;
                            pq.push(make_pair(-newtime, make_pair(therex, therey)));
                        }
                    }
                    pq.pop();
                }
                break;
            }
        }
    }
    for (int i=0;i<h;i++)
    {
        for (int j=0;j<w;j++)
        {
            if (f[i][j]==-1&&time[i][j]!=0)
            {
                cout<<time[i][j];
            }
        }
    }
}