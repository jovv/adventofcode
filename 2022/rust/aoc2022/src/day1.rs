use std::fmt;

pub struct Day {
    part1: String,
    part2: String,
}

impl fmt::Display for Day {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}\n{}", self.part1, self.part2)
    }
}

pub trait Solution {
    fn new(s: String) -> Self;
    fn part1(s: String) -> String;
    fn part2(s: String) -> String;
}

impl Day {
    fn cargo_per_elf(s: String) -> Vec<u32> {
        s.clone()
            .split("\n\n")
            .map(|s| s.split_whitespace().map(|s| s.parse::<u32>().unwrap()))
            .map(|xs| xs.sum())
            .collect()
    }
}

impl Solution for Day {
    fn new(s: String) -> Day {
        Day {
            part1: Self::part1(s.clone()),
            part2: Self::part2(s),
        }
    }

    fn part1(s: String) -> String {
        format!("{}", Self::cargo_per_elf(s).iter().max().unwrap())
    }

    fn part2(s: String) -> String {
        let mut cpe = Self::cargo_per_elf(s);
        cpe.sort();
        cpe.reverse();
        format!("{}", cpe[0..3].iter().sum::<u32>())
    }
}
