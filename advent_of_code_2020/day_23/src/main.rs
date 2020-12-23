use std::collections::HashMap;
use std::fs;

fn main() {
    let start = &get_input("test_input.txt");
    assert_eq!("92658374", play_game(start, 10));
    assert_eq!("67384529", play_game(start, 100));
    assert_eq!(149245887792, play_big_boy_game(start));
    let start = &get_input("input.txt");
    println!("Part 1: {}", play_game(start, 100));
    println!("Part 2: {}", play_big_boy_game(start));
}

fn get_input(input: &str) -> String {
    let data = fs::read_to_string(input).expect("Unable to read file");
    data.trim_end().to_string()
}

fn play_game(cups_as_str: &str, turns: u8) -> String {
    let cups: Vec<u8> = cups_as_str
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();
    let mut map: HashMap<u8, u8> = HashMap::new();
    for (i, cup) in cups.iter().enumerate() {
        let next = (i + 1) % cups.len();
        map.insert(*cup, *cups.get(next).unwrap());
    }
    let mut current = *cups.first().unwrap();
    for _ in 0..turns {
        // Triple
        let start_triple = *map.get(&current).unwrap();
        let mid_triple = *map.get(&start_triple).unwrap();
        let end_triple = *map.get(&mid_triple).unwrap();
        // After trip
        let after_trip = *map.get(&end_triple).unwrap();
        // Destination
        let pick_up = vec![start_triple, mid_triple, end_triple];
        let mut destination = current - 1;
        while pick_up.contains(&destination) || destination == 0 {
            if destination == 0 {
                destination = cups.len() as u8 + 1;
            }
            destination -= 1;
        }
        // After destination
        let after_destination = *map.get(&destination).unwrap();
        // Shuffling around
        map.insert(current, after_trip);
        map.insert(destination, start_triple);
        map.insert(end_triple, after_destination);
        current = after_trip;
    }
    let mut next = *map.get(&1).unwrap();
    let mut s = "".to_string();
    while next != 1 {
        s += &next.to_string();
        next = *map.get(&next).unwrap();
    }
    s
}

fn play_big_boy_game(cups_as_str: &str) -> u128 {
    let mut cups: Vec<u32> = cups_as_str
        .chars()
        .map(|c| c.to_digit(10).unwrap() as u32)
        .collect();
    for n in (cups.len() + 1)..=1_000_000 {
        cups.push(n as u32);
    }
    let mut map: HashMap<u32, u32> = HashMap::new();
    for (i, cup) in cups.iter().enumerate() {
        let next = (i + 1) % cups.len();
        map.insert(*cup, *cups.get(next).unwrap());
    }
    let mut current = *cups.first().unwrap();
    for _ in 0..10_000_000 {
        // Triple
        let start_triple = *map.get(&current).unwrap();
        let mid_triple = *map.get(&start_triple).unwrap();
        let end_triple = *map.get(&mid_triple).unwrap();
        // After trip
        let after_trip = *map.get(&end_triple).unwrap();
        // Destination
        let pick_up = vec![start_triple, mid_triple, end_triple];
        let mut destination = current - 1;
        while pick_up.contains(&destination) || destination == 0 {
            if destination == 0 {
                destination = cups.len() as u32 + 1;
            }
            destination -= 1;
        }
        let after_destination = *map.get(&destination).unwrap();
        map.insert(current, after_trip);
        map.insert(destination, start_triple);
        map.insert(end_triple, after_destination);
        current = after_trip;
    }
    let next = *map.get(&1).unwrap();
    let next_after = *map.get(&next).unwrap();
    next as u128 * next_after as u128
}
