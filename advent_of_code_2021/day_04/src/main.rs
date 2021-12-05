use std::fs;

fn main() {
    let data = fs::read_to_string("input.txt").expect("Unable to read file");
    let mut iter = data.lines();
    // Numbers pulled and skip next empty line
    // Technically don't need to convert to numbers but I prefer it over keeping strings
    let numbers: Vec<u32> = iter.next().unwrap().split(',').map(|x| x.parse::<u32>().unwrap()).collect();
    iter.next();
    // Create boards
    let mut boards: Vec<Vec<Vec<Option<u32>>>> = Vec::new();
    let mut board: Vec<Vec<Option<u32>>> = Vec::new();
    for line in iter {
        if line.is_empty() {
            boards.push(board.clone());
            board.clear();
        } else {
            // Generate rows
            board.push(line.split_whitespace().map(|x| Some(x.parse::<u32>().unwrap())).collect());
        }
    }
    boards.push(board.clone());
    let mut won_indexes: Vec<usize> = Vec::new();
    // Pull numbers and remove pulled numbers from bingo board
    for pull in numbers {
        for board in &mut boards {
            let length = board.len();
            for i in 0..length {
                for j in 0..length {
                    let curr = board.get_mut(i).unwrap().get_mut(j).unwrap();
                    match curr {
                        Some(nr) => {
                            if *nr == pull {
                                *curr = None;
                            }
                        },
                        None => {},
                    }
                }
            }
        }
        // Check for bingo
        'board: for (index, board) in boards.iter().enumerate() {
            if won_indexes.contains(&index) {
                continue;
            }
            let length = board.len();
            // Horizontals
            for i in 0..length {
                let mut bingo = true;
                for j in 0..length {
                    let curr = board.get(i).unwrap().get(j).unwrap();
                    match curr {
                        Some(_) => {
                            bingo = false;
                            break;
                        },
                        None => {},
                    }
                }
                if bingo {
                    get_victory(board, pull);
                    won_indexes.push(index);
                    continue 'board;
                }
            }
            // Verticals
            for i in 0..length {
                let mut bingo = true;
                for j in 0..length {
                    let curr = board.get(j).unwrap().get(i).unwrap();
                    match curr {
                        Some(_) => {
                            bingo = false;
                            break;
                        },
                        None => {},
                    }
                }
                if bingo {
                    get_victory(board, pull);
                    won_indexes.push(index);
                    continue 'board;
                }
            }
        }
    }
}

fn get_victory(board: &[Vec<Option<u32>>], pull: u32) {
    let flattened = board.iter().flat_map(|a| a.iter()).cloned().collect::<Vec<Option<u32>>>();
    let mut sum: u32 = 0;
    for opt in flattened {
        match opt {
            Some(val) => sum = sum + val,
            None => {},
        }
    }
    println!("Sum: {:?}, pull: {:?}, total: {:?}", sum, pull, sum * pull);
}

#[allow(dead_code)]
fn print_boards(boards: &[Vec<Vec<Option<u32>>>]) {
    for board in boards {
        for row in board {
            for opt in row {
                match opt {
                    Some(nr) => print!("{:2?} ", nr),
                    None => print!("{} ", " _")
                }
            }
            println!();
        }
        println!();
    }
}
