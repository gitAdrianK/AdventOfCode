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
					if (isValidPassport(currentPassport)) {
						validPassports++;
					}
					currentPassport = "";
				} else {
					currentPassport += line + " ";
				}
			}
			// Bcs the terminating newline is already null to the reader we have
			// one last password to check
			if (isValidPassport(currentPassport)) {
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

	private static boolean isValidPassport(String passport) {
		// Required fields validation
		if (!passport.contains("byr") || !passport.contains("iyr") || !passport.contains("eyr")
				|| !passport.contains("hgt") || !passport.contains("hcl") || !passport.contains("ecl")
				|| !passport.contains("pid")) {
			return false;
		}
		String[] fields = passport.split(" ");
		for (String field : fields) {
			String[] fieldSplit = field.split(":");
			// Birth year validation
			if (fieldSplit[0].equals("byr")) {
				int birYr = Integer.parseInt(fieldSplit[1]);
				if (birYr < 1920 || birYr > 2002) {
					return false;
				}
			}
			// Issue year validation
			if (fieldSplit[0].equals("iyr")) {
				int issYr = Integer.parseInt(fieldSplit[1]);
				if (issYr < 2010 || issYr > 2020) {
					return false;
				}
			}
			// Expiration year validation
			if (fieldSplit[0].equals("eyr")) {
				if (fieldSplit[1].length() != 4) {
					return false;
				}
				int expYr = Integer.parseInt(fieldSplit[1]);
				if (expYr < 2020 || expYr > 2030) {
					return false;
				}
			}
			// Height validation
			if (fieldSplit[0].equals("hgt")) {
				if(fieldSplit[1].length() <= 2){
					return false;
				}
				int height = Integer.parseInt(fieldSplit[1].substring(0, fieldSplit[1].length() - 2));
				if (fieldSplit[1].contains("cm")) {
					if (height < 150 || height > 193) {
						return false;
					}
				} else {
					if (height < 59 || height > 76) {
						return false;
					}
				}
			}
			// Hair colour validation
			if (fieldSplit[0].equals("hcl")) {
				if (!fieldSplit[1].matches("^#([a-f0-9]{6})$")) {
					return false;
				}
			}
			// Eye colour validation
			if (fieldSplit[0].equals("ecl")) {
				if (!fieldSplit[1].matches("amb|blu|brn|gry|grn|hzl|oth")) {
					return false;
				}
			}
			// Passport ID validation
			if (fieldSplit[0].equals("pid")) {
				if (!fieldSplit[1].matches("^[0-9]{9}$")) {
					return false;
				}	
			}
		}
		return true;
	}
}
