package day_7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

import javafx.util.Pair;

public class day7 {
	public static void main(String args[]) {
		// This got rather lengthy and overly complicated
		HashMap<String, ArrayList<Pair<Integer, String>>> bagRules = new HashMap<String, ArrayList<Pair<Integer, String>>>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
			String line;
			while ((line = reader.readLine()) != null) {
				if (line.contains("no other")) {
					// Bags containing no other bags are dead ends
					// We can either add them as <key><empty array list>
					// or not at all like this
					continue;
				}
				String[] splitLine = line.split(" ");
				// The first two words describe the outer bag
				String outerBag = splitLine[0] + " " + splitLine[1];
				splitLine = Arrays.copyOfRange(splitLine, 2, splitLine.length);
				ArrayList<String> innerSplit = new ArrayList<String>();
				for (String s : splitLine) {
					if (!s.matches(".*bag.*|contain")) {
						innerSplit.add(s);
					}
				}
				int innerAmount = 0;
				// Inner bags are similar to outer bags but have an additional
				// amount information at the front
				ArrayList<Pair<Integer, String>> innerBags = new ArrayList<Pair<Integer, String>>();
				for (int i = 0; i < innerSplit.size(); i += 3) {
					innerAmount = Integer.parseInt(innerSplit.get(i));
					innerBags.add(new Pair<Integer, String>(innerAmount,
							innerSplit.get(i + 1) + " " + innerSplit.get(i + 2)));
				}
				bagRules.put(outerBag, innerBags);
			}
			reader.close();
		} catch (Exception e) {
			System.err.format("Exception occurred trying to read '%s'.", "input.txt");
			e.printStackTrace();
			return;
		}
		// The amount of outer bag options that can contain a gold bag
		int shinyGoldOutsideOptions = 0;
		Stack<String> toCheckBags = new Stack<String>();
		for (Map.Entry<String, ArrayList<Pair<Integer, String>>> kv : bagRules.entrySet()) {
			// Initial fill
			for (Pair<Integer, String> pair : kv.getValue()) {
				toCheckBags.push(pair.getValue());
			}
			while (!toCheckBags.isEmpty()) {
				String current = toCheckBags.pop();
				if (current.equals("shiny gold")) {
					shinyGoldOutsideOptions++;
					toCheckBags.clear();
					break;
				}
				if (bagRules.containsKey(current)) {
					ArrayList<Pair<Integer, String>> list = bagRules.get(current);
					for (Pair<Integer, String> pair : list) {
						toCheckBags.push(pair.getValue());
					}
				}
			}
		}
		System.out.println(shinyGoldOutsideOptions);
		// The amount of bags contained in one shiny golden bag
		int shinyGoldContainsBags = 0;
		if (bagRules.containsKey("shiny gold")) {
			// Initial fill
			for (Pair<Integer, String> pair : bagRules.get("shiny gold")) {
				shinyGoldContainsBags += pair.getKey();
				for (int i = 0; i < pair.getKey(); i++) {
					toCheckBags.push(pair.getValue());
				}
			}
			while (!toCheckBags.empty()) {
				String current = toCheckBags.pop();
				if (bagRules.containsKey(current)) {
					ArrayList<Pair<Integer, String>> list = bagRules.get(current);
					for (Pair<Integer, String> pair : list) {
						shinyGoldContainsBags += pair.getKey();
						for (int i = 0; i < pair.getKey(); i++) {
							toCheckBags.push(pair.getValue());
						}
					}
				}
			}
		}
		System.out.println(shinyGoldContainsBags);
	}
}
