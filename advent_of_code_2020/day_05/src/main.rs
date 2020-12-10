use std::fs;

fn main() {
    let mut seats: Vec<u32> = Vec::new();
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for input in data.lines() {
        let id = find_seat_id(input);
        seats.push(id);
    }
    seats.sort();
    println!("Highest Id: {}", seats.last().unwrap());
    let mut my_seat = *seats.first().clone().unwrap();
    for &seat in seats.iter() {
        if seat != my_seat {
            break
        }
        my_seat = my_seat + 1;
    }
    println!("My seat: {}", my_seat);
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
