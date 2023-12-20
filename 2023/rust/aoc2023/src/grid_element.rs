pub struct GridElement {
    pub x: usize,
    pub y: usize,
    pub size: usize,
}

impl GridElement {
    pub fn is_adjacent(self, other: GridElement) -> bool {
        // let "self" be A and "other" B, then

        if self.y == other.y {
            // left
            // 0123456789
            // ..BBBAAA..
            if self.x == other.x + other.size {
                return true;
            }
            // right
            // 0123456789
            // ..AAABBB..
            if self.x + self.size == other.x {
                return true;
            }
        }

        // top or bottom
        if (self.y - 1) == other.y || (self.y + 1) == other.y {
            // 0123456789
            // ....B.....
            // .....A....
            if other.x < self.x && other.x + other.size >= self.x {
                return true;
            }
            // 0123456789
            // ......B...
            // .....A....
            if other.x == self.x + 1 {
                return true;
            }
            // 0123456789
            // .....BB...
            // .....A....
            if other.x == self.x {
                return true;
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_adjacent_left() {
        // 0123456789
        // ..BBBAAA..
        assert!(GridElement {
            x: 5,
            y: 2,
            size: 3
        }
        .is_adjacent(GridElement {
            x: 2,
            y: 2,
            size: 3
        }));

        // 0123456789
        // ..BB.AAA..
        assert!(!GridElement {
            x: 5,
            y: 2,
            size: 3
        }
        .is_adjacent(GridElement {
            x: 2,
            y: 2,
            size: 2
        }));
    }

    #[test]
    fn test_is_adjacent_right() {
        // right
        // 0123456789
        // ..AAABBB..
        assert!(GridElement {
            x: 2,
            y: 2,
            size: 3
        }
        .is_adjacent(GridElement {
            x: 5,
            y: 2,
            size: 3
        }));
        // right
        // 0123456789
        // ..AA.BBB..
        assert!(!GridElement {
            x: 2,
            y: 2,
            size: 2
        }
        .is_adjacent(GridElement {
            x: 5,
            y: 2,
            size: 3
        }));
    }

    #[test]
    fn test_is_adjacent_top_or_bottom() {
        // 0123456789
        // ..BB......
        // ....AAA...
        assert!(GridElement {
            x: 4,
            y: 2,
            size: 3
        }
        .is_adjacent(GridElement {
            x: 2,
            y: 1,
            size: 2
        }));
        // 0123456789
        // ...BBB....
        // ....A.....
        assert!(GridElement {
            x: 4,
            y: 2,
            size: 1
        }
        .is_adjacent(GridElement {
            x: 3,
            y: 1,
            size: 3
        }));
        // 0123456789
        // .....BBB..
        // ....A.....
        assert!(GridElement {
            x: 4,
            y: 2,
            size: 1
        }
        .is_adjacent(GridElement {
            x: 5,
            y: 1,
            size: 3
        }));
        // 0123456789
        // ....BBB...
        // ....A.....
        assert!(GridElement {
            x: 4,
            y: 2,
            size: 1
        }
        .is_adjacent(GridElement {
            x: 4,
            y: 1,
            size: 3
        }));
    }
    #[test]
    fn is_not_adjacent_top_or_bottom() {
        // 0123456789
        // ......BBB.
        // ....A.....
        assert!(!GridElement {
            x: 4,
            y: 2,
            size: 1
        }
        .is_adjacent(GridElement {
            x: 6,
            y: 1,
            size: 3
        }));
        // 0123456789
        // .BB.......
        // ....AAA...
        assert!(!GridElement {
            x: 4,
            y: 2,
            size: 3
        }
        .is_adjacent(GridElement {
            x: 1,
            y: 1,
            size: 2
        }));
    }
}
