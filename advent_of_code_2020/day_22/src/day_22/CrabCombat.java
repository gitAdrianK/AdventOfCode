package day_22;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayDeque;
import java.util.Scanner;

public class CrabCombat {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay22("test_input.txt");
		solveDay22("input.txt");
	}

	public static void solveDay22(String input) throws FileNotFoundException {
		ArrayDeque<Integer> player1 = new ArrayDeque<Integer>();
		ArrayDeque<Integer> player2 = new ArrayDeque<Integer>();
		boolean isPlayer1 = true;
		Scanner sc = new Scanner(new File(input));
		while (sc.hasNextLine()) {
			String line = sc.nextLine();
			if (line.contains("Player")) {
				continue;
			}
			if (line.isEmpty()) {
				isPlayer1 = false;
				continue;
			}
			int card = Integer.parseInt(line);
			if (isPlayer1) {
				player1.add(card);
			} else {
				player2.add(card);
			}
		}
		sc.close();
		while (!player1.isEmpty() && !player2.isEmpty()) {
			int p1Card = player1.remove();
			int p2Card = player2.remove();
			if (p1Card < p2Card) {
				player2.add(p2Card);
				player2.add(p1Card);
			} else {
				player1.add(p1Card);
				player1.add(p2Card);
			}
		}
		int sum = 0;
		if (player1.isEmpty()) {
			while (!player2.isEmpty()) {
				sum += player2.size() * player2.remove();
			}
		} else {
			while (!player1.isEmpty()) {
				sum += player1.size() * player1.remove();
			}
		}
		System.out.println(input + ": " + sum);
	}

}
