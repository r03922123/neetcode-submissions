
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;

        vector<int> dirs = {-1, 0, 1, 0, -1};
        int m = grid.size();
        int n = grid[0].size();
        int island_cnt = 0;

        function<void(int, int)> dfs = [&](int i, int j) {
            grid[i][j] = '0';

            auto valid = [&](int x, int y){
                return x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == '1';
            };
            
            for (int k = 0; k < 4; ++k) {
                int x = i + dirs[k];
                int y = j + dirs[k + 1];
                if (valid(x, y)) {
                    dfs(x, y);
                };
            }
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    island_cnt++;
                    dfs(i, j);

                }
            }
        }
        return island_cnt;

    }
};
