#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long a;
    int n, exp = 1;
    vector<long long> powSet;
    vector<int> isValueInPowSet;

    cin >> a >> n;
    powSet.resize(2 * n + 1, 0);
    powSet[1] = a;
    isValueInPowSet.push_back(1);
    while (exp * 2 < n) {
        a = a * a;
        exp = 2 * exp;
        powSet[exp] = a;
        isValueInPowSet.push_back(exp);
    }

    int interval = n - exp;
    for (int i = isValueInPowSet.size() - 1; i >= 0; i--) {
        if (isValueInPowSet[i] <= interval) {
            exp = exp + isValueInPowSet[i];
            a = a * powSet[isValueInPowSet[i]];
            interval = n - exp;
        }
    }

    cout << a;

    return 0;
}