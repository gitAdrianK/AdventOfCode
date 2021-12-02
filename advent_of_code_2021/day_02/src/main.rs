use std::fs;

fn main() {
    // Part 1
    let mut h = 0;
    let mut v = 0;

    // Part 2
    let mut h2 = 0;
    let mut v2 = 0;
    let mut aim = 0;

    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in data.lines() {
        let line_split: Vec<&str> = line.split(" ").collect();
        let command = line_split[0];
        let amount = line_split[1].parse::<u32>().unwrap();
        match command {
            "forward" => {
                v = v + amount;
                h2 = h2 + amount;
                v2 = v2 + aim * amount;
            },
            "down" => {
                h = h + amount;
                aim = aim + amount;
            },
            "up" => {
                h = h - amount;
                aim = aim - amount;
            },
            _ => unreachable!(),
        }
    }
    println!("{:?}, {:?}", h*v, h2*v2);
}
