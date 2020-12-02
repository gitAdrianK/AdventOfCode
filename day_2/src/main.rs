use std::fs;

fn main() {
    let mut valid_pw_total = 0;
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in data.lines() {
        let split_line: Vec<&str> = line.split(" ").collect();
        let pw_req_amount: Vec<&str> = split_line[0].split("-").collect();
        let pw_min_amount: u8 = pw_req_amount[0].parse().unwrap();
        let pw_max_amount: u8 = pw_req_amount[1].parse().unwrap();
        let pw_req_letter = split_line[1].chars().nth(0).unwrap();
        let mut count = 0;
        for c in split_line[2].chars() {
            if c == pw_req_letter {
                count = count + 1;

            }
        }
        if pw_min_amount <= count && count <= pw_max_amount {
            valid_pw_total = valid_pw_total + 1;
        }
    }
    println!("{:?}", valid_pw_total);
}
