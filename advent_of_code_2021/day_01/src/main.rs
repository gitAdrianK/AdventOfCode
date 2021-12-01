use std::collections::VecDeque;
use std::fs;

fn main() {
    // Part 1
    let mut increases = 0;
    let mut prev = u32::MAX;
    // Part 2
    let mut window: VecDeque<u32> = VecDeque::new();
    let mut increases_window = 0;
    let mut prev_window = u32::MAX;

    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in data.lines() {
        let curr = line.parse().unwrap();
        if curr > prev {
            increases = increases + 1;
        }
        prev = curr;

        window.push_back(curr);
        if window.len() < 3 {
            continue;
        }
        if window.len() > 3 {
            window.pop_front();
        }
        let window_sum = window.iter().sum::<u32>();
        if window_sum > prev_window {
            increases_window = increases_window + 1;
        }
        prev_window = window_sum;
    }
    println!("{:?}, {:?}", increases, increases_window);
}
