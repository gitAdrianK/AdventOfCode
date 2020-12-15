use std::fs;

fn main() {
    let mut seats: Vec<u32> = Vec::new();
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for input in data.lines() {
        seats.push(find(&input[..7], 0, 127) * 8 + find(&input[7..input.len()], 0, 7));
    }
    seats.sort();
    let mut my_seat = *seats.first().unwrap();
    for &seat in seats.iter() {
        if seat != my_seat { break }
        my_seat += 1;
    }
    println!("Highest Id: {} \nMy seat: {}", seats.last().unwrap(), my_seat);
}

fn find(input: &str, lo: u32, hi: u32) -> u32 {
    let (mut hi, mut lo, mut step) = (hi, lo, hi / 2);
    for c in input.chars() {
        match c {
            'F' | 'L' => hi = hi - step - 1,
            'B' | 'R' => lo = lo + step + 1,
            _ => unreachable!(),
        }
        step = step / 2;
    }
    hi
}
