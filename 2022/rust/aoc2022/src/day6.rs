use crate::day;
use itertools::Itertools;
pub struct Day6 {}

impl Day6 {}

fn marker(cs: &[char], i: usize, len: usize) -> usize {
    if cs[i..i + len]
        .into_iter()
        .copied()
        .unique()
        .collect::<Vec<char>>()
        .len()
        == len
    {
        i + len
    } else {
        marker(cs, i + 1, len)
    }
}

impl day::Solution for Day6 {
    fn part1(s: &String) -> String {
        format!("{}", marker(&s.chars().collect::<Vec<char>>(), 0, 4))
    }

    fn part2(s: &String) -> String {
        format!("{}", marker(&s.chars().collect::<Vec<char>>(), 0, 14))
    }
}
