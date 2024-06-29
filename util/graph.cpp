#include <vector>
#include <iostream>
#include <queue>
#include <set>
#include <stack>

struct Graph {
  int n;
  std::vector<std::vector<int>> adjacentes;
};

void bfs(const Graph& g, int s) {
    std::queue<int> q;
    std::set<int> seen;
    q.push(s);
    seen.insert(s);
    std::cout << "Vi a " << s << " (la fuente)." << std::endl;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : g.adjacentes[u]) {
            if (!seen.contains(v)) {
                q.push(v);
                seen.insert(v);
                std::cout << "Vi a " << v << "." << std::endl;
            }
        }
    }
}

void dfs(const Graph& g, int s) {
    std::stack<int> q;
    std::set<int> seen;
    q.push(s);
    seen.insert(s);
    std::cout << "Vi a " << s << " (la fuente)." << std::endl;
    while (!q.empty()) {
        int u = q.top();
        q.pop();
        for (int v : g.adjacentes[u]) {
            if (!seen.contains(v)) {
                q.push(v);
                seen.insert(v);
                std::cout << "Vi a " << v << "." << std::endl;
            }
        }
    }
}

int main() {
  int n, m;
  std::cin >> n >> m;
  Graph g{.n = n};
  g.adjacentes.resize(n);
  for (int i = 0; i < m; ++i) {
    int u, v;
    std::cin >> u >> v;
    g.adjacentes[u].push_back(v);
  }
  
  int source;
  std::cin >> source;
  std::cout << "BFS:" << std::endl;
  bfs(g, source);
  std::cout << "DFS:" << std::endl;
  dfs(g, source);
}