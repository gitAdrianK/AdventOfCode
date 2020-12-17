use std::fmt;
use std::fs;

fn main() {
    //assert_eq!((112, 0), solve_day_17("test_input.txt"));
    println!("{:?}", solve_day_17("input.txt"));
}

fn pretty_print(z_vec: &Vec<Vec<Vec<Cell>>>) {
    for (z, z_vec) in z_vec.iter().enumerate() {
        println!("z-level: {}", z);
        for y_vec in z_vec.iter() {
            for x in y_vec.iter() {
                print!("{}", x);
            }
            println!();
        }
    }
}

fn solve_day_17(input: &str) -> (usize, usize) {
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut seed_vec: Vec<Vec<Vec<Cell>>> = vec![vec![]];
    for line in data.lines() {
        seed_vec.get_mut(0).unwrap().push(tokenize(line));
    }
    //pretty_print(&seed_vec);
    (solve(&seed_vec), 0)
}

fn tokenize(line: &str) -> Vec<Cell> {
    let mut vec: Vec<Cell> = Vec::new();
    for c in line.chars() {
        match c {
            '.' => vec.push(Cell::Inactive),
            '#' => vec.push(Cell::Active),
            _ => unreachable!(),
        }
    }
    vec
}

fn solve(seed_vec: &Vec<Vec<Vec<Cell>>>) -> usize {
    let mut z_vec = seed_vec.clone();
    for _ in 0..6 {
        z_vec = do_cycle(&z_vec);
    }
    let mut sum_active = 0;
    for y_vec in z_vec.iter() {
        for x_vec in y_vec.iter() {
            sum_active += x_vec.iter().filter(|&n| *n == Cell::Active).count();
        }
    }
    sum_active
}

fn do_cycle(z_vec: &Vec<Vec<Vec<Cell>>>) -> Vec<Vec<Vec<Cell>>> {
    pretty_print(&z_vec);
    let z_vec = grow(&z_vec);
    let mut new_z_vec: Vec<Vec<Vec<Cell>>> = vec![];
    for (z, y_vec) in z_vec.iter().enumerate() {
        let mut new_y_vec: Vec<Vec<Cell>> = vec![];
        for (y, x_vec) in y_vec.iter().enumerate() {
            let mut new_x_vec: Vec<Cell> = vec![];
            for (x, cell) in x_vec.iter().enumerate() {
                let active_neighbors = get_neighbors(&z_vec, x, y, z);
                match cell {
                    Cell::Inactive => {
                        if active_neighbors == 3 {
                            new_x_vec.push(Cell::Active)
                        } else {
                            new_x_vec.push(Cell::Inactive)
                        }
                    },
                    Cell::Active => {
                        if active_neighbors == 2 || active_neighbors == 3 {
                            new_x_vec.push(Cell::Active)
                        } else {
                            new_x_vec.push(Cell::Inactive)
                        }
                    }
                }
                //print!("{} ", active_neighbors);
            }
            new_y_vec.push(new_x_vec);
            //println!();
        }
        new_z_vec.push(new_y_vec);
        //println!();
    }
    new_z_vec
}

// XXX: I am creating so many new vectors its not even funny, has to be a real hit on performance
// Rewrite this adding two empty cells at the end and rotating
// Same for shrink, rotate and pop when possible
fn grow(z_vec: &Vec<Vec<Vec<Cell>>>) -> Vec<Vec<Vec<Cell>>> {
    let y_len = z_vec.get(0).unwrap().len() + 2;
    let x_len = z_vec.get(0).unwrap().get(0).unwrap().len() + 2;
    let mut new_z_vec: Vec<Vec<Vec<Cell>>> = vec![];
    new_z_vec.push(vec![vec![Cell::Inactive; y_len]; y_len]);
    for y_vec in z_vec.iter() {
        let mut new_y_vec: Vec<Vec<Cell>> = vec![];
        new_y_vec.push(vec![Cell::Inactive; x_len]);
        for x_vec in y_vec.iter() {
            let mut new_x_vec: Vec<Cell> = vec![];
            new_x_vec.push(Cell::Inactive);
            for cell in x_vec.iter() {
                new_x_vec.push(*cell);
            }
            new_x_vec.push(Cell::Inactive);
            new_y_vec.push(new_x_vec);
        }
        new_y_vec.push(vec![Cell::Inactive; x_len]);
        new_z_vec.push(new_y_vec);
    }
    new_z_vec.push(vec![vec![Cell::Inactive; y_len]; y_len]);
    new_z_vec
}

fn shrink(z_vec: &Vec<Vec<Vec<Cell>>>) -> Vec<Vec<Vec<Cell>>> {
    //TODO: Remove empty xyz vectors
    let mut new_z_vec: Vec<Vec<Vec<Cell>>> = vec![];
    new_z_vec
}

fn get_neighbors(z_vec: &Vec<Vec<Vec<Cell>>>, x: usize, y: usize, z: usize) -> u8 {
    let mut active_neighbors = 0;
    for _x in -1..=1 {
        for _y in -1..=1 {
            for _z in -1..=1 {
                let neighbor_x = x as isize - _x;
                let neighbor_y = y as isize - _y;
                let neighbor_z = z as isize - _z;
                if (neighbor_x < 0 || neighbor_y < 0 || neighbor_z < 0)
                    || (_x == 0 && _y == 0 && _z == 0)
                {
                    continue;
                }
                // I gotta see about maybe some let xyz_vec = match {}
                if let Some(y_vec) = z_vec.get(neighbor_z as usize) {
                    if let Some(x_vec) = y_vec.get(neighbor_y as usize) {
                        if let Some(cell) = x_vec.get(neighbor_x as usize) {
                            match cell {
                                Cell::Active => active_neighbors += 1,
                                _ => {}
                            }
                        }
                    }
                }
            }
        }
    }
    active_neighbors
}

#[derive(Copy, Clone, PartialEq, Eq)]
enum Cell {
    Active,
    Inactive,
}

impl fmt::Display for Cell {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match &self {
            Cell::Active => write!(f, "⬜"),
            Cell::Inactive => write!(f, "⬛"),
        }
    }
}
