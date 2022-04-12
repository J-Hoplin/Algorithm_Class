#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>

using namespace std;

void recursiveQuickSort(vector<int>& numArr, int start, int end);

int main() {
    vector<vector<int>> dataSet;
    vector<vector<int>> resultSet;

    for (long long i = 100; i <= 100; i *= 100) { // i <= 10^4 it can do but slow
        vector<int> data;
        for (int j = 0; j < 20; j++) {
            for (long long numCount = 0; numCount < i; numCount++) {
                data.push_back(rand());
            }
            dataSet.push_back(data);
        }
    }

    for (vector<int>& data : dataSet) { // do quickSort and store result at resultSet
        vector<int> sample = { data.begin(), data.end() };
        recursiveQuickSort(sample, 0, sample.size());
        resultSet.push_back(sample);
    }

    for (vector<int>& result : resultSet) {
        for (int num : result)
            cout << num << " ";
        cout << "\n";
    }

    return 0;
}

void recursiveQuickSort(vector<int>& numArr, int start, int end) {
    if (start == end) return;
    int pivot, midPoint = start + 1;

    pivot = numArr[start];
    for (int i = midPoint; i < end; i++) {
        if (numArr[i] < pivot) {
            swap(numArr[i], numArr[midPoint]);
            midPoint++;
        }
    }
    // place pivot in right position and rearrange areas based on the position
    swap(numArr[start], numArr[midPoint - 1]);
    recursiveQuickSort(numArr, start, midPoint - 1);
    recursiveQuickSort(numArr, midPoint, end);
}