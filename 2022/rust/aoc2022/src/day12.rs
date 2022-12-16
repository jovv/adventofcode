use itertools::enumerate;
use std::collections::{HashSet, VecDeque};
use std::fs;

use crate::day;

pub struct Day12 {}

impl Day12 {
    fn show_path(path: &Vec<Vec<char>>) {
        let s = path
            .iter()
            .map(|chars| format!("{}\n", chars.into_iter().collect::<String>()))
            .collect::<String>();
        fs::write("path.txt", s).ok();
    }

    fn start_position(grid: &Vec<Vec<char>>, start_char: char) -> Option<(usize, usize)> {
        for (j, row) in enumerate(grid) {
            for (i, col) in enumerate(row) {
                if *col == start_char {
                    return Some((i, j));
                }
            }
        }
        None
    }

    fn neighbours_within_bounds(
        x: usize,
        y: usize,
        width: usize,
        height: usize,
    ) -> Vec<(usize, usize)> {
        let mut neighbours = Vec::<(usize, usize)>::new();
        match x.checked_sub(1) {
            None => (),
            Some(i) => neighbours.push((i, y)),
        };
        if x + 1 < width {
            neighbours.push((x + 1, y));
        }
        match y.checked_sub(1) {
            None => (),
            Some(j) => neighbours.push((x, j)),
        };
        if y + 1 < height {
            neighbours.push((x, y + 1));
        }
        neighbours
    }

    fn can_climb(grid: &Vec<Vec<char>>, neighbour: (usize, usize), elevation: char) -> bool {
        let curr_val = if elevation == 'E' { 'z' } else { elevation };
        let dest_val = if grid[neighbour.1][neighbour.0] == 'S' {
            'a'
        } else {
            grid[neighbour.1][neighbour.0]
        };
        curr_val as u8 <= dest_val as u8 + 1
    }

    fn shortest_path(grid: &Vec<Vec<char>>, start: (usize, usize), target: char) -> u32 {
        let mut queue = VecDeque::<((usize, usize), u32)>::from([(start, 0)]);
        let mut visited = HashSet::<(usize, usize)>::from([start]);
        let mut path = grid.clone();

        while !queue.is_empty() {
            let ((x, y), steps) = queue.pop_front().unwrap();
            let elevation = grid[y][x];
            if elevation == target {
                Self::show_path(&path);
                return steps;
            }
            for neighbour in Self::neighbours_within_bounds(x, y, grid[0].len(), grid.len()) {
                if Self::can_climb(&grid, neighbour, elevation)
                    && visited.insert((neighbour.0, neighbour.1))
                {
                    queue.push_back((neighbour, steps + 1));
                    path[neighbour.1][neighbour.0] = '*';
                }
            }
        }
        Self::show_path(&path);
        panic!("Couldn't find a path")
    }
}

impl day::Solution for Day12 {
    fn part1(s: &String) -> String {
        let grid = s
            .split_whitespace()
            .map(|s| s.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();

        let start = Self::start_position(&grid, 'E').expect("Couldn't find a start position");
        format!("{:?}", Self::shortest_path(&grid, start, 'S'))
    }

    fn part2(s: &String) -> String {
        let grid = s
            .split_whitespace()
            .map(|s| s.chars().collect::<Vec<char>>())
            .collect::<Vec<Vec<char>>>();

        let start = Self::start_position(&grid, 'E').expect("Couldn't find a start position");
        format!("{:?}", Self::shortest_path(&grid, start, 'a'))
    }
}
