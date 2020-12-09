extern crate regex;

use std::fs;
use regex::Regex;

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
        // Due to testing every adress start value
        // we know the adress values that don't result in a loop are:
        // 52-64, 100-104, 281, 302-306, 363-370, 525-531,
        // 563-567, 601-604, 629-633
        // Note: Adresses in file start at 1 (internal adresses are -1)
        // for n in 0..operations.len() {
        //    // We need to reset for every loop
        //    for reset_op in operations.iter_mut() {
        //        reset_op.2 = false;
        //    }
        //    ...
        // }
        let regex = Regex::new("^(5[2-9]|6[0-4])$|(10[0-4])|281|(30[2-6])|(36[3-9]|370)|(52[5-9]|53[01])|(56[3-7])|(60[1-4])|(629|63[0-3])$").unwrap();
        if current_op.0 == "nop" {
            if regex.is_match(&(current_op.1 + adress + 1).to_string()) {
                println!("Corrupt operation at {}, change \"nop\" to \"jmp\"", adress + 1);
            }
        } else if current_op.0 == "jmp" {
            if regex.is_match(&(1 + adress + 1).to_string()) {
                println!("Corrupt operation at {}, change \"jmp\" to \"nop\"", adress + 1);
            }
        }
        if current_op.2 {
            print!("Exited via attempted looping. ");
            break;
        }
        match &current_op {
            ("nop", _, _) => {
                adress = adress + 1;
            },
            ("acc", acc, _) => {
                accumulator = accumulator + acc;
                adress = adress + 1;
            },
            ("jmp", jmp, _) => {
                adress = adress + jmp;
            },
            _ => unreachable!()
        };
        current_op.2 = true;
    }
    println!("{}", accumulator);
    // Corrupt operation at 280, change "jmp" to "nop"
    // changing this in the file results in an accumulator
    // value of 1358
}
