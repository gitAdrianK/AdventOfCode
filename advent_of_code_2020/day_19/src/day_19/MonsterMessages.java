package day_19;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Scanner;
import java.util.stream.Collectors;

import javafx.util.Pair;

public class MonsterMessages {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay19("test_input.txt");
		solveDay19("input.txt");
	}

	@SuppressWarnings({ "rawtypes", "unchecked" })
	public static void solveDay19(String input) throws FileNotFoundException {
		HashMap<Integer, Pair<String[], String[]>> rules = new HashMap<Integer, Pair<String[], String[]>>();
		ArrayList<String> possible = new ArrayList<String>();
		int p1 = 0;
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
				ArrayList<String> startRuleArr = new ArrayList<String>(Arrays.asList(startRule));
				possible = createOptions(rules, startRuleArr, 0);
				possible.sort(Comparator.comparingInt(String::length));
				//System.out.println(possible);
				i++;
			case 2:
				int inputLen = line.length();
				for (String s : possible) {
					if (s.length() < inputLen) {
						continue;
					}
					if (s.length() > inputLen) {
						break;
					}
					//System.out.println("s: " + s + ", in: " + line + ", cmp: " + line.equals(s));
					if (s.equals(line)) {
						p1++;
					}
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
		System.out.println(p1 + " " + 0);
	}

	// TODO: Steal a parser because this is SLOW
	private static ArrayList<String> createOptions(HashMap<Integer, Pair<String[], String[]>> rules,
			ArrayList<String> start, int startIndex) {
		ArrayList<String> options = new ArrayList<String>();
		//System.out.println("start: " + start);
		for (int i = startIndex; i < start.size(); i++) {
			String curr = start.get(i);
			Pair<String[], String[]> pair = rules.get(Integer.parseInt(curr));
			String[] left = pair.getKey();
			if (left != null) {
				boolean replacementWasTerminator = false;
				boolean hasReplaced = false;
				@SuppressWarnings("unchecked")
				ArrayList<String> newStart = (ArrayList<String>) start.clone();
				for (String next : left) {
					if (next.matches("[^0-9]+")) {
						start.set(i, next);
						replacementWasTerminator = true;
						break;
					} else {
						if (!hasReplaced) {
							newStart.set(i, next);
							hasReplaced = true;
						} else {
							newStart.add(i + 1, next);
						}
					}
				}
				if (!replacementWasTerminator) {
					//System.out.println("new left: " + newStart);
					options.addAll(createOptions(rules, newStart, i));
				}
			}
			String[] right = pair.getValue();
			if (right != null) {
				boolean replacementWasTerminator = false;
				boolean hasReplaced = false;
				@SuppressWarnings("unchecked")
				ArrayList<String> newStart = (ArrayList<String>) start.clone();
				for (String next : right) {
					if (next.matches("[^0-9]+")) {
						start.set(i, next);
						replacementWasTerminator = true;
						break;
					} else {
						if (!hasReplaced) {
							newStart.set(i, next);
							hasReplaced = true;
						} else {
							newStart.add(i + 1, next);
						}
					}
				}
				if (!replacementWasTerminator) {
					//System.out.println("new right: " + newStart);
					options.addAll(createOptions(rules, newStart, i));
				}
			}
		}
		StringBuilder builder = new StringBuilder();
		for (String s : start) {
			builder.append(s);
		}
		options.add(builder.toString());
		ArrayList<String> filtered = (ArrayList<String>) options.stream().filter(opt -> !opt.matches(".*[0-9].*")).collect(Collectors.toList());
		return filtered;
	}
}
