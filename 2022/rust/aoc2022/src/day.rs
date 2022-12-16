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
    fn new(s: String) -> Day {
        Day {
            part1: Self::part1(&s),
            part2: Self::part2(&s),
        }
    }
    fn part1(s: &String) -> String;
    fn part2(s: &String) -> String;
}
