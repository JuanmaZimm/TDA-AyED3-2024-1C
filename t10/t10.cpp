#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    int k;
    while (cin >> n >> k)
    {
        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
        }
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (v[i] >= v[k - 1] && v[i] > 0)
            {
                count++;
            }
        }
        cout << count << endl;
    }
}