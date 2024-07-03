#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;


void solve(int n){

    // M es la matriz de adyacencias. Straightforward input.
    vector<vector<int>> D(n, vector<int>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> D[i][j];
        }
    }
    
    vector<int> orden(n);
    for (int i = 0; i < n; ++i) {
        cin >> orden[i];
    }
    
    
    // ITERO AL REVES SOBRE ORDEN
    vector<bool> restaurado(n,false);
    long long energia_total = 0;

    for (int i = n-1; i >= 0; --i) {
        // aca tengo que "permitir pasar por el nodo orden[i]"
        // es decir, hacer el doble for loop que actualiza la matriz FW, 
        // pero permitiendo usar nodos intermedios en un orden particular
        int z = orden[i];
        restaurado[z] = true;
        for (int k = 0; k < n; ++k) {
            for (int j = 0; j < n; ++j) {
                D[k][j] = min(D[k][j], D[k][z] + D[z][j]);
            }
        }
        // en las iteraciones subsecuentes, se va a poder pasar por z, puesto que no fue destruido.

        // ahora, calcular la suma de las distancias minima entre cualquier par de nodos (sin contar dist(z,z))
        

        // osea, sumar todas las posiciones de la matriz FW actualizada, 
        // tales que ninguna entra o sale de una torre destruida
        for (int k = 0; k < n; ++k) {
            if (restaurado[k]) {
                for (int j = 0; j < n; ++j) {
                    if (restaurado[j]) {
                        energia_total += D[k][j];
                    }
                }
            }
        }
    }
    cout << energia_total << endl;
}



int main() {
    int t;
    cin >> t;

    while (t-- > 0) {
        int n;
        cin >> n;
        solve(n);
    }
    return 0;
}