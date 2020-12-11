use std::fmt;
use std::fs;
use grid::*;

fn main() {
    assert_eq!(37, solve_day_11("test_input.txt"));
    println!("{}", solve_day_11("input.txt"));
}

fn solve_day_11(input: &str) -> usize {
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut seating: Grid<Seating> = grid![];
    for line in data.lines() {
        seating.push_row(tokenize_seating(line));
    }
    seating = do_step(&seating);
    let mut prev_occ = 0;
    let mut curr_occ = seating.flatten()
        .iter()
        .filter(|&n| *n == Seating::Occupied).count();
    while prev_occ != curr_occ {
        seating = do_step(&seating);
        prev_occ = curr_occ;
        curr_occ = seating.flatten()
            .iter()
            .filter(|&n| *n == Seating::Occupied).count();
    }
    return curr_occ
}

fn tokenize_seating(line: &str) -> Vec<Seating> {
    let mut vec : Vec<Seating> = Vec::new();
    let chars = line.chars();
    for c in chars {
        match c {
            '.' => vec.push(Seating::Floor),
            'L' => vec.push(Seating::Empty),
            '#' => vec.push(Seating::Occupied),
            _ => unreachable!(),
        }
    }
    return vec
}

fn do_step(grid: &Grid<Seating>) -> Grid<Seating> {
    let mut new_grid = grid![];
    for row in 0..grid.rows() {
        let mut vec: Vec<Seating> = Vec::new();
        for col in 0..grid.cols() {
            let curr_seat = grid.get(row, col).unwrap();
            let occupied_neighbors = get_occupied_neighbors(grid, row, col);
            match *curr_seat {
                Seating::Floor => vec.push(Seating::Floor),
                Seating::Empty => {
                    if occupied_neighbors == 0 {
                        vec.push(Seating::Occupied)
                    } else {
                        vec.push(Seating::Empty)
                    }
                },
                Seating::Occupied => {
                    if occupied_neighbors >=  4 {
                        vec.push(Seating::Empty)
                    } else {
                        vec.push(Seating::Occupied)
                    }
                },
            }
        }
        new_grid.push_row(vec)
    }
    return new_grid
}

fn get_occupied_neighbors(grid: &Grid<Seating>, row: usize, col: usize) -> u8 {
    let mut occupied_seats = 0;
    for x in -1..2  {
        for y in -1..2 {
            let row_pos = row as isize + y;
            let col_pos = col as isize + x;
            if (x == 0 && y == 0) || row_pos < 0 || col_pos < 0 {
                continue
            }
            let seat = match grid.get(row_pos as usize, col_pos as usize) {
                Some(seat) => seat,
                None => &Seating::Floor,
            };
            match seat {
                Seating::Occupied => occupied_seats += 1,
                Seating::Empty => {},
                Seating::Floor => {},
            }
        }
    }
    return occupied_seats
}

#[derive(Copy, Clone, PartialEq)]
enum Seating {
    Empty,
    Occupied,
    Floor,
}

impl Default for Seating {
    fn default() -> Self { Seating::Floor }
}

impl fmt::Debug for Seating {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match &self {
            Seating::Empty => write!(f, "L"),
            Seating::Floor => write!(f, "."),
            Seating::Occupied => write!(f, "#"),
        }
    }
}
