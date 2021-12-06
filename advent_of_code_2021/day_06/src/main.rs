use std::fs;

fn main() {
    let mut data = fs::read_to_string("input.txt").expect("Unable to read file");
    data = data.replace("\n", "");
    let fish: Vec<usize> = data
        .split(',')
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
    // Generate spawn timings
    let mut can_spawn: Vec<usize> = vec![0; 7];
    let mut growing_up: Vec<usize> = vec![0; 7];
    for i in 0..7 {
        if let Some(x) = can_spawn.get_mut(i) {
            *x = fish.iter().filter(|&n| *n == i).count();
        }
    }
    for day in 0..256 {
        if day == 79 {
            print!("{:?} ", can_spawn.iter().sum::<usize>() + growing_up.iter().sum::<usize>());
        }
        let today = day % 7;
        let after_tomorrow = (day + 2) % 7;
        // Add new spawned fish
        if let Some(x) = growing_up.get_mut(after_tomorrow) {
            *x = *can_spawn.get(today).unwrap();
        }
        // Add new fish that spawn this day to already spawning fish
        if let Some(x) = can_spawn.get_mut(today) {
            *x += *growing_up.get(today).unwrap();
        }
        if let Some(x) = growing_up.get_mut(today) {
            *x = 0;
        }
    }
    println!("{:?}", can_spawn.iter().sum::<usize>() + growing_up.iter().sum::<usize>());
}
