mod base_tile;
mod state_tile;

use base_tile::BaseTile;
use state_tile::StateTile;
use std::fs;

#[allow(dead_code)]
fn main() {
    assert_eq!(20899048083289, solve_day_20("test_input.txt"));
    solve_day_20("input.txt");
}

fn solve_day_20(input: &str) -> u128 {
    let data = fs::read_to_string(input).expect("Unable to read file");
    let mut tiles: Vec<BaseTile> = vec![];
    let mut vec: Vec<&str> = vec![];
    for line in data.lines() {
        if line.is_empty() {
            tiles.push(parse(&vec));
            vec.clear();
        } else {
            vec.push(line)
        }
    }
    tiles.push(parse(&vec));
    println!(
        "Read {0} tiles, resulting in a {1}x{1} square solution!",
        tiles.len(),
        (tiles.len() as f32).sqrt()
    );
    let size_of_square = (tiles.len() as f32).sqrt() as u16;
    let solved_puzzle = match solve_part_1(&tiles, size_of_square) {
        Some(solved) => solved,
        None => {
            println!("There was no solution!");
            std::process::exit(0)
        },
    };
    let corner_ids = get_corner_tiles_ids(&solved_puzzle, size_of_square);
    let prod = corner_ids.0 as u128 * corner_ids.1 as u128 * corner_ids.2 as u128 * corner_ids.3 as u128;
    println!("{}", prod);
    prod
}

fn parse<'a>(arr: &[&'a str]) -> BaseTile<'a> {
    let id: String = arr[0].chars().filter(|c| c.is_digit(10)).collect();
    let mut tile = BaseTile::new(id.parse::<u32>().unwrap());
    for row in arr.iter().skip(1) {
        tile.insert_row(row);
    }
    tile
}

fn solve_part_1<'a>(tiles: &'a[BaseTile], square_size: u16) -> Option<Vec<StateTile<'a>>> {
    for tile in tiles {
        for variant in StateTile::get_variants(tile) {
            let mut field: Vec<Vec<StateTile>> = vec![vec![]; square_size as usize];
            field.get_mut(0).unwrap().push(variant);
            match assemble_square(field, tiles, square_size, 1) {
                Some(solved) => return Some(solved),
                None => {},
            }
        }
    }
    None
}

fn assemble_square<'a>(mut field: Vec<Vec<StateTile<'a>>>, tiles: &'a[BaseTile], square_size: u16, current_pos: u16) -> Option<Vec<StateTile<'a>>> {
    let (row, col) = ((current_pos / square_size) as usize, (current_pos % square_size) as usize);
    if current_pos as usize >= tiles.len() {
        let mut flattened = vec![];
        for field_row in field {
            for field_col in field_row {
                flattened.push(field_col)
            }
        }
        return Some(flattened);
    }
    'tile: for tile in tiles {
        for r in 0..=row {
            for c in 0..=col {
                if r == row && c == col {
                    continue
                }
                // Check if the tile is already used
                if field.get(r).unwrap().get(c).unwrap().cmp_with_basetile(tile) {
                    continue 'tile
                }
            }
        }
        for variant in StateTile::get_variants(tile) {
            // Row at the top has no top edge
            if row != 0 {
                if variant.get_top_edge().unwrap() != field.get(row - 1).unwrap().get(col).unwrap().get_bottom_edge().unwrap() {
                    continue
                }
            }
            // Column at the left has no left edge
            if col != 0 {
                if variant.get_left_edge().unwrap() != field.get(row).unwrap().get(col - 1).unwrap().get_right_edge().unwrap() {
                    continue
                }
            }
            // Since I am filling top left to bottom right there will never be elements to the right
            // or the bottom to the current one
            // [X] [ ] [ ]    [X] [X] [ ]    [X] [X] [X]    [X] [X] [X]    [X] [X] [X]
            // [ ] [ ] [ ] -> [ ] [ ] [ ] -> [ ] [ ] [ ] -> [X] [ ] [ ] -> [X] [X] [ ]
            // [ ] [ ] [ ]    [ ] [ ] [ ]    [ ] [ ] [ ]    [ ] [ ] [ ]    [ ] [ ] [ ]
            // Start          Cmp left       Cmp left      Cmp top        Cmp top/left
            // At this point all edges match
            field.get_mut(row).unwrap().push(variant);
            return assemble_square(field, tiles, square_size, current_pos + 1);
        }
    }
    None
}

fn get_corner_tiles_ids(tiles: &[StateTile], square_size: u16) -> (u32, u32, u32, u32) {
    (
        tiles.get(0).unwrap().tile.id,
        tiles.get((square_size - 1) as usize).unwrap().tile.id,
        tiles.get(tiles.len() - square_size as usize).unwrap().tile.id,
        tiles.get(tiles.len() - 1).unwrap().tile.id,
    )
    //(1951, 3079, 2971, 1171)
}
