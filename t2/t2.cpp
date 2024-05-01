#include <iostream>
#include <vector>
#define forn(i, n) for(int i = 0; i < n; i++)
using namespace std;

void solve(int caso, int n, int alturas[], int anchos[]){
    int maxIncSeq = 0;
    int maxDecSeq = 0;
    vector<int> inS(n);
    vector<int> deS(n);

    forn(i, n){
        inS[i] = anchos[i];
        deS[i] = anchos[i];

        forn(j, i){            
            if (alturas[j] < alturas[i]){             
                inS[i] = max(inS[i], inS[j] + anchos[i]);
            }

            if (alturas[j] > alturas[i]){
                deS[i] = max(deS[i], deS[j] + anchos[i]);
            }
        }

        maxIncSeq = max(maxIncSeq, inS[i]);
        maxDecSeq = max(maxDecSeq, deS[i]);
    }

    if(maxDecSeq <= maxIncSeq)
        cout << "Case " << caso << ". Increasing (" << maxIncSeq << "). Decreasing (" << maxDecSeq << ").\n";
    else
        cout << "Case " << caso << ". Decreasing (" << maxDecSeq << "). Increasing (" << maxIncSeq << ").\n";
}

int main(){
    int nCasos;
    cin >> nCasos;
    forn(i, nCasos){
        int n;
        cin >> n;
        int alturas[n];
        int anchos[n];
        forn(i, n){
            cin >> alturas[i];
        }
        forn(i, n){
            cin >> anchos[i];
        }
        solve(i+1, n, alturas, anchos);
    }
    return 0;
}