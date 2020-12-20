use crate::state_tile::StateTile;
use std::fmt;

#[derive(Clone)]
pub struct BaseTile<'a> {
    pub id: u32,
    data: Vec<&'a str>,
    row_size: usize,
    col_size: usize,
}

#[allow(dead_code)]
impl<'a> BaseTile<'a> {
    pub fn new(id: u32) -> Self {
        BaseTile {
            id: id,
            data: vec![],
            row_size: 0,
            col_size: 0,
        }
    }

    pub fn insert_row(&mut self, row: &'a str) {
        if self.row_size == 0 {
            self.row_size = row.len();
        }
        if self.row_size != row.len() {
            println!("Couldn't insert \"{}\", as size to previous differs", row);
            return;
        }
        self.data.push(row);
        self.col_size += 1;
    }

    fn get_row(&self, index: usize) -> Option<String> {
        if self.row_size == 0 || self.row_size <= index {
            return None;
        }
        let string = *self.data.get(index).unwrap();
        Some(string.into())
    }

    pub fn get_top_edge(&self) -> Option<String> {
        self.get_row(0)
    }

    pub fn get_bottom_edge(&self) -> Option<String> {
        self.get_row(self.col_size - 1)
    }

    fn get_col(&self, index: usize) -> Option<String> {
        if self.col_size == 0 || self.col_size <= index {
            return None;
        }
        let mut col = String::new();
        for row in &self.data {
            col.push(row.chars().nth(index).unwrap());
        }
        Some(col)
    }

    pub fn get_left_edge(&self) -> Option<String> {
        self.get_col(0)
    }

    pub fn get_right_edge(&self) -> Option<String> {
        self.get_col(self.row_size - 1)
    }

    pub fn cmp_with_basetile(&self, other: &StateTile) -> bool {
        return self.id == other.tile.id
    }
}

impl<'a> fmt::Display for BaseTile<'a> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        Ok(for line in &self.data {
            match write!(f, "{}\n", line) {
                Ok(_) => {}
                Err(e) => return Err(e),
            }
        })
    }
}

impl<'a> fmt::Debug for BaseTile<'a> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match write!(
            f,
            "Tile ID: {}, Row amount: {}, Column amount: {}, Rows: \n",
            self.id, self.col_size, self.row_size
        ) {
            Ok(_) => {}
            Err(e) => return Err(e),
        }
        Ok(for line in &self.data {
            match write!(f, "{:?}\n", line) {
                Ok(_) => {}
                Err(e) => return Err(e),
            }
        })
    }
}

impl<'a> PartialEq for BaseTile<'a> {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}
