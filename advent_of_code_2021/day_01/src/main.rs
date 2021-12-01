use std::fs;

fn main() {
    let mut increases = 0;
    let mut prev = u32::MAX;
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in data.lines() {
        let curr = line.parse().unwrap();
        if curr > prev {
            increases = increases + 1;
        }
        prev = curr
    }
    println!("{:?}", increases);
}
