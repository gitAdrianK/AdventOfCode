import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class day1 {
	public static void main(String args[]) {
		List<Integer> numbers = new ArrayList<Integer>();
		// Read all numbers of the file and add them to a list
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
			String line;
			while ((line = reader.readLine()) != null) {
				numbers.add(Integer.parseInt(line));
			}
			reader.close();
		} catch (Exception e) {
			System.err.format("Exception occurred trying to read '%s'.", "input.txt");
			e.printStackTrace();
			return;
		}
		// Add all pairs of numbers together and print out the result of the
		// multiplication should the addition result in 2020
		for (int a : numbers) {
			for (int b : numbers) {
				if (a + b == 2020) {
					System.out.println(a * b);
					return;
				}
			}
		}
	}
}