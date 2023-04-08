#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, m, maxval = -1, past, room;
    cin >> n >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> room;
        if (i == 0)
        {
            maxval = max(maxval, room - 423);
        }
        else
        {
            maxval = max(maxval, (room - past) / 2);
        }
        past = room;
    }
    maxval = max(maxval, 423 + n - 1 - room);
    cout << maxval + 8;
}