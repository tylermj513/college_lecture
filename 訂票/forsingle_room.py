 #include <iostream>
#include <vector>
#include <algorithm>
#define P 7
#define R 3

using namespace std;

bool is_safe(int process_id, vector<bool>& marked, vector<vector<int>>& allocated,
             vector<vector<int>>& maxm, vector<int>& available) {
    for (int i = 0; i < R; i++) {
        if (maxm[process_id][i] - allocated[process_id][i] > available[i]) {
            return false;
        }
    }
    return true;
}

void safe_sequence(vector<bool>& marked, vector<vector<int>>& allocated,
                   vector<vector<int>>& maxm, vector<int>& available, vector<int>& safe) {
    for (int i = 0; i < P; i++) {
        if (!marked[i] && is_safe(i, marked, allocated, maxm, available)) {
            marked[i] = true;
            for (int j = 0; j < R; j++) {
                available[j] += allocated[i][j];
            }
            safe.push_back(i);

            safe_sequence(marked, allocated, maxm, available, safe);

            safe.pop_back();
            marked[i] = false;

            for (int j = 0; j < R; j++) {
                available[j] -= allocated[i][j];
            }
        }
    }

    if (safe.size() == P) {
        cout << "1212Safe sequence: ";
        for (int i = 0; i < P; i++) {
            cout << "P" << safe[i] << " ";
            if (i != P - 1) {
                cout << "-> ";
            }
        }
        cout << endl;
    }
}

int main() {
    vector<int> avail = {3, 0, 6};
    
    vector<vector<int>> maxm = {
        {0, 3, 0},
        {3, 6, 5},
        {2, 1, 5},
        {5, 6, 1},
        {6, 1, 0},
        {4, 1, 3},
        {0, 6, 8}
    };

    vector<vector<int>> allot = {
        {0, 1, 0},
        {1, 2, 2},
        {1, 1, 0},
        {1, 2, 0},
        {2, 1, 0},
        {1, 1, 1},
        {0, 0, 0}
    };

    vector<int> available(R, 0);
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < P; j++) {
            available[i] += allot[j][i];
        }
        available[i] = avail[i] - available[i];
    }

    vector<bool> marked(P, false);
    vector<int> safe;

    cout << "Safe sequences are:" << endl;
    safe_sequence(marked, allot, maxm, available, safe);

    return 0;
}
 