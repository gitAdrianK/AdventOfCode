package day_16;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class day16 {

	public static void main(String[] args) throws FileNotFoundException {
		solveDay16("test_input.txt");
		solveDay16("input.txt");
	}

	public static void solveDay16(String input) throws FileNotFoundException {
		int p1 = 0;
		ArrayList<TicketRule> rules = new ArrayList<TicketRule>();
		int[] yourTicket;
		Scanner sc = new Scanner(new File(input));
		for (int i = 0; sc.hasNextLine(); i = i) {
			String line = sc.nextLine();
			// Newline
			if (line.isEmpty()) {
				i++;
				continue;
			}
			// Non number containing lines
			if (!line.matches(".*[0-9]+.*")) {
				continue;
			}
			switch (i) {
			case 0:
				// Ticket Rules
				line = line.replaceAll("[^0-9]+", " ");
				line = line.trim();
				String[] ruleStr = line.split("[^0-9]+");
				int[] ruleInt = new int[4];
				for (int j = 0; j < ruleStr.length; j++) {
					ruleInt[j] = Integer.parseInt(ruleStr[j]);
				}
				rules.add(new TicketRule(ruleInt[0], ruleInt[1], ruleInt[2], ruleInt[3]));
				break;
			case 1:
				// Your Ticket
				String[] yourTicketStr = line.split(",");
				int[] yourTicketInt = new int[yourTicketStr.length];
				for (int j = 0; j < yourTicketStr.length; j++) {
					yourTicketInt[j] = Integer.parseInt(yourTicketStr[j]);
				}
				yourTicket = yourTicketInt;
				break;
			case 2:
				// Nearby Tickets
				String[] nrbyTicketStr = line.split(",");
				int[] nrbyTicketInt = new int[nrbyTicketStr.length];
				for (int j = 0; j < nrbyTicketStr.length; j++) {
					nrbyTicketInt[j] = Integer.parseInt(nrbyTicketStr[j]);
				}
				for (int j : nrbyTicketInt) {
					boolean isValidForOne = false;
					for (TicketRule r : rules) {
						if (r.isValid(j)) {
							isValidForOne = true;
						}
					}
					if (!isValidForOne) {
						p1 += j;
					}
				}
				break;
			default:
				break;
			}
		}
		sc.close();
		System.out.println(p1);
	}
}