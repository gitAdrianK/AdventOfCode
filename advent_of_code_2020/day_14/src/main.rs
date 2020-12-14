extern crate regex;
use regex::Regex;
use InitInstruction::*;
use std::collections::HashMap;

fn main() {
    assert_eq!(165, solve_day_14("test_input.txt", true, false).0);
    assert_eq!(208, solve_day_14("test_input_2.txt", false, true).1);
    println!("{:?}", solve_day_14("input.txt", true, true));
}

fn solve_day_14(input: &str, do_p1: bool, do_p2: bool) -> (u64, u64) {
    use std::fs;
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut tokens: Vec<InitInstruction> = Vec::new();
    for line in data.lines() {
        tokens.push(tokenize(line));
    }
    let mut p1 = 0;
    if do_p1 {
        p1 = solve_part_1(&tokens);
    }
    let mut p2 = 0;
    if do_p2 {
        p2 = solve_part_2(&tokens);
    }
    (p1, p2)
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

fn solve_part_1(init: &Vec<InitInstruction>) -> u64 {
    let mut _mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    let mut _addr: HashMap<u64, u64> = HashMap::new();
    for &i in init {
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

fn solve_part_2(init: &Vec<InitInstruction>) -> u64 {
    let mut _mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    let mut _addr: HashMap<u64, u64> = HashMap::new();
    for &i in init {
        match i {
            Mask { mask } => _mask = mask,
            Value { addr, value } => {
                let addr_as_binary = format!("{:036b}", addr);
                let mut result: String = "".into();
                for (i, c) in _mask.chars().enumerate() {
                    match c {
                        '1' => result += "1",
                        'X' => result += "X",
                        '0' => result += &addr_as_binary.chars().nth(i).unwrap().to_string(),
                        _ => unreachable!(),
                    }
                }
                let re = Regex::new(r"X").unwrap();
                replace_first_x(&result, &re, value, &mut _addr);
            }
        }
    }
    let sum = _addr.values().sum();
    sum
}

fn replace_first_x<'a>(s: &'a str, r: &Regex, v: u64, map: &mut HashMap<u64, u64>) {
    if !r.is_match(s) {
        let e: u64 = u64::from_str_radix(&s, 2).unwrap();
        map.insert(e, v);
    } else {
        replace_first_x(&r.replacen(s, 1, "0"), &r, v, map);
        replace_first_x(&r.replacen(s, 1, "1"), &r, v, map);
    }
}

#[derive(Copy, Clone)]
enum InitInstruction<'a> {
    Mask { mask: &'a str },
    Value { addr: u64, value: u64 },
}
