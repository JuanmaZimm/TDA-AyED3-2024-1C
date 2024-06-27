#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>

using namespace std;

// Function to calculate the movement cost between two codes
int lock_moves(int start, int end) {
    string start_str = to_string(start), end_str = to_string(end);
    while (start_str.size() < 4) start_str = '0' + start_str;
    while (end_str.size() < 4) end_str = '0' + end_str;
    
    int total_moves = 0;
    for (int i = 0; i < 4; ++i) {
        int diff = abs(start_str[i] - end_str[i]);
        total_moves += min(diff, 10 - diff);
    }
    return total_moves;
}

// Prim's algorithm to find the MST cost
int primMST(vector<vector<int>>& graph, int n) {
    vector<int> key(n, INT_MAX);
    vector<bool> inMST(n, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    key[0] = 0;
    pq.push({0, 0}); // {weight, node}

    int mst_cost = 0;
    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (inMST[u]) continue;
        inMST[u] = true;
        mst_cost += key[u];

        for (int v = 0; v < n; ++v) {
            int weight = graph[u][v];
            if (!inMST[v] && weight < key[v]) {
                key[v] = weight;
                pq.push({key[v], v});
            }
        }
    }
    return mst_cost;
}

int main() {
    int cases;
    cin >> cases;
    
    while (cases--) {
        int n;
        cin >> n;
        
        vector<int> codes(n);
        for (int i = 0; i < n; ++i) {
            cin >> codes[i];
        }

        // Create the graph
        vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));

        // Add the 0000 initial state as node 0
        codes.insert(codes.begin(), 0);

        for (int i = 0; i <= n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                int cost = lock_moves(codes[i], codes[j]);
                graph[i][j] = cost;
                graph[j][i] = cost;
            }
        }

        // Find MST using Prim's algorithm
        int result = primMST(graph, n + 1);
        cout << result << endl;
    }

    return 0;
}
