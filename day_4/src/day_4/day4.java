package day_4;

import java.io.BufferedReader;
import java.io.FileReader;

public class day4 {

	public static void main(String[] args) {
		int validPassports = 0;
		String currentPassport = "";
		try {
			BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
			String line;
			while ((line = reader.readLine()) != null) {
				if (line.isEmpty()) {
					// Evaluate presence of all required fields
					if (validatePassport(currentPassport)) {
						validPassports++;
					}
					currentPassport = "";
				} else {
					currentPassport += line + " ";
				}
			}
			// Bcs the terminating newline is already null to the reader we have one last password to check
			if (validatePassport(currentPassport)) {
				validPassports++;
			}
			currentPassport = "";
			reader.close();
		} catch (Exception e) {
			System.err.format("Exception occurred trying to read '%s'.", "input.txt");
			e.printStackTrace();
			return;
		}
		System.out.println(validPassports);
	}

	private static boolean validatePassport(String passport) {
		if (passport.contains("byr") && passport.contains("iyr") && passport.contains("eyr") && passport.contains("hgt")
				&& passport.contains("hcl") && passport.contains("ecl") && passport.contains("pid")) {
			return true;
		}
		return false;
	}
}
