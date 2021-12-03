use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let len = data.lines().nth(0).unwrap().len();
    // Part 1
    let mut vec = vec![(0,0); len];
    for line in data.lines() {
        // Count 0s and 1s
        for (i, c) in line.chars().enumerate() {
            match c {
                '0' => {
                    let pair = vec.get(i).unwrap();
                    vec[i] = (pair.0 + 1, pair.1)
                },
                '1' => {
                    let pair = vec.get(i).unwrap();
                    vec[i] = (pair.0, pair.1 + 1)
                },
                _ => unreachable!(),
            }
        }
    }
    // Build binary number
    let mut gamma_rate = "".to_owned();
    let mut epsilon_rate = "".to_owned();
    for v in vec {
        if v.0 > v.1 {
            gamma_rate = gamma_rate + "0";
            epsilon_rate = epsilon_rate + "1";
        } else {
            gamma_rate = gamma_rate + "1";
            epsilon_rate = epsilon_rate + "0";
        }
    }
    // Part 2
    let mut oxygen_rate: Vec<&str> = data.lines().collect();
    let mut index = 0;
    while oxygen_rate.len() > 1 {
        let mut pair = (0, 0);
        // Count 0s and 1s
        for line in oxygen_rate.iter() {
            match line.chars().nth(index).unwrap() {
                '0' => {
                    pair = (pair.0 + 1, pair.1)
                },
                '1' => {
                    pair = (pair.0, pair.1 + 1)
                },
                 _ => unreachable!(),
            }
        }
        // Filter out numbers with the lower bit at index position
        let mut filtered_ox_rate: Vec<&str> = Vec::new();
        if pair.0 > pair.1 {
            for line in oxygen_rate.iter() {
                if line.chars().nth(index).unwrap() == '0' {
                    filtered_ox_rate.push(line);
                }
            }
        } else {
            for line in oxygen_rate {
                if line.chars().nth(index).unwrap() == '1' {
                    filtered_ox_rate.push(line);
                }
            }
        }
        oxygen_rate = filtered_ox_rate;
        index = index + 1;
    }
    let mut co2_rate: Vec<&str> = data.lines().collect();
    index = 0;
    while co2_rate.len() > 1 {
        let mut pair = (0, 0);
        // Count 0s and 1s
        for line in co2_rate.iter() {
            match line.chars().nth(index).unwrap() {
                '0' => {
                    pair = (pair.0 + 1, pair.1)
                },
                '1' => {
                    pair = (pair.0, pair.1 + 1)
                },
                 _ => unreachable!(),
            }
        }
        // Filter out numbers with the lower bit at index position
        let mut filtered_co2_rate: Vec<&str> = Vec::new();
        if pair.0 > pair.1 {
            for line in co2_rate.iter() {
                if line.chars().nth(index).unwrap() == '1' {
                    filtered_co2_rate.push(line);
                }
            }
        } else {
            for line in co2_rate {
                if line.chars().nth(index).unwrap() == '0' {
                    filtered_co2_rate.push(line);
                }
            }
        }
        co2_rate = filtered_co2_rate;
        index = index + 1;
    }
    println!(
        "{:?}, {:?}",
        usize::from_str_radix(&gamma_rate, 2).unwrap()*usize::from_str_radix(&epsilon_rate, 2).unwrap(),
        usize::from_str_radix(&oxygen_rate.first().unwrap(), 2).unwrap()*usize::from_str_radix(&co2_rate.first().unwrap(), 2).unwrap(),
    );
}
