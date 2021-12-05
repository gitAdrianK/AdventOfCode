use std::collections::HashMap;
use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let mut positions: HashMap<(u32, u32), u32> = HashMap::new();
    for line in data.lines() {
        let from_to_split: Vec<&str> = line.split(" -> ").collect();
        let from: Vec<u32> = from_to_split
            .get(0)
            .unwrap()
            .split(',')
            .map(|x| x.parse::<u32>().unwrap())
            .collect();
        let to: Vec<u32> = from_to_split
            .get(1)
            .unwrap()
            .split(',')
            .map(|x| x.parse::<u32>().unwrap())
            .collect();
        // X equal
        if from.get(0).unwrap() == to.get(0).unwrap() {
            let x = *from.get(0).unwrap();
            // Cant be bothered to compare whats smaller/bigger
            for n in *from.get(1).unwrap()..=*to.get(1).unwrap() {
                let value = positions.entry((x, n)).or_insert(0);
                *value += 1;
            }
            for n in *to.get(1).unwrap()..=*from.get(1).unwrap() {
                let value = positions.entry((x, n)).or_insert(0);
                *value += 1;
            }
        }
        // Y equal
        if from.get(1).unwrap() == to.get(1).unwrap() {
            let y = *from.get(1).unwrap();
            // Cant be bothered to compare whats smaller/bigger
            for n in *from.get(0).unwrap()..=*to.get(0).unwrap() {
                let value = positions.entry((n, y)).or_insert(0);
                *value += 1;
            }
            for n in *to.get(0).unwrap()..=*from.get(0).unwrap() {
                let value = positions.entry((n, y)).or_insert(0);
                *value += 1;
            }
        }
    }
    println!("{:?}", positions.values().filter(|x| **x > 1).count());
}

#[allow(dead_code)]
fn print_positions(positions: &HashMap<(u32, u32), u32>) {
    let mut highest_x = 0;
    let mut highest_y = 0;
    for pos in positions.keys() {
        if pos.0 > highest_x {
            highest_x = pos.0;
        }
        if pos.1 > highest_y {
            highest_y = pos.1;
        }
    }
    for i in 0..=highest_x {
        for j in 0..=highest_y {
            if positions.contains_key(&(i, j)) {
                print!("{:2?}", positions.get(&(i, j)).unwrap());
            } else {
                print!(" .");
            }
        }
        println!();
    }
}
