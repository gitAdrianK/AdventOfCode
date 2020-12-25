package day_25;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ComboBreaker {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay25("test_input.txt");
		solveDay25("input.txt");
	}

	public static void solveDay25(String input) throws FileNotFoundException {
		Scanner sc = new Scanner(new File(input));
		int cardPubKey = sc.nextInt();
		int doorPubKey = sc.nextInt();
		sc.close();
		long cardLoopSize = getLoopSize(cardPubKey);
		long doorLoopSize = getLoopSize(doorPubKey);	
		long cardPrivateKey = 1;
		for (long i = 0; i < doorLoopSize; i++) {
			cardPrivateKey = transformNumber(cardPrivateKey, cardPubKey);
		}
		
		long doorPrivateKey = 1;
		for (long i = 0; i < cardLoopSize; i++) {
			doorPrivateKey = transformNumber(doorPrivateKey, doorPubKey);
		}
		if (cardPrivateKey != doorPrivateKey) {
			System.out.println("The programs internal arbitrary upper limit wasn't high enough, tough luck buddy!");
		} else {
			System.out.println("Encryption key: " + cardPrivateKey);	
		}
	}

	// Completely arbitrary upper limit
	final static long UPPER_LIMIT = 20_000_000;

	public static long getLoopSize(int key) {
		for (long subjectNr = 1; subjectNr < UPPER_LIMIT; subjectNr++) {
			long value = 1;
			for (long loopSize = 1; loopSize < UPPER_LIMIT; loopSize++) {
				value = transformNumber(value, subjectNr);
				if (value == key) {
					return loopSize;
				}
			}
		}
		return -1;
	}

	public static long transformNumber(long value, long subjectNr) {
		value *= subjectNr;
		value %= 20201227;
		return value;
	}
}
