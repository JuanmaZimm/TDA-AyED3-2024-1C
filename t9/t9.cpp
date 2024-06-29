#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;
int main()
{
    int cases;
    cin >> cases;
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

        for (const string &node : nodes)
        {
            cout << node << " ";
        }
        cout << endl;
    }
    int end;
    cin >> end;
}