use std::fs;

fn main() {
    let mut valid_pw_total = 0;
    let mut valid_pw_total_p2 = 0;
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in data.lines() {
        let split_line: Vec<&str> = line.split(" ").collect();
        let pw_req_amount: Vec<&str> = split_line[0].split("-").collect();
        let pw_min_amount: u8 = pw_req_amount[0].parse().unwrap();
        let pw_max_amount: u8 = pw_req_amount[1].parse().unwrap();
        let pw_req_letter = split_line[1].chars().nth(0).unwrap();
        // Part 1
        let mut count = 0;
        for c in split_line[2].chars() {
            if c == pw_req_letter {
                count = count + 1;
            }
        }
        if pw_min_amount <= count && count <= pw_max_amount {
            valid_pw_total = valid_pw_total + 1;
        }
        // Part 2
        // Reusing pw_min_amount and pw_max_amount w/o changing the names.
        // Better names would be pw_pos_one and pw_pos_two
        if (split_line[2].chars().nth((pw_min_amount - 1).into()).unwrap() == pw_req_letter)
            ^ (split_line[2].chars().nth((pw_max_amount - 1).into()).unwrap() == pw_req_letter) {
                valid_pw_total_p2 = valid_pw_total_p2 + 1;
        }
    }
    println!("{:?}, {:?}", valid_pw_total, valid_pw_total_p2);
}
