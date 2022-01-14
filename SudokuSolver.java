public class SudokuSolver{
	public static void main(String[] args) {
		char[][] board = {	
			{'5','2',' ',' ','7',' ','6',' ',' '},
			{' ','7',' ','3','4',' ',' ',' ','2'},
			{' ',' ',' ',' ',' ','1',' ','9',' '},
			{'6','1','8',' ','3','4',' ',' ',' '},
			{'3','5','2',' ',' ',' ','1','4','8'},
			{' ',' ',' ','1','8',' ','3','6','5'},
			{' ','6',' ','8',' ',' ',' ',' ',' '},
			{'4',' ',' ',' ','6','7',' ','8',' '},
			{' ',' ','9',' ','5',' ',' ','7','6'}	};

		/*{	
			{' ',' ',' ',' ',' ',' ',' ',' ','1'},
			{' ','5',' ',' ','9','4',' ',' ','6'},
			{'9','2',' ',' ',' ','7','3','4',' '},
			{'6','8','5','1',' ',' ',' ',' ','9'},
			{'7',' ',' ',' ',' ',' ','1','6','2'},
			{'2',' ','9','7',' ',' ',' ',' ',' '},
			{'1',' ','7','6','3','8','2',' ','4'},
			{' ','4','2',' ','5','1',' ',' ',' '},
			{'5','6','8','4','7',' ',' ',' ',' '}	};
		*/


		if (solve(board)) {
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					System.out.print(board[i][j] + ", ");
				}
				System.out.println();
			}
		}
	}

	private static boolean solve(char[][] board) {
	 	int[] place = findSpace(board);
	 	return solve(board, place[0], place[1]);
	}

	private static boolean solve(char[][] board, int row, int col) {
		char[] iter = {'1','2','3','4','5','6','7','8','9'};
		boolean ret;
		boolean done = false;
		if (row == -1) {
			return ret = true;
		} 
		else {

			/*
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++) {
					System.out.print(board[i][j] + ", ");
				}
				System.out.println();
			}
			System.out.println();
			*/

			for (int i = 0; i < 9; i++) {
				board[row][col] = iter[i];
				// System.out.println("Checking val: " + iter[i]);
				if (isValid(board, row,col)) {
					int[] place = findSpace(board);
					ret = solve(board, place[0], place[1]);
					if (ret) {
						// System.out.println("DONE");
						done = true;
						break;
					}
				} 
			}
			if(!done) {
				board[row][col] = ' ';
				/* System.out.println("Backtracking...");
				for (int i = 0; i < 9; i++) {
					for (int j = 0; j < 9; j++) {
						System.out.print(board[i][j] + ", ");
					}
					System.out.println();
				}
				System.out.println();
				*/
				return false;
			} else 
				return true;
		}
	}

	private static int[] findSpace(char[][] board) {
		int[] place = {-1,-1};
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				if (board[i][j] == ' ') {
					return new int[] {i,j};
				}
			}
		}
		return place;
	}

	private static boolean isValid(char[][] board, int row, int col) {
		// System.out.println("Checking, row: " + row + " col: " + col);
		boolean ret = false;
		if(checkCol(board, col)) {
			// System.out.println("Valid col");
			if(checkRow(board, row)) {
				// System.out.println("Valid row");
				if(checkBox(board, row,col)) {
					// System.out.println("Valid");
					ret = true;
				}
			}
		}
		return ret;
	}

	// Checks if col is valid
	private static boolean checkCol(char[][] board, int col) {
		boolean ret = false;
		String temp = "";
		// Loops through column and checks for duplicates
		for (int i = 0; i < 9; i++) {
			char val = board[i][col];
			if (val == ' ') {
				if (i == 8) {
					ret = true;
				}
				continue;
			}
			if (temp.indexOf(val) < 0) {
				temp += val;
				if (i == 8) {
					ret = true;
				}
			} else {
				break;
			}
		}
		return ret;
	}

	// Checks if row is valid
	private static boolean checkRow(char[][] board, int row) {
		boolean ret = false;
		String temp = "";
		// Loops through column and checks for duplicates
		for (int i = 0; i < 9; i++) {
			char val = board[row][i];
			if (val == ' ') {
				if (i == 8) {
					ret = true;
				}
				continue;
			}
			if (temp.indexOf(val) < 0) {
				temp += val;
				if (i == 8) {
					ret = true;
				}
			} else
				break;
		}
		return ret;
	}

	private static boolean checkBox(char[][] board, int row, int col){
		boolean ret = false;
		String temp = "";
		if (col > 5)
			col = 6;
		else if (col > 2)
			col = 3;
		else
			col = 0;

		if (row > 5)
			row = 6;
		else if (row > 2)
			row = 3;
		else
			row = 0;

		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				char val = board[row+i][col+j];
				if (val == ' ') {
					if (i == 2 & j == 2) {
						ret = true;
					}
					continue;
				}
				if (temp.indexOf(val) < 0) {
					temp += val;
					if (i == 2 & j == 2) {
						ret = true;
					}
				} else
					break;
			}
		}
		return ret;
	}
}