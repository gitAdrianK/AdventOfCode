extern crate regex;
use regex::Regex;
use std::fs;

fn main() {
    let re = Regex::new(r"([0-9]+)-([0-9]+) ([a-z]{1}): ([a-z]+)").unwrap();
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let (mut p1, mut p2) = (0, 0);
    for line in data.lines() {
        let cap = re.captures(line).unwrap();
        let a = cap[1].parse().unwrap();
        let b = cap[2].parse().unwrap();
        let c = cap[3].chars().nth(0).unwrap();
        let d = &cap[4];
        if solve_part_1(a, b, c, d) { p1 += 1; }
        if solve_part_2(a, b, c, d) { p2 += 1; }
    }
    println!("{:?}, {:?}", p1, p2);
}

fn solve_part_1(min: usize, max: usize, letter: char, pw: &str) -> bool {
    let c = pw.matches(letter).count();
    min <= c && c <= max
}

fn solve_part_2(pos1: usize, pos2: usize, letter: char, pw: &str) -> bool {
    (pw.chars().nth(pos1 - 1).unwrap() == letter) ^ (pw.chars().nth(pos2 - 1).unwrap() == letter)
}
