use crate::day;

pub struct Day1 {}

impl Day1 {
    fn cargo_per_elf(s: &String) -> Vec<u32> {
        s.clone()
            .split("\n\n")
            .map(|s| s.split_whitespace().map(|s| s.parse::<u32>().unwrap()))
            .map(|xs| xs.sum())
            .collect()
    }
}

impl day::Solution for Day1 {
    fn part1(s: &String) -> String {
        format!("{}", Self::cargo_per_elf(s).iter().max().unwrap())
    }

    fn part2(s: &String) -> String {
        let mut cpe = Self::cargo_per_elf(s);
        cpe.sort();
        cpe.reverse();
        format!("{}", cpe[0..3].iter().sum::<u32>())
    }
}
