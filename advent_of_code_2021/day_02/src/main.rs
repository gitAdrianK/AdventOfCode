use std::fs;

fn main() {
    let mut h = 0;
    let mut v = 0;

    let data = fs::read_to_string("test_input.txt").expect("Unable to read file");
    for line in data.lines() {
        let line_split: Vec<&str> = line.split(" ").collect();
        let command = line_split[0];
        let amount = line_split[1].parse::<u32>().unwrap();
        match command {
            "forward" => v = v + amount,
            "down" => h = h + amount,
            "up" => h = h - amount,
            _ => unreachable!(),
        }
    }
    println!("{:?}", h*v);
}
