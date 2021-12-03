use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let len = data.lines().nth(0).unwrap().len();
    let mut vec = vec![(0,0); len];
    for line in data.lines() {
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
    println!("{:?}", usize::from_str_radix(&gamma_rate, 2).unwrap()*usize::from_str_radix(&epsilon_rate, 2).unwrap());
}
