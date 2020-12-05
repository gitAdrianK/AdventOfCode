use std::fs;

fn main() {
    let mut highest_id = 0;
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for input in data.lines() {
        let id = find_seat_id(input);
        if id > highest_id {
            highest_id = id;
        }
    }
    println!("{}", highest_id)
}

fn find_seat_id(input: &str) -> u32 {
    fn find_binarily(input: &str, lower_bound: u32, upper_bound: u32) -> u32 {
        let character = match input.chars().nth(0) {
            Some(character) => character,
            None => return upper_bound,
        };
        let diff = (upper_bound - lower_bound) / 2;
        match character {
            'F' | 'L' => {
                return find_binarily(&input[1..], lower_bound, upper_bound - diff - 1)
            },
            'B' | 'R' => {
                return find_binarily(&input[1..], lower_bound + diff + 1, upper_bound)
            },
            _ => unreachable!(),
        }
    }
    return find_binarily(&input[..7], 0, 127) * 8 + find_binarily(&input[7..input.len()], 0, 7)
}
