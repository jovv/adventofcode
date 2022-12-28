use crate::day;
use itertools::enumerate;
use lazy_static::lazy_static;
use regex::Regex;
pub struct Day5 {}

type Crates = Vec<Vec<char>>;

#[derive(Debug)]
struct Move {
    cnt: usize,
    source: usize,
    target: usize,
}

fn transpose(css: Crates) -> Crates {
    let rows = css.len();
    let columns = css[0].len();
    let (t_rows, t_cols) = (columns, rows);
    let mut transposed = vec![vec![' '; t_cols]; t_rows];
    for (j, cs) in enumerate(css) {
        for (i, c) in enumerate(cs) {
            transposed[i][j] = c
        }
    }
    transposed
}

fn to_lines(s: &str) -> Vec<&str> {
    s.split("\n").collect::<Vec<&str>>()
}

fn to_crates(lines: Vec<&str>) -> Crates {
    let pad_to = lines.iter().copied().map(|line| line.len()).max().unwrap();
    let raw_grid = lines
        .iter()
        .copied()
        .map(|l| format!("{:width$}", l, width = pad_to))
        .map(|l| l.chars().collect::<Vec<char>>())
        .collect::<Crates>();
    let transposed = transpose(raw_grid);
    transposed
        .into_iter()
        .map(|xs| {
            xs.iter()
                .copied()
                .filter(|c| c.is_ascii_uppercase())
                .collect::<Vec<char>>()
        })
        .filter(|xs| !xs.is_empty())
        .map(|mut xs| {
            xs.reverse();
            xs
        })
        .collect::<Crates>()
}

fn to_moves(lines: Vec<&str>) -> Vec<Move> {
    lazy_static! {
        static ref MOVE_RE: Regex = Regex::new(r"\d+").unwrap();
    }

    lines
        .iter()
        .copied()
        .map(|line| {
            let groups = MOVE_RE
                .find_iter(line)
                .map(|i| i.as_str().parse::<u16>().unwrap())
                .collect::<Vec<u16>>();
            Move {
                cnt: groups[0] as usize,
                source: groups[1] as usize,
                target: groups[2] as usize,
            }
        })
        .collect::<Vec<Move>>()
}

fn move_crates(crates: Crates, moves: &Vec<Move>) -> Crates {
    let mut rearranged = crates;
    for mv in moves {
        for _ in 1..=mv.cnt {
            let crt = rearranged[mv.source - 1].pop().unwrap();
            rearranged[mv.target - 1].push(crt);
        }
    }
    rearranged
}

fn move_crates_9001(crates: Crates, moves: &Vec<Move>) -> Crates {
    let mut rearranged = crates;
    let mut bulk = Vec::new();
    for mv in moves {
        for _ in 1..=mv.cnt {
            let crt = rearranged[mv.source - 1].pop().unwrap();
            bulk.push(crt);
        }
        bulk.reverse();
        for crt in &bulk {
            rearranged[mv.target - 1].push(*crt);
        }
        bulk.clear();
    }
    rearranged
}

fn top_crates_per_stack(crates: &Crates) -> String {
    crates
        .into_iter()
        .map(|stack| *stack.last().unwrap())
        .collect::<Vec<char>>()
        .into_iter()
        .collect::<String>()
}

impl day::Solution for Day5 {
    fn part1(s: &String) -> String {
        let input = s.split("\n\n").collect::<Vec<&str>>();
        let crates = to_crates(to_lines(input[0]));
        let moves = to_moves(to_lines(input[1]));
        let rearranged = move_crates(crates, &moves);

        format!("{}", top_crates_per_stack(&rearranged))
    }

    fn part2(s: &String) -> String {
        let input = s.split("\n\n").collect::<Vec<&str>>();
        let crates = to_crates(to_lines(input[0]));
        let moves = to_moves(to_lines(input[1]));
        let rearranged = move_crates_9001(crates, &moves);

        format!("{}", top_crates_per_stack(&rearranged))
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn transpose_vec_of_vecs() {
        let input = vec![
            vec!['a', 'b', 'c'],
            vec!['d', 'e', 'f'],
            vec!['g', 'i', 'j'],
        ];
        let expected = vec![
            vec!['a', 'd', 'g'],
            vec!['b', 'e', 'i'],
            vec!['c', 'f', 'j'],
        ];
        assert_eq!(transpose(input), expected);
    }
}
