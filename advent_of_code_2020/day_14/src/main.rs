extern crate regex;
use regex::Regex;
use InitInstruction::*;
use std::collections::HashMap;

fn main() {
    assert_eq!((165, 0), solve_day_14("test_input.txt"));
    println!("{:?}", solve_day_14("input.txt"));
}

fn solve_day_14(input: &str) -> (u64, usize) {
    use std::fs;
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut tokens: Vec<InitInstruction> = Vec::new();
    for line in data.lines() {
        tokens.push(tokenize(line));
    }
    (solve_part_1(tokens), 0)
}

fn tokenize(s: &str) -> InitInstruction {
    let re = Regex::new(r"mask = (?P<mask>[0|1|X]{36})|mem\[(?P<addr>\d+)\] = (?P<value>\d+)")
        .unwrap();
    let instruction = re.captures(s).unwrap();
    if let Some(i) = instruction.name("mask") {
        return Mask {
            mask: &s[i.start()..i.end()],
        };
    }
    let (i, j) = (instruction.name("addr").unwrap(), instruction.name("value").unwrap());
    Value {
        addr: s[i.start()..i.end()].parse().unwrap(),
        value: s[j.start()..j.end()].parse().unwrap(),
    }
}

fn solve_part_1(init: Vec<InitInstruction>) -> u64 {
    let mut _mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    let mut _addr: HashMap<u64, u64> = HashMap::new();
    for i in init {
        match i {
            Mask { mask } => _mask = mask,
            Value { addr, value } => {
                let re = Regex::new(r"X").unwrap();
                let zero_mask: u64 = u64::from_str_radix(&re.replace_all(_mask, "0"), 2).unwrap();
                let one_mask: u64 = u64::from_str_radix(&re.replace_all(_mask, "1"), 2).unwrap();
                let mut _value = value;
                _value = _value | zero_mask;
                _value = _value & one_mask;
                _addr.insert(addr, _value);
            }
        }
    }
    _addr.values().sum()
}

#[derive(Copy, Clone)]
enum InitInstruction<'a> {
    Mask { mask: &'a str },
    Value { addr: u64, value: u64 },
}
