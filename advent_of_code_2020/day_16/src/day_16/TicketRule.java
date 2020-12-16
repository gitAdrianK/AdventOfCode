package day_16;

import javafx.util.Pair;

public class TicketRule {
	Pair<Integer, Integer> lowerRange;
	Pair<Integer, Integer> higherRange;

	public TicketRule(int loLo, int loHi, int hiLo, int hiHi) {
		this.lowerRange = new Pair<Integer, Integer>(loLo, loHi);
		this.higherRange = new Pair<Integer, Integer>(hiLo, hiHi);
	}

	public boolean isValid(int number) {
		return (number >= lowerRange.getKey() && number <= lowerRange.getValue())
				|| (number >= higherRange.getKey() && number <= higherRange.getValue());
	}
	
	@Override
	public String toString() {
		return lowerRange.getKey() + "-" + lowerRange.getValue() + ", " + higherRange.getKey() + "-" + higherRange.getValue();
	}
}
