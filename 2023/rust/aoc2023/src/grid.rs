#[derive(PartialEq, Debug, Clone)]
pub struct Grid(pub Vec<Vec<char>>);

impl Grid {
    pub fn from(s: &str, separator: char) -> Grid {
        Grid(
            s.split(separator)
                .map(|line| line.chars().collect())
                .collect(),
        )
    }

    pub fn new(v: Vec<Vec<char>>) -> Grid {
        Grid(v)
    }

    pub fn pad(self, x: usize, y: usize, fill: char) -> Grid {
        self.pad_x(x, fill).pad_y(y, fill)
    }

    fn nr_of_cols(&self) -> usize {
        self.0[0].len()
    }

    fn nr_of_rows(&self) -> usize {
        self.0.len()
    }

    pub fn dimensions(&self) -> (usize, usize) {
        (self.nr_of_rows(), self.nr_of_cols())
    }

    fn pad_x(self, x: usize, fill: char) -> Grid {
        if x == 0 {
            return self;
        }
        let padding = std::iter::repeat(fill).take(x).collect::<Vec<char>>();
        Grid(
            self.0
                .iter()
                .map(|line| [padding.clone(), line.to_vec(), padding.clone()].concat())
                .collect::<Vec<Vec<char>>>(),
        )
    }

    fn pad_y(self, y: usize, fill: char) -> Grid {
        if y == 0 {
            return self;
        }
        let line = std::iter::repeat(fill)
            .take(self.nr_of_cols())
            .collect::<Vec<char>>();
        Grid([vec![line.clone(); y], self.0, vec![line; y]].concat())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_from() {
        assert_eq!(
            Grid::from("12345\n67890", '\n'),
            Grid(vec![
                vec!['1', '2', '3', '4', '5'],
                vec!['6', '7', '8', '9', '0']
            ])
        );
    }

    #[test]
    fn test_pad_x() {
        assert_eq!(
            Grid::from("123\n456", '\n').pad_x(2, '.'),
            Grid(vec![
                vec!['.', '.', '1', '2', '3', '.', '.'],
                vec!['.', '.', '4', '5', '6', '.', '.'],
            ])
        )
    }

    #[test]
    fn test_pad_y() {
        assert_eq!(
            Grid::from("123\n456", '\n').pad_y(2, '.'),
            Grid(vec![
                vec!['.', '.', '.'],
                vec!['.', '.', '.'],
                vec!['1', '2', '3'],
                vec!['4', '5', '6'],
                vec!['.', '.', '.'],
                vec!['.', '.', '.']
            ])
        )
    }

    #[test]
    fn test_nr_of_cols() {
        assert_eq!(Grid::from("123\n456", '\n').nr_of_cols(), 3)
    }

    #[test]
    fn test_nr_of_rows() {
        assert_eq!(Grid::from("123\n456", '\n').nr_of_rows(), 2)
    }

    #[test]
    fn test_pad() {
        assert_eq!(
            Grid::from("123\n456", '\n').pad(2, 2, '.'),
            Grid(vec![
                vec!['.', '.', '.', '.', '.', '.', '.'],
                vec!['.', '.', '.', '.', '.', '.', '.'],
                vec!['.', '.', '1', '2', '3', '.', '.'],
                vec!['.', '.', '4', '5', '6', '.', '.'],
                vec!['.', '.', '.', '.', '.', '.', '.'],
                vec!['.', '.', '.', '.', '.', '.', '.'],
            ])
        )
    }
}
