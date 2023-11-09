#include <iostream>
#include <vector>

using namespace std;

void drawTreeForComponent(vector<vector<int>>& arr, int i, int j, vector<vector<bool>>& visited){
    if(i < 0 || j < 0 || i >= arr.size() || j >= arr[0].size() || arr[i][j] == 1 || visited[i][j] == true) return;
    
    visited[i][j] = true;

    drawTreeForComponent(arr, i - 1, j, visited);
    drawTreeForComponent(arr, i, j + 1, visited);
    drawTreeForComponent(arr, i, j - 1, visited);
    drawTreeForComponent(arr, i + 1, j, visited);

}

int main() {
    int m, n, count = 0;
    cin >> m >> n;

    vector<vector<int>> arr(m, vector<int>(n));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    vector<vector<bool>> visited(arr.size(), vector<bool>(arr[0].size()));
    for(int i = 0; i < arr.size(); i++){
        for(int j = 0; j < arr[0].size(); j++){
            if(arr[i][j] == 0 && visited[i][j] == false){
                drawTreeForComponent(arr, i, j, visited);
                count++;
            }
        }
    }

    cout<<count;

    return 0;
}
