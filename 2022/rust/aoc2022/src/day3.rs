use crate::day;
use itertools::Itertools;
use std::collections::{BTreeSet, HashSet};

const LOWERCASE_MODIFIER: u16 = 'a' as u16 - 1;
const UPPERCASE_MODIFIER: u16 = 'A' as u16 - 27;

pub struct Day3 {}

impl Day3 {
    fn score(c: &char) -> u16 {
        if c.is_lowercase() {
            *c as u16 - LOWERCASE_MODIFIER
        } else {
            *c as u16 - UPPERCASE_MODIFIER
        }
    }
    fn priority_pt1(s: &str) -> u16 {
        let (first, second) = s.split_at(s.len() / 2);
        let mut hs1 = BTreeSet::from_iter(first.chars().collect::<Vec<char>>());
        let hs2 = BTreeSet::from_iter(second.chars().collect::<Vec<char>>());
        hs1.retain(|c| hs2.contains(c));
        let item_type = Vec::from_iter::<BTreeSet<char>>(hs1)[0];
        Self::score(&item_type)
    }

    fn common_char(a: &Vec<char>, b: &Vec<char>, c: &Vec<char>) -> Option<char> {
        for x in a {
            if b.contains(&x) && c.contains(&x) {
                return Some(*x);
            }
        }
        None
    }
    // a reduce operation would've been cleaner but I couldn't get out of move/temp value compiler errors,
    // tried hashset.retain, intersection, contains
    fn priority_pt2(group: Vec<&str>) -> u16 {
        let a = group[0].chars().collect::<Vec<char>>();
        let b = group[1].chars().collect::<Vec<char>>();
        let c = group[2].chars().collect::<Vec<char>>();
        let item_type = Self::common_char(&a, &b, &c).expect("Couldn't find a common char");
        Self::score(&item_type)
    }
}

impl day::Solution for Day3 {
    fn part1(s: &String) -> String {
        format!(
            "{}",
            s.split_whitespace()
                .map(|s| Self::priority_pt1(s))
                .sum::<u16>()
        )
    }

    fn part2(s: &String) -> String {
        format!(
            "{}",
            s.split_whitespace()
                .collect::<Vec<&str>>()
                .chunks_exact(3)
                .map(|group| Self::priority_pt2(group.to_vec()))
                .sum::<u16>()
        )
    }
}
