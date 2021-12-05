use std::collections::HashMap;
use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let mut positions: HashMap<(i32, i32), u32> = HashMap::new();
    for line in data.lines() {
        let from_to_split: Vec<&str> = line.split(" -> ").collect();
        let mut from: Vec<i32> = from_to_split
            .get(0)
            .unwrap()
            .split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        let to: Vec<i32> = from_to_split
            .get(1)
            .unwrap()
            .split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
        // Determine growth -1, 0 or 1 for x and y
        // e.g. 0,9 -> 5,9 => 1,0 per step
        //      8,0 -> 0,8 => -1,1 per step
        let x_diff = *to.get(0).unwrap() - *from.get(0).unwrap();
        let mut x_range: Vec<i32> = vec![-1, 1, x_diff.into()];
        x_range.sort();
        let x_change = x_range.get(1).unwrap();
        let y_diff = *to.get(1).unwrap() - *from.get(1).unwrap();
        let mut y_range: Vec<i32> = vec![-1, 1, y_diff.into()];
        y_range.sort();
        let y_change = y_range.get(1).unwrap();
        while *from.get(0).unwrap() != (to.get(0).unwrap() + x_change)
            || *from.get(1).unwrap() != (to.get(1).unwrap() + y_change)
        {
            let value = positions
                .entry((*from.get(0).unwrap(), *from.get(1).unwrap()))
                .or_insert(0);
            *value += 1;
            if let Some(x) = from.get_mut(0) {
                *x += x_change;
            }
            if let Some(y) = from.get_mut(1) {
                *y += y_change;
            }
        }
    }
    println!("{:?}", positions.values().filter(|x| **x > 1).count());
}

#[allow(dead_code)]
fn print_positions(positions: &HashMap<(i32, i32), u32>) {
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
    for j in 0..=highest_y {
        for i in 0..=highest_x {
            if positions.contains_key(&(i, j)) {
                print!("{:2?}", positions.get(&(i, j)).unwrap());
            } else {
                print!(" .");
            }
        }
        println!();
    }
}
