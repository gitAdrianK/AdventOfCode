use std::fs;

fn main() {
    let mut data = fs::read_to_string("input.txt").expect("Unable to read file");
    data = data.replace("\n", "");
    let mut fish: Vec<u8> = data
        .split(',')
        .map(|x| x.parse::<u8>().unwrap())
        .collect();
    for _ in 0..80 {
        let mut spawned: Vec<u8> = Vec::new();
        for f in &mut fish {
            if *f == 0 {
                spawned.push(8);
                *f = 6;
            } else {
                *f -= 1;
            }
        }
        fish.append(&mut spawned);
    }
    println!("{:?}", fish.len());
}
