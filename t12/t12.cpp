#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

long energy(int n, vector<vector<int>> graph, vector<int> order)
{

    vector<bool> aux(n, false);
    long res = 0;

    for (int i = n - 1; i >= 0; --i)
    {
        int z = order[i];
        aux[z] = true;
        for (int k = 0; k < n; ++k)
        {
            for (int j = 0; j < n; ++j)
            {
                graph[k][j] = min(graph[k][j], graph[k][z] + graph[z][j]);
            }
        }

        for (int k = 0; k < n; ++k)
        {
            if (aux[k])
            {
                for (int j = 0; j < n; ++j)
                {
                    if (aux[j])
                    {
                        res += graph[k][j];
                    }
                }
            }
        }
    }
    return res;
}

int main()
{
    int cases;
    cin >> cases;

    vector<long> answers;

    while (cases--)
    {
        int n;
        cin >> n;

        vector<vector<int>> graph(n, vector<int>(n));

        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                cin >> graph[i][j];
            }
        }
        vector<int> order(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> order[i];
        }

        long answer = energy(n, graph, order);
        answers.push_back(answer);
    }
    for (long e : answers)
    {
        cout << e << endl;
    }
    return 0;
}