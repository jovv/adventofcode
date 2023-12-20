pub struct Day1 {}

const WORDNUMS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

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
            .map(|s| s.chars().filter(|c| c.is_ascii_digit()).collect::<String>())
            .map(|t| {
                format!(
                    "{}{}",
                    t.chars().nth(0).unwrap(),
                    t.chars().nth_back(0).unwrap()
                )
            })
            .map(|s| s.parse::<i32>().unwrap())
            .sum::<i32>()
            .to_string()
    }

    fn pt2_forward(s: &str) -> String {
        let c = s.chars().nth(0).unwrap();
        if c.is_ascii_digit() {
            c.to_string()
        } else {
            for (i, wordnum) in WORDNUMS.iter().enumerate() {
                if s.starts_with(wordnum) {
                    return format!("{}", i + 1);
                }
            }
            "".to_string()
        }
    }

    fn pt2_backward(s: &str) -> String {
        let c = s.chars().nth_back(0).unwrap();
        if c.is_ascii_digit() {
            c.to_string()
        } else {
            for (i, wordnum) in WORDNUMS.iter().enumerate() {
                if s.ends_with(wordnum) {
                    return format!("{}", i + 1);
                }
            }
            "".to_string()
        }
    }

    fn pt2_cleaner(s: &str) -> String {
        let mut first: String = "".to_string();
        for n in 0..=s.chars().count() {
            let result = Self::pt2_forward(&s[n..]);
            if !result.is_empty() {
                first = result;
                break;
            }
        }

        let mut last: String = "".to_string();
        for n in (0..=s.chars().count()).rev() {
            let result = Self::pt2_backward(&s[..n]);
            if !result.is_empty() {
                last = result;
                break;
            }
        }

        format!("{}{}", first, last)
    }

    fn part2(s: &str) -> String {
        s.split('\n')
            .map(|s| Self::pt2_cleaner(s))
            .map(|s| s.parse::<i32>().unwrap())
            .sum::<i32>()
            .to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_pt2_forward() {
        assert_eq!(Day1::pt2_forward("1tt"), "1");
        assert_eq!(Day1::pt2_forward("ttt"), "");
        assert_eq!(Day1::pt2_forward("ninett"), "9");
        assert_eq!(Day1::pt2_forward("ttwot"), "");
    }

    #[test]
    fn test_pt2_backward() {
        assert_eq!(Day1::pt2_backward("tt9"), "9");
        assert_eq!(Day1::pt2_backward("ttt"), "");
        assert_eq!(Day1::pt2_backward("ttnine"), "9");
        assert_eq!(Day1::pt2_backward("ttwot"), "");
        assert_eq!(Day1::pt2_backward("two1nine"), "9")
    }

    #[test]
    fn test_pt2_cleaner() {
        assert_eq!(Day1::pt2_cleaner("two1nine"), "29");
        assert_eq!(Day1::pt2_cleaner("eightwothree"), "83");
        assert_eq!(Day1::pt2_cleaner("abcone2threexyz"), "13");
        assert_eq!(Day1::pt2_cleaner("xtwone3four"), "24");
        assert_eq!(Day1::pt2_cleaner("4nineeightseven2"), "42");
        assert_eq!(Day1::pt2_cleaner("zoneight234"), "14");
        assert_eq!(Day1::pt2_cleaner("7pqrstsixteen"), "76");
    }
}
