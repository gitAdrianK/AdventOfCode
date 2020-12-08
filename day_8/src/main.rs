use std::fs;

fn main() {
    let mut operations :Vec<(&str, i32, bool)> = Vec::new();
    let input = fs::read_to_string("input.txt").expect("Unable to read file");
    for line in input.lines() {
        let split: Vec<&str> = line.split(" ").collect();
        operations.push((split[0], split[1].parse().unwrap(), false));
    }
    let mut accumulator = 0;
    // While adress can have negative numbers, we trust it to never
    // actually be negative as this would adress nothing
    // and the problem speak of an infinite loop
    let mut adress = 0;
    while let Some(current_op) = operations.get_mut(adress as usize) {
        if current_op.2 {
            println!("Exited via attempted looping.");
            break;
        }
        match &current_op {
            ("nop", _, _) => adress = adress + 1,
            ("acc", acc, _) => {
                accumulator = accumulator + acc;
                adress = adress + 1;
            },
            ("jmp", jmp, _) => adress = adress + jmp,
            _ => unreachable!()
        };
        current_op.2 = true;
    }
    println!("{}", accumulator);
}
