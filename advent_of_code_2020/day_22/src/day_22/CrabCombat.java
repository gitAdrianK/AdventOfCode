package day_22;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Scanner;

public class CrabCombat {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay22("test_input.txt");
		// Don't run this for part 1 combat
		solveDay22("test_input_2.txt");
		solveDay22("input.txt");
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
		//System.out.println(getWinValue(doCombat(playerOne.subdeckPlayer(), playerTwo.subdeckPlayer())));
		System.out.println(getWinValue(doRecursiveCombat(playerOne.subdeckPlayer(), playerTwo.subdeckPlayer())));
	}

	private static Player doRecursiveCombat(Player playerOne, Player playerTwo) {
		ArrayList<ArrayDeque<Integer>> playerOnePrevious = new ArrayList<ArrayDeque<Integer>>();
		ArrayList<ArrayDeque<Integer>> playerTwoPrevious = new ArrayList<ArrayDeque<Integer>>();
		while (!isDeckOutVictory(playerOne, playerTwo)) {
			for (int i = 0; i < playerOnePrevious.size(); i++) {
				ArrayDeque<Integer> prevOne = playerOnePrevious.get(i).clone();
				ArrayDeque<Integer> prevTwo = playerTwoPrevious.get(i).clone();
				if (prevOne.size() != playerOne.getCards().size() && prevTwo.size() != playerTwo.getCards().size()) {
					continue;
				}
				ArrayDeque<Integer> currOne = playerOne.getCards().clone();
				ArrayDeque<Integer> currTwo = playerTwo.getCards().clone();
				compare: while (!prevOne.isEmpty()) {
					while (!prevTwo.isEmpty()) {
						if (prevTwo.remove() != currTwo.remove()) {
							break compare;
						}
					}
					if (prevOne.remove() != currOne.remove()) {
						break;
					}
					return playerOne;
				}
			}
			playerOnePrevious.add(playerOne.getCards().clone());
			playerTwoPrevious.add(playerTwo.getCards().clone());
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
