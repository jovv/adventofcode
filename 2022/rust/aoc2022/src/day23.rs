use counter::Counter;
use itertools::{enumerate, Itertools};
use lazy_static::lazy_static;
use std::cmp;
use std::collections::{HashMap, VecDeque};

use crate::day;

// TODO: needs some serious performance optimization work
pub struct Day23 {}

const ELF: char = '#';
const EMPTY: char = '.';

lazy_static! {
    static ref DIRECTIONS: HashMap<&'static str, (i16, i16)> = HashMap::from_iter([
        ("N", (0, -1)),
        ("NE", (1, -1)),
        ("E", (1, 0)),
        ("SE", (1, 1)),
        ("S", (0, 1)),
        ("SW", (-1, 1)),
        ("W", (-1, 0)),
        ("NW", (-1, -1)),
    ]);
}

type Grid = Vec<Vec<char>>;
type Moves = HashMap<(usize, usize), (usize, usize)>;
type Surroundings = HashMap<&'static str, char>;

fn to_grid(lines: &Vec<String>) -> Vec<Vec<char>> {
    lines
        .iter()
        .map(|line| line.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>()
}

fn show_lines(lines: &Vec<String>) {
    println!("{}", lines.join("\n"))
}

fn show_grove(grid: &Vec<Vec<char>>) {
    println!(
        "{}",
        grid.iter()
            .map(|v| v.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join("\n")
    )
}

fn pad(lines: Vec<String>, padding: &usize) -> Vec<String> {
    let desired_width = lines[0].len() + (padding * 2);
    let row_padding = EMPTY.to_string().repeat(desired_width);
    let mut padded_grid = Vec::<String>::new();
    for _ in 0..*padding {
        padded_grid.push(row_padding.clone());
    }
    for row in lines {
        padded_grid.push(format!(
            "{p}{row}{p}",
            p = EMPTY.to_string().repeat(*padding)
        ));
    }
    for _ in 0..*padding {
        padded_grid.push(row_padding.clone());
    }
    padded_grid
}

fn cycle_directions_queue(queue: &mut VecDeque<char>) -> VecDeque<char> {
    let head = queue.pop_front().unwrap();
    let mut new_queue = queue.clone();
    new_queue.push_back(head);
    new_queue
}

fn surroundings(grid: &Grid, i: usize, j: usize) -> Surroundings {
    DIRECTIONS
        .iter()
        .map(|(direction, modifier)| {
            (
                *direction,
                grid[(j as i16 + modifier.1) as usize][(i as i16 + modifier.0) as usize],
            )
        })
        .collect::<Surroundings>()
}

fn are_surroundings_clear(surr: &Surroundings) -> bool {
    surr.iter().all(|(_, loc)| *loc == EMPTY)
}

fn is_valid_direction(direction: &char, surr: &Surroundings) -> bool {
    surr.iter()
        .filter(|(dir, _)| dir.chars().contains(direction))
        .all(|(_, val)| *val == EMPTY)
}

fn proposed_moves(grid: &Grid, directions: VecDeque<char>) -> Moves {
    let empty_row = EMPTY
        .to_string()
        .repeat(grid[0].len())
        .chars()
        .collect::<Vec<char>>();
    let mut proposed = HashMap::new();

    for (j, row) in enumerate(grid) {
        if *row == empty_row {
            continue;
        }
        for (i, col) in enumerate(row) {
            if *col == EMPTY {
                continue;
            }
            let surr = surroundings(&grid, i, j);
            if are_surroundings_clear(&surr) {
                continue;
            }
            for direction in &directions {
                if is_valid_direction(&direction, &surr) {
                    proposed.insert(
                        (i, j),
                        (
                            (i as i16 + DIRECTIONS[&direction.to_string()[..]].0) as usize,
                            (j as i16 + DIRECTIONS[&direction.to_string()[..]].1) as usize,
                        ),
                    );
                    break;
                }
            }
        }
    }

    proposed
}

fn move_all(grid: &Grid, moves: Moves) -> Grid {
    let mut new_grid = grid.clone();
    for (source, target) in moves {
        new_grid[source.1][source.0] = EMPTY;
        new_grid[target.1][target.0] = ELF;
    }
    new_grid
}

fn do_round(grid: Vec<Vec<char>>, directions: VecDeque<char>) -> (Grid, bool) {
    let proposed = proposed_moves(&grid, directions);
    if proposed.is_empty() {
        return (grid, true);
    }
    let target_counts = proposed.values().collect::<Counter<_>>();
    let move_conflicts = target_counts
        .into_iter()
        .filter(|(_, cnt)| *cnt > 1usize)
        .map(|(k, _)| *k)
        .collect::<Vec<(usize, usize)>>();
    let actual_moves = proposed
        .into_iter()
        .filter(|(_, target)| !move_conflicts.contains(target))
        .collect::<Moves>();
    let new_grid = move_all(&grid, actual_moves);
    (new_grid, false)
}

fn smallest_rectangle(grid: &Grid) -> (usize, usize, usize, usize) {
    let (mut min_x, mut min_y) = (grid[0].len(), grid.len());
    let (mut max_x, mut max_y) = (0, 0);
    for (j, row) in enumerate(grid) {
        for (i, col) in enumerate(row) {
            min_x = if *col == ELF {
                cmp::min(min_x, i)
            } else {
                min_x
            };
            max_x = if *col == ELF {
                cmp::max(max_x, i)
            } else {
                max_x
            };
            min_y = if *col == ELF {
                cmp::min(min_y, j)
            } else {
                min_y
            };
            max_y = if *col == ELF {
                cmp::max(max_y, j)
            } else {
                max_y
            };
        }
    }
    (min_x, min_y, max_x, max_y)
}

fn empty_ground_tiles(grid: &Grid, min_x: usize, min_y: usize, max_x: usize, max_y: usize) -> u32 {
    let mut cnt = 0u32;
    for (j, row) in enumerate(grid) {
        if j < min_y || j > max_y {
            continue;
        }
        for (i, col) in enumerate(row) {
            if i < min_x || i > max_x {
                continue;
            }
            if *col == EMPTY {
                cnt += 1;
            }
        }
    }
    cnt
}

impl day::Solution for Day23 {
    fn part1(s: &String) -> String {
        let lines = s
            .split_whitespace()
            .map(|line| line.to_string())
            .collect::<Vec<String>>();
        let rounds = 10;
        let padding = rounds.clone();
        let padded = pad(lines, &padding);
        let mut grove = to_grid(&padded);
        let mut directions_queue = VecDeque::from_iter(['N', 'S', 'W', 'E']);
        let mut stable = false;

        for _ in 1..=rounds {
            (grove, stable) = do_round(grove, directions_queue.clone());
            directions_queue = cycle_directions_queue(&mut directions_queue);
        }

        // show_grove(&grove);

        let (min_x, min_y, max_x, max_y) = smallest_rectangle(&grove);

        format!("{}", empty_ground_tiles(&grove, min_x, min_y, max_x, max_y))
    }

    fn part2(s: &String) -> String {
        let lines = s
            .split_whitespace()
            .map(|line| line.to_string())
            .collect::<Vec<String>>();
        let padding = 100;
        let padded = pad(lines, &padding);
        let mut grove = to_grid(&padded);
        let mut directions_queue = VecDeque::from_iter(['N', 'S', 'W', 'E']);
        let mut stable = false;
        let mut rounds = 1u32;
        loop {
            (grove, stable) = do_round(grove, directions_queue.clone());
            if stable {
                break;
            }
            directions_queue = cycle_directions_queue(&mut directions_queue);
            rounds += 1;
        }
        format!("{}", rounds)
    }
}
