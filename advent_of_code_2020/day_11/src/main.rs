use grid::*;
use std::fmt;
use std::fs;

fn main() {
    assert_eq!((37, 26), solve_day_11("test_input.txt"));
    println!("{:?}", solve_day_11("input.txt"));
}

fn solve_day_11(input: &str) -> (usize, usize) {
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut seating: Grid<Seating> = grid![];
    for line in data.lines() {
        seating.push_row(tokenize_seating(line));
    }
    return (solve(&seating, 4, 1), solve(&seating, 5, 0));
}

fn tokenize_seating(line: &str) -> Vec<Seating> {
    let mut vec: Vec<Seating> = Vec::new();
    let chars = line.chars();
    for c in chars {
        match c {
            '.' => vec.push(Seating::Floor),
            'L' => vec.push(Seating::Empty),
            '#' => vec.push(Seating::Occupied),
            _ => unreachable!(),
        }
    }
    return vec;
}

fn solve(grid: &Grid<Seating>, tolerance: usize, search_range: usize) -> usize {
    let mut grid = do_step(&grid, tolerance, search_range);
    let mut prev_occ = 0;
    let mut curr_occ = grid
        .flatten()
        .iter()
        .filter(|&n| *n == Seating::Occupied)
        .count();
    while prev_occ != curr_occ {
        grid = do_step(&grid, tolerance, search_range);
        prev_occ = curr_occ;
        curr_occ = grid
            .flatten()
            .iter()
            .filter(|&n| *n == Seating::Occupied)
            .count();
    }
    return curr_occ;
}

fn do_step(grid: &Grid<Seating>, tolerance: usize, search_range: usize) -> Grid<Seating> {
    let mut new_grid = grid![];
    for row in 0..grid.rows() {
        let mut vec: Vec<Seating> = Vec::new();
        for col in 0..grid.cols() {
            let curr_seat = grid.get(row, col).unwrap();
            let occupied_neighbors = get_occupied_visible(grid, row, col, search_range);
            match *curr_seat {
                Seating::Floor => vec.push(Seating::Floor),
                Seating::Empty => {
                    if occupied_neighbors == 0 {
                        vec.push(Seating::Occupied)
                    } else {
                        vec.push(Seating::Empty)
                    }
                }
                Seating::Occupied => {
                    if occupied_neighbors >= tolerance {
                        vec.push(Seating::Empty)
                    } else {
                        vec.push(Seating::Occupied)
                    }
                }
            }
        }
        new_grid.push_row(vec)
    }
    return new_grid;
}

fn get_occupied_visible(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    let mut occupied_seats = 0;
    let mut search_range = search_range;
    if search_range == 0 {
        search_range = usize::MAX - 1;
    }
    // XXX: ¯\_(ツ)_/¯ Lets not talk about it, I am not proud of it
    // I WILL rewrite this.
    occupied_seats += do_north(grid, row, col, search_range);
    occupied_seats += do_north_east(grid, row, col, search_range);
    occupied_seats += do_east(grid, row, col, search_range);
    occupied_seats += do_south_east(grid, row, col, search_range);
    occupied_seats += do_south(grid, row, col, search_range);
    occupied_seats += do_south_west(grid, row, col, search_range);
    occupied_seats += do_west(grid, row, col, search_range);
    occupied_seats += do_north_west(grid, row, col, search_range);
    return occupied_seats;
}

fn do_north(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        let pos = row as isize - i as isize;
        if pos < 0 {
            return 0;
        }
        if let Some(seat) = grid.get(pos as usize, col) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        }
    }
    return 0
}

fn do_south(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        if let Some(seat) = grid.get(row + i as usize, col) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        } else {
            return 0
        }
    }
    return 0
}

fn do_west(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        let pos = col as isize - i as isize;
        if pos < 0 {
            return 0;
        }
        if let Some(seat) = grid.get(row, pos as usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        }
    }
    return 0
}

fn do_east(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        if let Some(seat) = grid.get(row, col + i as usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        } else {
            return 0
        }
    }
    return 0
}

fn do_north_west(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        let pos_x = row as isize - i as isize;
        if pos_x < 0 {
            return 0;
        }
        let pos_y = col as isize - i as isize;
        if pos_y < 0 {
            return 0;
        }
        if let Some(seat) = grid.get(pos_x as usize, pos_y as usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        }
    }
    return 0
}

fn do_south_east(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        if let Some(seat) = grid.get(row + i as usize, col + i as usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        } else {
            return 0
        }
    }
    return 0
}

fn do_north_east(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        let pos = row as isize - i as isize;
        if pos < 0 {
            return 0;
        }
        if let Some(seat) = grid.get(pos as usize, col + i as  usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        } else {
            return 0
        }
    }
    return 0
}

fn do_south_west(grid: &Grid<Seating>, row: usize, col: usize, search_range: usize) -> usize {
    for i in 1..search_range + 1 {
        let pos = col as isize - i as isize;
        if pos < 0 {
            return 0;
        }
        if let Some(seat) = grid.get(row + i as usize, pos as usize) {
            match seat {
                Seating::Occupied => return 1,
                Seating::Empty => return 0,
                Seating::Floor => {},
            }
        } else {
            return 0
        }
    }
    return 0
}

#[derive(Copy, Clone, PartialEq)]
enum Seating {
    Empty,
    Occupied,
    Floor,
}

impl Default for Seating {
    fn default() -> Self {
        Seating::Floor
    }
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
