#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int MAX = 100000;

string BF(vector<vector<int>> graph, vector<vector<int>> weight, int s)
{
    // cout << "ENTRE A BF" << endl;
    vector<int> dist(graph.size(), MAX); // pi
    dist[s] = 0;                         // pi[primero] = 0
    int size = graph.size();
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
            for (int k : graph[j])
            {
                dist[k] = min(dist[k], dist[j] + weight[j][k]);
            }
    }
    for (int i = 0; i < size; i++)
        for (int j : graph[i])
        {
            if (dist[j] > dist[i] + weight[i][j])
            {
                return "successful conspiracy";
            }
        }
    // cout << "BF FALSE" << endl;
    return "lamentable kingdom";
}

int main()
{
    int n;
    int m;
    cin >> n >> m;
    vector<string> answers;
    while (n != 0)
    {
        vector<vector<int>> graph(n + 2, vector<int>(0));           // matriz de adyacencia
        vector<vector<int>> weight(n + 2, vector<int>(n + 2, MAX)); // matriz de pesos
        for (int i = 1; i < n + 2; i++)
        {
            graph[0].push_back(i);
            weight[0][i] = 0;
        }
        // cout << "Armo el grafo" << endl;
        for (int i = 0; i < m; i++)
        {
            int s_i, n_i, k_i; // s_i es el indice de inicio, n_i es la long, k_i es la constante a comparar
            string o_i;        // gt es mayor que, lt es menor que
            cin >> s_i >> n_i >> o_i >> k_i;
            if (o_i == "lt")
            {
                graph[s_i + n_i + 1].push_back(s_i);
                weight[s_i + n_i + 1][s_i] = min(k_i - 1, weight[s_i + n_i + 1][s_i]);
            }
            else
            {
                graph[s_i].push_back(s_i + n_i + 1);
                weight[s_i][s_i + n_i + 1] = min(-k_i - 1, weight[s_i][s_i + n_i + 1]);
            }
        }
        // cout << "Armo weights" << endl;
        answers.push_back(BF(graph, weight, 0));
        cin >> n >> m;
    }
    for (string s : answers)
    {
        cout << s << endl;
    }
    // cout << "n: " << n << " m: " << m << " FIN DEL PROGRAMA" << endl;
    return 0;
}