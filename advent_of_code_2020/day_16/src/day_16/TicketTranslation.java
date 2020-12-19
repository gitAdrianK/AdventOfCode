package day_16;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TicketTranslation {

	public static void main(String[] args) throws FileNotFoundException {
		// solveDay16("test_input.txt");
		// solveDay16("test_input_2.txt");
		solveDay16("input.txt");
	}

	public static void solveDay16(String input) throws FileNotFoundException {
		int p1 = 0;

		// Rules and tickets
		ArrayList<TicketRule> rules = new ArrayList<TicketRule>();
		int[] yourTicket = null;
		ArrayList<int[]> nearbyTickets = new ArrayList<int[]>();

		Scanner sc = new Scanner(new File(input));
		for (int i = 0; sc.hasNextLine();) {
			String line = sc.nextLine();
			// Newline & Non number containing lines
			if (!line.matches(".*[0-9]+.*")) {
				i++;
				continue;
			}
			switch (i) {
			case 0:
				// Ticket Rules
				String name = line.replaceAll(":.*", "");
				line = line.replaceAll("[^0-9]+", " ");
				line = line.trim();
				String[] ruleStr = line.split("[^0-9]+");
				int[] ruleInt = new int[4];
				for (int j = 0; j < ruleStr.length; j++) {
					ruleInt[j] = Integer.parseInt(ruleStr[j]);
				}
				rules.add(new TicketRule(name, ruleInt[0], ruleInt[1], ruleInt[2], ruleInt[3]));
				break;
			case 2:
				// Your Ticket
				yourTicket = parseTicket(line);
				break;
			case 4:
				// Nearby Tickets
				int[] ticket = parseTicket(line);
				int errorValue = solvePart1(rules, ticket);
				if (errorValue == -1) {
					nearbyTickets.add(ticket);
				} else {
					p1 += errorValue;
				}
				break;
			default:
				break;
			}
		}
		sc.close();
		long p2 = solvePart2(rules, nearbyTickets, yourTicket);
		System.out.println(p1 + " " + p2);
	}

	private static int solvePart1(List<TicketRule> rules, int[] nrbyTicketInt) {
		for (int j : nrbyTicketInt) {
			boolean isValidForOne = false;
			for (TicketRule r : rules) {
				if (r.isValid(j)) {
					isValidForOne = true;
				}
			}
			if (!isValidForOne) {
				return j;
			}
		}
		return -1;
	}

	private static long solvePart2(List<TicketRule> rules, List<int[]> nearbyTickets, int[] yourTicket) {
		ArrayList<ArrayList<TicketRule>> allPossible = new ArrayList<ArrayList<TicketRule>>();
		int[] column = new int[nearbyTickets.size() + 1];
		for (int i = 0; i < yourTicket.length; i++) {
			column[0] = yourTicket[i];
			int index = 1;
			for (int[] nearbyTicket : nearbyTickets) {
				column[index] = nearbyTicket[i];
				index++;
			}
			ArrayList<TicketRule> possible = new ArrayList<TicketRule>();
			for (TicketRule rule : rules) {
				if (rule.isValidForAll(column)) {
					possible.add(rule);
				}
			}
			allPossible.add(possible);
		}
		TicketRule[] assigned = eliminateOptions(allPossible);
		long p2 = 1;
		for(int i = 0; i < assigned.length; i++) {
			if (assigned[i].getName().contains("departure")) {
				p2 *= yourTicket[i];
			}
		}
		return p2;
	}

	private static int[] parseTicket(String line) {
		String[] ticketStr = line.split(",");
		int[] ticketInt = new int[ticketStr.length];
		for (int j = 0; j < ticketStr.length; j++) {
			ticketInt[j] = Integer.parseInt(ticketStr[j]);
		}
		return ticketInt;
	}

	private static TicketRule[] eliminateOptions(ArrayList<ArrayList<TicketRule>> list) {
		return eliminateOptions(list, new TicketRule[list.size()]);
	}

	private static TicketRule[] eliminateOptions(ArrayList<ArrayList<TicketRule>> list, TicketRule[] assigned) {
		TicketRule onlyRule = null;
		for (int i = 0; i < list.size(); i++) {
			if (list.get(i).size() == 1) {
				onlyRule = list.get(i).get(0);
				assigned[i] = onlyRule;
			}
		}
		if (onlyRule == null) {
			return assigned;
		}
		for (List<TicketRule> entry : list) {
			entry.remove(onlyRule);
		}
		return eliminateOptions(list, assigned);
	}
}
