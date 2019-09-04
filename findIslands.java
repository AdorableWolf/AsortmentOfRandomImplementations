import java.util.*;

class findIslands {
    boolean isSafe(int M[][], int row, int col, boolean visited[][], int ROW, int COL) {
        return (row >= 0) && (row < ROW) && (col >= 0) && (col < COL) && (M[row][col] == 1 && !visited[row][col]);
    }

    void DFS(int M[][], int row, int col, boolean visited[][], int ROW, int COL) {

        // arrays used to get the 8 neighbours of the current cell.
        int rowNum[] = new int[] { -1, -1, -1, 0, 0, 1, 1, 1 };
        int colNum[] = new int[] { -1, 0, -1, 1, 0, -1, 0, 1 };

        visited[row][col] = true;

        for (int i = 0; i < 8; i++) {
            if (isSafe(M, row + rowNum[i], col + colNum[i], visited, ROW, COL)) {
                DFS(M, row + rowNum[i], col + colNum[i], visited, ROW, COL);
            }
        }
    }

    int countIslands(int M[][], int ROW, int COL) {

        boolean visited[][] = new boolean[ROW][COL];

        int count = 0;

        for (int i = 0; i < ROW; ++i) {
            for (int j = 0; j < COL; ++j) {
                if (M[i][j] == 1 && !visited[i][j]) {
                    DFS(M, i, j, visited, ROW, COL);
                    ++count;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) throws Exception {

        Scanner input = new Scanner(System.in);
        System.out.print("Please enter the number of rows: ");
        int ROW = input.nextInt();
        System.out.print("Please enter the number of columns: ");
        int COL = input.nextInt();

        int M[][] = new int[ROW][COL];

        System.out.println("Please enter " + ROW + " x " + COL + " boolean matrix: ");
        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                M[i][j] = input.nextInt();
            }
        }
        input.close();

        findIslands I = new findIslands();
        System.out.println("Number of islands is: " + I.countIslands(M, ROW, COL));

    }
}