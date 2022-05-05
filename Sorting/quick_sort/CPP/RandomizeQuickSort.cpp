#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>
#include <stack>
#include <algorithm>
#include <ctime>

using namespace std;

vector<int>* randomizedQuickSort(const vector<int>& inputData);

int main() {
    vector<vector<int>> dataSet;
    vector<vector<int>*> resultSet;

    for (long long i = 100; i <= 100; i *= 100) { // i <= 10^4 it can do but slow
        vector<int> data;
        for (int j = 0; j < 20; j++) {
            for (long long numCount = 0; numCount < i; numCount++) {
                data.push_back(rand());
            }
            dataSet.push_back(data);
        }
    }

    for (vector<int>& data : dataSet) {
        resultSet.push_back(randomizedQuickSort(data));
    }

    for (vector<int>* result : resultSet) {
        for (int num : *result)
            cout << num << " ";
        cout << "\n";
    }

    for (vector<int>* result : resultSet) {
        delete result;
    }

    return 0;
}

vector<int>* randomizedQuickSort(const vector<int>& inputData) {
    vector<int>* resultDataPointer = new vector<int>{ inputData.begin(), inputData.end() };
    vector<int>& resultData = *resultDataPointer;
    stack<pair<int, int>> sortRanges; // start, end

    sortRanges.push(make_pair(0, resultData.size()));
    while (!sortRanges.empty()) {
        // assign variables to ranges
        pair<int, int> range = sortRanges.top();
        sortRanges.pop();
        int start = range.first, end = range.second;
        if (start == end) continue;

        // decide pivot and position that starting point in resultData for sorting
        int randomIndex = start + (rand() % (start - end));
        int pivot = resultData[randomIndex];
        swap(resultData[start], resultData[randomIndex]);
        int midPoint = start + 1;

        for (int i = midPoint; i < end; i++) {
            if (resultData[i] < pivot) {
                swap(resultData[i], resultData[midPoint]);
                midPoint++;
            }
        }

        // place pivot in right position and rearrange areas based on the position
        swap(resultData[start], resultData[midPoint - 1]);
        sortRanges.push(make_pair(start, midPoint - 1));
        sortRanges.push(make_pair(midPoint, end));
        // quickSort(numArr, start, midPoint - 1);
        // quickSort(numArr, midPoint, end);
    }

    return resultDataPointer;
}

