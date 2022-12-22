use std::{collections::HashSet, ops::RangeInclusive};

use crate::day;

pub struct Day4 {}

struct Section {
    pub start: u16,
    pub end: u16,
}

#[derive(Debug)]
struct Pair {
    a: RangeInclusive<u16>,
    b: RangeInclusive<u16>,
}

impl Pair {
    fn is_fully_contained(&self) -> bool {
        (self.a.start() >= self.b.start() && self.a.end() <= self.b.end())
            || (self.b.start() >= self.a.start() && self.b.end() <= self.a.end())
    }

    fn is_overlapping(&self) -> bool {
        let a: HashSet<u16> = HashSet::from_iter(self.a.clone());
        let b: HashSet<u16> = HashSet::from_iter(self.b.clone());
        a.intersection(&b).collect::<HashSet<_>>().len() > 0
    }
}

impl Day4 {
    fn pairs(s: &str) -> Pair {
        let pair = s
            .split(",")
            .map(|r| {
                let bounds = r.split("-").collect::<Vec<&str>>();
                Section {
                    start: bounds[0].parse::<u16>().unwrap(),
                    end: bounds[1].parse::<u16>().unwrap(),
                }
            })
            .collect::<Vec<Section>>();
        Pair {
            a: pair[0].start..=pair[0].end,
            b: pair[1].start..=pair[1].end,
        }
    }
}

impl day::Solution for Day4 {
    fn part1(s: &String) -> String {
        format!(
            "{}",
            s.split_whitespace()
                .map(|pair| Self::pairs(pair))
                .filter(|pair| pair.is_fully_contained())
                .collect::<Vec<Pair>>()
                .len()
        )
    }

    fn part2(s: &String) -> String {
        format!(
            "{}",
            s.split_whitespace()
                .map(|pair| Self::pairs(pair))
                .filter(|pair| pair.is_overlapping())
                .collect::<Vec<Pair>>()
                .len()
        )
    }
}
