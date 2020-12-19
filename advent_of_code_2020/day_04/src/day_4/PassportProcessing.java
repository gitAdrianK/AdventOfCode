package day_4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class PassportProcessing {

	public static void main(String[] args) throws FileNotFoundException {		
		int p1 = 0;
		int p2 = 0;
		Scanner sc = new Scanner(new File("input.txt"));
		sc.useDelimiter("\n\n");
		while(sc.hasNext()) {
			String pp = sc.next().replace("\n", " ");
			if (isValidPassport1(pp)) {
				p1++;
				if(isValidPassport2(pp)) {
					p2++;
				}
			}
		}
		sc.close();
		System.out.println(p1 + " " + p2);
	}

	private static boolean isValidPassport1(String passport) {
		return passport.contains("byr")
				&& passport.contains("iyr")
				&& passport.contains("eyr")
				&& passport.contains("hgt")
				&& passport.contains("hcl")
				&& passport.contains("ecl")
				&& passport.contains("pid");
	}
	
	private static boolean isValidPassport2(String passport) {
		return passport.matches(".*byr:(192[0-9]|19[3-9][0-9]|200[0-2])( |$).*")
				&& passport.matches(".*iyr:(201[0-9]|2020)( |$).*")
				&& passport.matches(".*eyr:(202[0-9]|2030)( |$).*")
				&& passport.matches(".*hgt:(((15[0-9]|1[6-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))( |$).*")
				&& passport.matches(".*hcl:(#[a-f0-9]{6})( |$).*")
				&& passport.matches(".*ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$).*")
				&& passport.matches(".*pid:([0-9]{9})( |$).*");
	}
}
