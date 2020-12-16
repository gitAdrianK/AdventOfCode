package day_16;

import java.util.Comparator;

import javafx.util.Pair;

public class TicketRule {
	private String name;
	private Pair<Integer, Integer> lowerRange;
	private Pair<Integer, Integer> higherRange;

	public TicketRule(String name, int loLo, int loHi, int hiLo, int hiHi) {
		this.name = name;
		this.lowerRange = new Pair<Integer, Integer>(loLo, loHi);
		this.higherRange = new Pair<Integer, Integer>(hiLo, hiHi);
	}

	public boolean isValid(int number) {
		return (number >= lowerRange.getKey() && number <= lowerRange.getValue())
				|| (number >= higherRange.getKey() && number <= higherRange.getValue());
	}

	public boolean isValidForAll(int[] numbers) {
		for (int n : numbers) {
			if (!isValid(n)) {
				return false;
			}
		}
		return true;
	}

	public String getName() {
		return name;
	}

	@Override
	public String toString() {
		return name;
	}
	
//	@Override
//	public String toString() {
//		return name + ": " + lowerRange.getKey() + "-" + lowerRange.getValue() + ", " + higherRange.getKey() + "-"
//				+ higherRange.getValue();
//	}
}

class NameCompare implements Comparator<TicketRule> {
	public int compare(TicketRule t1, TicketRule t2) {
		return t1.getName().compareTo(t2.getName());
	}
}
