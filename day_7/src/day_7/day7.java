package day_7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class day7 {
	public static void main(String args[]) {
		HashMap<String, ArrayList<String>> bagRules = new HashMap<String, ArrayList<String>>();
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
				String outerBag = splitLine[0] + " " + splitLine[1];
				splitLine = Arrays.copyOfRange(splitLine, 2, splitLine.length);
				ArrayList<String> innerSplit = new ArrayList<String>();
				for (String s : splitLine) {
					if (!s.matches(".*bag.*|[0-9]|contain")) {
						innerSplit.add(s);
					}
				}
				ArrayList<String> innerBags = new ArrayList<String>();
				for (int i = 0; i < innerSplit.size(); i += 2) {
					innerBags.add(innerSplit.get(i) + " " + innerSplit.get(i + 1));
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
		for (Map.Entry<String, ArrayList<String>> kv : bagRules.entrySet()) {
			// Initial fill
			for (String s : kv.getValue()) {
				toCheckBags.push(s);
			}
			while (!toCheckBags.isEmpty()) {
				String current = toCheckBags.pop();
				if (current.equals("shiny gold")) {
					shinyGoldOutsideOptions++;
					toCheckBags.clear();
					break;
				}
				if (bagRules.containsKey(current)) {
					for (String s : bagRules.get(current)) {
						toCheckBags.push(s);
					}
				}
			}
		}
		System.out.println(shinyGoldOutsideOptions);
	}
}
