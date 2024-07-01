#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

const int MAX = 21;

int lockMoves(string a, string b)
{
    int moves = 0;
    for (int i = 0; i < 4; i++)
    {
        moves += min(abs(a[i] - b[i]), 10 - abs(a[i] - b[i]));
    }
    return moves;
}

vector<vector<int>> buildGraph(vector<string> nodes, int n)
{
    vector<vector<int>> graph(n, vector<int>(n, MAX));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i != j)
            {
                graph[i][j] = lockMoves(nodes[i], nodes[j]);
            }
            else
            {
                graph[i][j] = MAX;
            }
        }
    }
    return graph;
}

int prim(vector<vector<int>> graph, int n)
{
    vector<int> minTree(n, MAX);
    minTree[0] = 0;
    vector<bool> visited(n, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> stack;
    stack.push({0, 0});
    int moves = 0;
    while (!stack.empty())
    {
        int j = stack.top().second;
        stack.pop();

        if (!visited[j])
        {
            visited[j] = true;
            moves += minTree[j];
            for (int i = 0; i < n; ++i)
            {
                if (graph[j][i] != MAX && graph[j][i] < minTree[i] && !visited[i])
                {
                    minTree[i] = graph[j][i];
                    stack.push(make_pair(minTree[i], i));
                }
            }
        }
    }
    return moves;
}

int start(vector<string> nodes, int n)
{
    string start = "0000";
    int moves = MAX;
    for (int i = 0; i < n; i++)
    {
        int aux = lockMoves(start, nodes[i]);
        if (aux < moves)
        {
            moves = aux;
        }
    }
    return moves;
}

int main()
{
    int cases;
    cin >> cases;
    vector<int> answers;
    while (cases--)
    {
        int n;
        cin >> n;
        vector<string> nodes;
        for (int i = 0; i < n; i++)
        {
            string number;
            cin >> number;
            nodes.push_back(number);
        }

        vector<vector<int>> graph = buildGraph(nodes, n);
        int answer = prim(graph, n) + start(nodes, n);
        answers.push_back(answer);
    }
    for (int i = 0; i < answers.size(); i++)
    {
        cout << answers[i] << endl;
    }
}

/*
4
2 1155 2211
3 1111 1155 5511
3 1234 5678 9090
4 2145 0213 9113 8113
*/