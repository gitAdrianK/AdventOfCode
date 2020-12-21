mod base_tile;
mod state_tile;

use base_tile::BaseTile;
use state_tile::StateTile;
use std::fs;

#[allow(dead_code)]
fn main() {
    assert_eq!((20899048083289, 273), solve_day_20("test_input.txt"));
    solve_day_20("input.txt");
}

fn solve_day_20(input: &str) -> (u128, u32) {
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
        }
    };
    let corner_ids = get_corner_tiles_ids(&solved_puzzle);
    let prod =
        corner_ids.0 as u128 * corner_ids.1 as u128 * corner_ids.2 as u128 * corner_ids.3 as u128;
    println!("Product of corner ids: {}", prod);
    let sharps = solve_part_2(&solved_puzzle);
    println!("Water roughness: {}", sharps);
    (prod, sharps)
}

fn parse(arr: &[&str]) -> BaseTile {
    let id: String = arr[0].chars().filter(|c| c.is_digit(10)).collect();
    let mut tile = BaseTile::new(id.parse::<u32>().unwrap());
    for row in arr.iter().skip(1) {
        tile.insert_row(row);
    }
    tile
}

fn solve_part_1(tiles: &[BaseTile], square_size: u16) -> Option<Vec<Vec<StateTile>>> {
    for tile in tiles {
        for variant in StateTile::get_variants(tile) {
            let mut field: Vec<Vec<StateTile>> = vec![vec![]; square_size as usize];
            field.get_mut(0).unwrap().push(variant);
            match assemble_square(field, tiles, square_size, 1) {
                Some(solved) => return Some(solved),
                None => {}
            }
        }
    }
    None
}

fn assemble_square(
    mut field: Vec<Vec<StateTile>>,
    tiles: &[BaseTile],
    square_size: u16,
    current_pos: u16,
) -> Option<Vec<Vec<StateTile>>> {
    let (row, col) = (
        (current_pos / square_size) as usize,
        (current_pos % square_size) as usize,
    );
    if current_pos as usize >= tiles.len() {
        return Some(field);
    }
    'tile: for tile in tiles {
        for r in 0..=row {
            for c in 0..=col {
                if r == row && c == col {
                    continue;
                }
                // Check if the tile is already used
                if field
                    .get(r)
                    .unwrap()
                    .get(c)
                    .unwrap()
                    .cmp_with_basetile(tile)
                {
                    continue 'tile;
                }
            }
        }
        for variant in StateTile::get_variants(tile) {
            // Row at the top has no top edge
            if row != 0 {
                if variant.get_top_edge().unwrap()
                    != field
                        .get(row - 1)
                        .unwrap()
                        .get(col)
                        .unwrap()
                        .get_bottom_edge()
                        .unwrap()
                {
                    continue;
                }
            }
            // Column at the left has no left edge
            if col != 0 {
                if variant.get_left_edge().unwrap()
                    != field
                        .get(row)
                        .unwrap()
                        .get(col - 1)
                        .unwrap()
                        .get_right_edge()
                        .unwrap()
                {
                    continue;
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

fn get_corner_tiles_ids(tiles: &Vec<Vec<StateTile>>) -> (u32, u32, u32, u32) {
    (
        tiles.first().unwrap().first().unwrap().tile.id,
        tiles.first().unwrap().last().unwrap().tile.id,
        tiles.last().unwrap().first().unwrap().tile.id,
        tiles.last().unwrap().last().unwrap().tile.id,
    )
}

fn solve_part_2(image_tiles: &Vec<Vec<StateTile>>) -> u32 {
    let stitch_tile = stitch_tiles(image_tiles);
    let mut amount_sharps = 0;
    for i in 0..stitch_tile.row_size {
        amount_sharps += stitch_tile
            .get_row(i)
            .unwrap()
            .chars()
            .filter(|c| *c == '#')
            .collect::<Vec<char>>()
            .len() as u32;
    }
    for variant in StateTile::get_variants(&stitch_tile) {
        let seamonsters = find_seamonster(&variant);
        if seamonsters != 0 {
            // Roughness: amount all #s - (15 * seamonsters)
            return amount_sharps - 15 * seamonsters;
        }
    }
    amount_sharps
}

fn stitch_tiles(image_tiles: &Vec<Vec<StateTile>>) -> BaseTile {
    let mut stitch = BaseTile::new(1);
    for col in image_tiles {
        let col_size = col.first().unwrap().tile.col_size;
        for i in 1..col_size - 1 {
            let mut row_stitch: String = "".into();
            for row in col {
                let trim_front_end: String = row
                    .get_row(i)
                    .unwrap()
                    .chars()
                    .take(row.tile.row_size - 1)
                    .skip(1)
                    .collect();
                row_stitch.push_str(&trim_front_end);
            }
            stitch.insert_row(&row_stitch);
        }
    }
    stitch
}

fn find_seamonster(tile: &StateTile) -> u32 {
    let mut seamonsters = 0;
    for col in 1..(tile.tile.col_size - 1) {
        for row in 0..(tile.tile.row_size - 20) {
            if tile.get_col(col).unwrap().chars().nth(row).unwrap() == '#' {
                if is_seamonster(tile, row, col) {
                    seamonsters += 1;
                }
            }
        }
    }
    seamonsters
}

fn is_seamonster(tile: &StateTile, start_x: usize, start_y: usize) -> bool {
    // The longest line is the middle one.
    // The height is 3, the width is 20
    // A seamonster consists of 15 #s
    // Seamonster:
    //                   #
    // #    ##    ##    ###
    //  #  #  #  #  #  #
    let above_row = tile.get_col(start_y - 1).unwrap();
    let above = above_row.as_str();
    let middle_row = tile.get_col(start_y).unwrap();
    let middle = middle_row.as_str();
    let below_row = tile.get_col(start_y + 1).unwrap();
    let below = below_row.as_str();
    above.get(start_x + 18..=start_x + 18).unwrap() == "#"
        && middle.get(start_x + 0..=start_x + 0).unwrap() == "#"
        && middle.get(start_x + 5..=start_x + 5).unwrap() == "#"
        && middle.get(start_x + 6..=start_x + 6).unwrap() == "#"
        && middle.get(start_x + 11..=start_x + 11).unwrap() == "#"
        && middle.get(start_x + 12..=start_x + 12).unwrap() == "#"
        && middle.get(start_x + 17..=start_x + 17).unwrap() == "#"
        && middle.get(start_x + 18..=start_x + 18).unwrap() == "#"
        && middle.get(start_x + 19..=start_x + 19).unwrap() == "#"
        && below.get(start_x + 1..=start_x + 1).unwrap() == "#"
        && below.get(start_x + 4..=start_x + 4).unwrap() == "#"
        && below.get(start_x + 7..=start_x + 7).unwrap() == "#"
        && below.get(start_x + 10..=start_x + 10).unwrap() == "#"
        && below.get(start_x + 13..=start_x + 13).unwrap() == "#"
        && below.get(start_x + 16..=start_x + 16).unwrap() == "#"
}
