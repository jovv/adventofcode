use regex::Regex;

use crate::grid::Grid;
use crate::grid_element::GridElement;

pub struct Day3 {}

#[derive(PartialEq, Debug, Clone)]
struct PartNumber {
    x: usize,
    y: usize,
    n: u32,
    n_len: usize,
}

#[derive(PartialEq, Debug)]
struct Gear {
    x: usize,
    y: usize,
}

impl Day3 {
    pub fn solution(puzzle_input: &str) -> String {
        format!(
            "{}\n{}",
            Self::part1(puzzle_input),
            Self::part2(puzzle_input)
        )
    }

    fn get_candidates(y: usize, line: Vec<char>) -> Vec<PartNumber> {
        let re = Regex::new(r"([0-9]{1,3})+").unwrap();
        let mut candidates = vec![];
        let s: String = line.into_iter().collect();
        for matched in re.find_iter(&s) {
            if let Ok(n) = matched.as_str().parse::<u32>() {
                candidates.push(PartNumber {
                    x: matched.start(),
                    y,
                    n,
                    n_len: n.to_string().chars().count(),
                })
            }
        }
        candidates
    }

    fn is_part_number(c: &PartNumber, grid: &Grid) -> bool {
        // left
        if grid.0[c.y][c.x - 1] != '.' {
            return true;
        }
        // right
        if grid.0[c.y][c.x + c.n_len] != '.' {
            return true;
        }
        // top
        for xx in (c.x - 1)..(c.x + c.n_len + 1) {
            if grid.0[c.y - 1][xx] != '.' {
                return true;
            }
        }
        // bottom
        for xx in (c.x - 1)..(c.x + c.n_len + 1) {
            if grid.0[c.y + 1][xx] != '.' {
                return true;
            }
        }
        false
    }

    fn part_numbers(g: &Grid) -> Vec<PartNumber> {
        g.0.iter()
            .enumerate()
            .flat_map(|(i, line)| Self::get_candidates(i, line.to_vec()))
            .filter(|candidate| Self::is_part_number(candidate, &g))
            .collect()
    }

    fn part1(s: &str) -> String {
        let grid = Grid::from(s, '\n').pad(1, 1, '.');

        Self::part_numbers(&grid)
            .iter()
            .map(|part_number| part_number.n)
            .sum::<u32>()
            .to_string()
    }

    fn get_gears(y: usize, line: Vec<char>) -> Vec<Gear> {
        line.iter()
            .enumerate()
            .filter(|(_, c)| **c == '*')
            .map(|(x, _)| Gear { x, y })
            .collect()
    }

    fn part2(s: &str) -> String {
        let grid = Grid::from(s, '\n').pad(1, 1, '\n');
        let part_numbers = Self::part_numbers(&grid);
        let gears = grid
            .0
            .iter()
            .enumerate()
            .flat_map(|(i, line)| Self::get_gears(i, line.clone()));

        let mut total = 0;
        for gear in gears {
            let adjacents = part_numbers
                .clone()
                .into_iter()
                .filter(|part_number| {
                    GridElement {
                        x: gear.x,
                        y: gear.y,
                        size: 1,
                    }
                    .is_adjacent(GridElement {
                        x: part_number.x,
                        y: part_number.y,
                        size: part_number.n_len,
                    })
                })
                .collect::<Vec<PartNumber>>();
            if adjacents.len() == 2 {
                total += adjacents
                    .iter()
                    .map(|part_number| part_number.n)
                    .product::<u32>();
            }
        }
        total.to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_candidates() {
        assert_eq!(
            Day3::get_candidates(0, "467..114..".chars().collect()),
            vec![
                PartNumber {
                    x: 0,
                    y: 0,
                    n: 467,
                    n_len: 3
                },
                PartNumber {
                    x: 5,
                    y: 0,
                    n: 114,
                    n_len: 3
                }
            ]
        );
    }

    #[test]
    fn test_part1() {
        assert_eq!(
            Day3::part1(
                "467..114..\n\
...*......\n\
..35...633\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598.."
            ),
            "4361"
        )
    }

    #[test]
    fn test_get_gears() {
        assert_eq!(
            Day3::get_gears(0, "...*......".chars().collect()),
            vec![Gear { x: 3, y: 0 }]
        );
    }

    // #[test]
    // fn test_part_numbers() {
    //     assert_eq!(
    //         Vec<
    //     )
    // }

    #[test]
    fn test_part2() {
        assert_eq!(
            Day3::part2(
                "467..114..\n\
...*......\n\
..35...633\n\
......#...\n\
617*......\n\
.....+.58.\n\
..592.....\n\
......755.\n\
...$.*....\n\
.664.598.."
            ),
            "467835"
        )
    }
}

/*
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
*/
