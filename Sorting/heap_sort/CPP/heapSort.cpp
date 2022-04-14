#include <iostream>
#include <vector>
#include <ctime>
#include <cmath>

using namespace std;

void heapify(vector<int>& numArr, int k);
void heapSort(vector<int>& numArr);

int main() {
    vector<int> numArr;
    int n;

    cout << "10^n n value : ";
    cin >> n;

    srand(time(NULL));
    for (int i = 0; i < (int)pow(10, n); i++) {
        numArr.push_back(rand());
    }

	for (int j=numArr.size()/2; j >= 0; j--) {
		heapify(numArr, j);
	}

    for (int num : numArr) {
        cout << num << " ";
    } cout << endl;

    heapSort(numArr);

    for (int num : numArr) {
        cout << num << " ";
    }

    return 0;
}

void heapify(vector<int>& numArr, int current) {
    if (((int)numArr.size() / 2) - 1 < current ) return;
    int left = 2 * current + 1;
    int right = 2 * current + 2;

    // there is a childNode
    if (right == numArr.size()) {
        if (numArr[left] > numArr[current])
            swap(numArr[left], numArr[current]);
        return;
    }

    // there are two childNodes
    int max = left;
    if (numArr[max] < numArr[right])
        max = right;
    
    if (numArr[max] > numArr[current]) {
        swap(numArr[max], numArr[current]);
    }
    heapify(numArr, max);
}

void heapSort(vector<int>& numArr) {
    static vector<int> resultArr;
    if (numArr.empty()) {
        numArr.assign(resultArr.begin(), resultArr.end());
        resultArr.clear();
        return;
    }
    swap(numArr.back(), numArr.front());
    resultArr.push_back(numArr.back());
    numArr.pop_back();
    heapify(numArr, 0);
    heapSort(numArr);
}