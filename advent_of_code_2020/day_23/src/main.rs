use std::fs;

fn main() {
    assert_eq!("92658374", solve_day_23("test_input.txt", 10));
    assert_eq!("67384529", solve_day_23("test_input.txt", 100));
    println!("{:?}", solve_day_23("input.txt", 100));
}

fn solve_day_23(input: &str, turns: u8) -> String {
    let data = fs::read_to_string(input).expect("Unable to read file");
    play_game(&data.trim_end(), turns)
}

fn play_game(cups_as_str: &str, turns: u8) -> String {
    let mut cups: Vec<u8> = cups_as_str
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();
    let mut pick_up: Vec<u8> = vec![];
    for _ in 0..turns {
        let current = *cups.get(0).unwrap();
        for _ in 1..=3 {
            pick_up.push(cups.remove(1));
        }
        let mut destination = current - 1;
        while !cups.contains(&destination) {
            if destination == 0 {
                destination = 10;
            }
            destination -= 1;
        }
        let index = cups.iter().position(|&i| i == destination).unwrap();
        while !pick_up.is_empty() {
            cups.insert(index + 1, pick_up.pop().unwrap());
        }
        cups.rotate_left(1);
    }
    while *cups.first().unwrap() != 1 as u8 {
        cups.rotate_left(1);
    }
    cups.remove(0);
    let mut s = "".to_string();
    for c in cups {
        s += &c.to_string();
    }
    s
}
