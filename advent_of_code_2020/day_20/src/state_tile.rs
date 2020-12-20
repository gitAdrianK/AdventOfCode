use crate::base_tile::BaseTile;
use std::slice::Iter;
use std::fmt;

#[derive(Clone)]
pub struct StateTile<'a> {
    pub tile: BaseTile<'a>,
    state: (Turn, Flip),
}

#[allow(dead_code)]
impl<'a> StateTile<'a> {
    pub fn new(tile: &BaseTile<'a>) -> Self {
        StateTile {
            tile: tile.clone(),
            state: (Turn::default(), Flip::default()),
        }
    }

    pub fn new_with_state(tile: &BaseTile<'a>, turn: Turn, flip: Flip) -> Self {
        StateTile {
            tile: tile.clone(),
            state: (turn, flip),
        }
    }

    pub fn get_variants(tile: &BaseTile<'a>) -> Vec<Self> {
        let mut variants: Vec<StateTile> = vec![];
        for t in Turn::iterator() {
            for f in Flip::iterator() {
                variants.push(StateTile::new_with_state(tile, *t, *f));
            }
        }
        variants
    }

    // Writing the cases is just tedious, if I was smart I would make
    // A matrix and apply a rotation to it and call it a day,
    // but I don't want to use another external crate like
    // the regex one, it's just that regex is too good to give up,
    // because I would find a crate that does exactly what I want 100%

    pub fn get_top_edge(&self) -> Option<String> {
        match self.state {
            // No turns
            (Turn::NoTurn, Flip::NoFlip) => self.tile.get_top_edge(),
            (Turn::NoTurn, Flip::Horizontal) => self.tile.get_bottom_edge(),
            (Turn::NoTurn, Flip::Vertical) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Left turns
            (Turn::Left, Flip::NoFlip) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Horizontal) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Vertical) => self.tile.get_left_edge(),
            // Right turns
            (Turn::Right, Flip::NoFlip) => self.tile.get_right_edge(),
            (Turn::Right, Flip::Horizontal) => self.tile.get_left_edge(),
            (Turn::Right, Flip::Vertical) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Upside down turns
            (Turn::UpsideDown, Flip::NoFlip) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Horizontal) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Vertical) => self.tile.get_bottom_edge(),
        }
    }

    pub fn get_bottom_edge(&self) -> Option<String> {
        match self.state {
            // No turns
            (Turn::NoTurn, Flip::NoFlip) => self.tile.get_bottom_edge(),
            (Turn::NoTurn, Flip::Horizontal) => self.tile.get_top_edge(),
            (Turn::NoTurn, Flip::Vertical) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Left turns
            (Turn::Left, Flip::NoFlip) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Horizontal) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Vertical) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Right turns
            (Turn::Right, Flip::NoFlip) => self.tile.get_left_edge(),
            (Turn::Right, Flip::Horizontal) => self.tile.get_right_edge(),
            (Turn::Right, Flip::Vertical) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Upside down turns
            (Turn::UpsideDown, Flip::NoFlip) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Horizontal) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Vertical) => self.tile.get_top_edge(),
        }
    }

    pub fn get_left_edge(&self) -> Option<String> {
        match self.state {
            // No turns
            (Turn::NoTurn, Flip::NoFlip) => self.tile.get_left_edge(),
            (Turn::NoTurn, Flip::Horizontal) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::NoTurn, Flip::Vertical) => self.tile.get_right_edge(),
            // Left turns
            (Turn::Left, Flip::NoFlip) => self.tile.get_bottom_edge(),
            (Turn::Left, Flip::Horizontal) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Vertical) => self.tile.get_top_edge(),
            // Right turns
            (Turn::Right, Flip::NoFlip) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Right, Flip::Horizontal) => self.tile.get_top_edge(),
            (Turn::Right, Flip::Vertical) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Upside down turns
            (Turn::UpsideDown, Flip::NoFlip) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Horizontal) => self.tile.get_right_edge(),
            (Turn::UpsideDown, Flip::Vertical) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
        }
    }

    pub fn get_right_edge(&self) -> Option<String> {
        match self.state {
            // No turns
            (Turn::NoTurn, Flip::NoFlip) => self.tile.get_right_edge(),
            (Turn::NoTurn, Flip::Horizontal) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::NoTurn, Flip::Vertical) => self.tile.get_left_edge(),
            // Left turns
            (Turn::Left, Flip::NoFlip) => self.tile.get_top_edge(),
            (Turn::Left, Flip::Horizontal) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Left, Flip::Vertical) => self.tile.get_bottom_edge(),
            // Right turns
            (Turn::Right, Flip::NoFlip) => match self.tile.get_bottom_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::Right, Flip::Horizontal) => self.tile.get_bottom_edge(),
            (Turn::Right, Flip::Vertical) => match self.tile.get_top_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            // Upside down turns
            (Turn::UpsideDown, Flip::NoFlip) => match self.tile.get_left_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
            (Turn::UpsideDown, Flip::Horizontal) => self.tile.get_left_edge(),
            (Turn::UpsideDown, Flip::Vertical) => match self.tile.get_right_edge() {
                Some(top) => {
                    let rev = top.chars().rev().collect();
                    Some(rev)
                }
                None => None,
            },
        }
    }

    pub fn cmp_with_basetile(&self, other: &BaseTile) -> bool {
        return self.tile.id == other.id
    }
}

impl<'a> fmt::Debug for StateTile<'a> {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:?}", self.tile.id)
    }
}

#[derive(Clone, Copy, Debug, PartialEq)]
pub enum Turn {
    NoTurn,
    Left,
    Right,
    UpsideDown,
}

impl Turn {
    pub fn iterator() -> Iter<'static, Turn> {
        static TURNS: [Turn; 4] = [Turn::NoTurn, Turn::Left, Turn::Right, Turn::UpsideDown];
        TURNS.iter()
    }
}

impl Default for Turn {
    fn default() -> Self {
        Turn::NoTurn
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Flip {
    NoFlip,
    Horizontal,
    Vertical,
}

impl Flip {
    pub fn iterator() -> Iter<'static, Flip> {
        static FLIPS: [Flip; 3] = [Flip::NoFlip, Flip::Horizontal, Flip::Vertical];
        FLIPS.iter()
    }
}

impl Default for Flip {
    fn default() -> Self {
        Flip::NoFlip
    }
}
