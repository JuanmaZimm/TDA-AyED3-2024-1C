#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

int max_acorns(vector<vector<int>> &grid, int t, int h, int f)
{
    vector<vector<int>> memoria(t, vector<int>(h, 0));
    vector<int> aux(h, 0);

    for (int arbol = 0; arbol < t; ++arbol)
    {
        memoria[arbol][h - 1] = grid[arbol][h - 1];
    }

    for (int altura = h - 2; altura >= 0; --altura)
    {
        for (int arbol = 0; arbol < t; ++arbol)
        {
            if (altura + f < h)
            {
                memoria[arbol][altura] = grid[arbol][altura] + max(memoria[arbol][altura + 1], aux[altura + f]);
            }
            else
            {
                memoria[arbol][altura] = grid[arbol][altura] + max(memoria[arbol][altura + 1], 0);
            }
            aux[altura] = max(aux[altura], memoria[arbol][altura]);
        }
    }

    int res = 0;
    for (int arbol = 0; arbol < t; ++arbol)
    {
        res = max(res, memoria[arbol][0]);
    }
    return res;
}

int main()
{
    int c, t, h, f;
    stringstream res;
    cin >> c;
    while (c--)
    {
        cin >> t >> h >> f;
        vector<vector<int>> grid(t, vector<int>(h, 0));
        for (int i = 0; i < t; i++)
        {
            int a;
            cin >> a;
            while (a--)
            {
                int p;
                cin >> p;
                grid[i][p - 1]++;
            }
        }

        int rta = max_acorns(grid, t, h, f);
        res << rta << endl;
    }

    cout << res.str();
    return 0;
} // usuario de vJudge: JuanmaZimm