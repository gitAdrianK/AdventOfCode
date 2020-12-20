package day_19;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

import javafx.util.Pair;

public class MonsterMessages {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay19("test_input.txt");
		solveDay19("test_input_2.txt");
		solveDay19("test_input_3.txt");
		solveDay19("input.txt");
		solveDay19("input_2.txt");
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void solveDay19(String input) throws FileNotFoundException {
		HashMap<Integer, Pair<String[], String[]>> rules = new HashMap<Integer, Pair<String[], String[]>>();
		ArrayList<String> startRuleArr = null;
		int valid = 0;
		Scanner sc = new Scanner(new File(input));
		for (byte i = 0; sc.hasNextLine();) {
			String line = sc.nextLine();
			// Newline
			if (line.isEmpty()) {
				i++;
				continue;
			}
			switch (i) {
			case 0:
				String[] ruleSplitAtColon = line.split(":");
				int ruleNr = Integer.parseInt(ruleSplitAtColon[0]);
				if (ruleSplitAtColon[1].contains("\"")) {
					ruleSplitAtColon[1] = ruleSplitAtColon[1].replaceAll("[^a-z]", "");
					String[] terminatingSymbol = new String[1];
					terminatingSymbol[0] = ruleSplitAtColon[1];
					rules.put(ruleNr, new Pair(terminatingSymbol, null));
					break;
				}
				ruleSplitAtColon[1] = ruleSplitAtColon[1].trim();
				String left = null;
				String right = null;
				if (ruleSplitAtColon[1].contains("|")) {
					String[] ruleSplitAtPipe = ruleSplitAtColon[1].split("\\|");
					left = ruleSplitAtPipe[0].trim();
					right = ruleSplitAtPipe[1].trim();
				} else {
					left = ruleSplitAtColon[1];
				}
				String[] leftSplit = null;
				String[] rightSplit = null;
				if (left != null) {
					if (left.contains(" ")) {
						leftSplit = left.split(" ");
					} else {
						leftSplit = new String[1];
						leftSplit[0] = left;
					}
				}
				if (right != null) {
					if (right.contains(" ")) {
						rightSplit = right.split(" ");
					} else {
						rightSplit = new String[1];
						rightSplit[0] = right;
					}
				}
				rules.put(ruleNr, new Pair(leftSplit, rightSplit));
				break;
			case 1:
				String[] startRule = rules.get(0).getKey();
				startRuleArr = new ArrayList<String>(Arrays.asList(startRule));
				startRuleArr.ensureCapacity(30);
				i++;
			case 2:
				if (isValid(rules, startRuleArr, line)) {
					valid++;
				}
				break;
			default:
				break;
			}
		}
		sc.close();
//		for (Map.Entry<Integer, Pair<String[], String[]>> e : rules.entrySet()) {
//			Pair<String[], String[]> p = e.getValue();
//			System.out.println(e.getKey() + ": " + Arrays.toString(p.getKey()) + " | " + Arrays.toString(p.getValue()));
//		}
		System.out.println(input + " - " + valid);
	}

	private static boolean isValid(HashMap<Integer, Pair<String[], String[]>> rules, ArrayList<String> start, String cmpTo) {
		boolean isValid = false;
		//System.out.println(start + " " + cmpTo);
		if(start.size() > cmpTo.length()) {
			return false;
		}
		int skip = 0;
		for(String s : start) {
			if (s.matches("[ab]")) {
				if (s.charAt(0) != cmpTo.charAt(skip)) {
					return false;
				}
				skip++;
			} else {
				break;
			}
		}
		if (skip >= start.size()) {
			StringBuilder builder = new StringBuilder();
			for(String s: start) {
				builder.append(s);
			}
			return cmpTo.equals(builder.toString());
		}
		Pair<String[], String[]> pair = rules.get(Integer.parseInt(start.get(skip)));
		String[] leftReplacement = pair.getKey();
		String[] rightReplacement = pair.getValue();
		@SuppressWarnings("unchecked")
		ArrayList<String> startLeft = (ArrayList<String>) start.clone();
		@SuppressWarnings("unchecked")
		ArrayList<String> startRight = (ArrayList<String>) start.clone();
		if (leftReplacement != null) {
			boolean hasReplaced = false;
			for (int i = 0; i < leftReplacement.length; i++) {
				if (!hasReplaced) {
					startLeft.set(skip, leftReplacement[i]);
					hasReplaced = true;
				} else {
					startLeft.add(skip + i, leftReplacement[i]);
				}
			}
			isValid |= isValid(rules, startLeft, cmpTo);
		}
		if (rightReplacement != null) {
			boolean hasReplaced = false;
			for (int i = 0; i < rightReplacement.length; i++) {
				if (!hasReplaced) {
					startRight.set(skip, rightReplacement[i]);
					hasReplaced = true;
				} else {
					startRight.add(skip + i, rightReplacement[i]);
				}
			}
			isValid |= isValid(rules, startRight, cmpTo);
		}
		return isValid;
	}
}
