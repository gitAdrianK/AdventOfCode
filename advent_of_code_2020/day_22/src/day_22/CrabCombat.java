package day_22;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;

public class CrabCombat {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay22("test_input.txt");
		// Don't run this for part 1 combat
		solveDay22("test_input_2.txt");
		long time = System.currentTimeMillis();
		solveDay22("input.txt");
		System.out.println(System.currentTimeMillis() - time);
	}

	public static void solveDay22(String input) throws FileNotFoundException {
		Player playerOne = new Player("Player 1");
		Player playerTwo = new Player("Player 2");
		boolean isPlayerOne = true;
		Scanner sc = new Scanner(new File(input));
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			if (line.contains("Player")) {
				continue;
			}
			if (line.isEmpty()) {
				isPlayerOne = false;
				continue;
			}
			int card = Integer.parseInt(line);
			if (isPlayerOne) {
				playerOne.add(card);
			} else {
				playerTwo.add(card);
			}
		}
		sc.close();
		System.out.println(input);
		// System.out.println(getWinValue(doCombat(playerOne.subdeckPlayer(), playerTwo.subdeckPlayer())));
		System.out.println(getWinValue(doRecursiveCombat(playerOne.subdeckPlayer(), playerTwo.subdeckPlayer())));
	}

	private static Player doRecursiveCombat(Player playerOne, Player playerTwo) {
		HashSet<String> playerOnePrevious = new HashSet<String>();
		HashSet<String> playerTwoPrevious = new HashSet<String>();
		while (!isDeckOutVictory(playerOne, playerTwo)) {
			String currOneStr = playerOne.getCards().toString();
			String currTwoStr = playerTwo.getCards().toString();
			if (playerOnePrevious.contains(playerOne.getCards().toString()) && playerTwoPrevious.contains(playerTwo.getCards().toString())) {
				return playerOne;
			}
			playerOnePrevious.add(currOneStr);
			playerTwoPrevious.add(currTwoStr);
			int playerOneCard = playerOne.remove();
			int playerTwoCard = playerTwo.remove();
			if (playerOneCard <= playerOne.size() && playerTwoCard <= playerTwo.size()) {
				Player subPlayerOne = playerOne.subdeckPlayer(playerOneCard);
				Player subPlayerTwo = playerTwo.subdeckPlayer(playerTwoCard);
				Player winner = doRecursiveCombat(subPlayerOne, subPlayerTwo);
				if (winner.equals(playerOne)) {
					playerOne.add(playerOneCard);
					playerOne.add(playerTwoCard);
				} else {
					playerTwo.add(playerTwoCard);
					playerTwo.add(playerOneCard);
				}
			} else {
				compareCards(playerOne, playerTwo, playerOneCard, playerTwoCard);
			}
		}
		return getDeckOutWinner(playerOne, playerTwo);
	}

	private static Player doCombat(Player playerOne, Player playerTwo) {
		while (!isDeckOutVictory(playerOne, playerTwo)) {
			int playerOneCard = playerOne.remove();
			int playerTwoCard = playerTwo.remove();
			compareCards(playerOne, playerTwo, playerOneCard, playerTwoCard);
		}
		return getDeckOutWinner(playerOne, playerTwo);
	}

	private static void compareCards(Player playerOne, Player playerTwo, int playerOneCard, int playerTwoCard) {
		if (playerOneCard < playerTwoCard) {
			playerTwo.add(playerTwoCard);
			playerTwo.add(playerOneCard);
		} else {
			playerOne.add(playerOneCard);
			playerOne.add(playerTwoCard);
		}
	}

	private static boolean isDeckOutVictory(Player playerOne, Player playerTwo) {
		if (playerOne.isEmpty()) {
			return true;
		} else if (playerTwo.isEmpty()) {
			return true;
		}
		return false;
	}

	private static Player getDeckOutWinner(Player playerOne, Player playerTwo) {
		if (playerOne.isEmpty()) {
			return playerTwo;
		} else if (playerTwo.isEmpty()) {
			return playerOne;
		}
		return null;
	}

	private static int getWinValue(Player winner) {
		int sum = 0;
		while (!winner.isEmpty()) {
			sum += winner.size() * winner.remove();
		}
		return sum;
	}
}
