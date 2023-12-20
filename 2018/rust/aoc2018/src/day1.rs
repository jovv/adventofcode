use std::collections::HashSet;

pub struct Day1 {}

impl Day1 {
    pub fn solution(puzzle_input: &str) -> String {
        format!(
            "{}\n{}",
            Self::part1(puzzle_input),
            Self::part2(puzzle_input)
        )
    }
    fn part1(s: &str) -> String {
        s.split('\n')
            .map(|s| s.parse::<i32>().unwrap())
            .sum::<i32>()
            .to_string()
    }

    fn part2(s: &str) -> String {
        let xs = s.split('\n').map(|s| s.parse::<i32>().unwrap());
        let mut freqs: HashSet<i32> = HashSet::new();
        freqs.insert(0);
        let mut curr_freq: i32 = 0;
        let mut calibrated = false;
        while !calibrated {
            for x in xs.clone() {
                curr_freq += x;
                if !freqs.insert(curr_freq) {
                    calibrated = true;
                    break;
                }
            }
        }
        curr_freq.to_string()
    }
}
