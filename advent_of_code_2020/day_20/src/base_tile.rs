use std::fmt;

#[derive(Clone)]
pub struct BaseTile {
    pub id: u32,
    data: Vec<String>,
    pub row_size: usize,
    pub col_size: usize,
}

impl BaseTile {
    pub fn new(id: u32) -> Self {
        BaseTile {
            id: id,
            data: vec![],
            row_size: 0,
            col_size: 0,
        }
    }

    pub fn insert_row(&mut self, row: &str) {
        if self.row_size == 0 {
            self.row_size = row.len();
        }
        if self.row_size != row.len() {
            println!("Couldn't insert \"{}\", as size to previous differs", row);
            return;
        }
        self.data.push(row.into());
        self.col_size += 1;
    }

    pub fn get_row(&self, index: usize) -> Option<String> {
        if self.col_size == 0 || self.col_size <= index {
            return None;
        }
        let string = self.data.get(index).unwrap();
        Some(string.into())
    }

    pub fn get_col(&self, index: usize) -> Option<String> {
        if self.row_size == 0 || self.row_size <= index {
            return None;
        }
        let mut col = String::new();
        for row in &self.data {
            col.push(row.chars().nth(index).unwrap());
        }
        Some(col)
    }
}

impl fmt::Display for BaseTile {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        Ok(for line in &self.data {
            match write!(f, "{}\n", line) {
                Ok(_) => {}
                Err(e) => return Err(e),
            }
        })
    }
}

impl fmt::Debug for BaseTile {
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

impl PartialEq for BaseTile {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}
