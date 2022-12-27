use itertools::enumerate;

use crate::day;

pub struct Day25 {}

impl Day25 {}

fn to_decimal(s: &str) -> i64 {
    let mut x = 0i64;
    for (i, c) in enumerate(s.chars().rev()) {
        x += 5i64.pow(i as u32)
            * match c {
                '=' => -2,
                '-' => -1,
                _ => c.to_string().parse::<i64>().unwrap(),
            };
    }
    x
}

fn divmod(x: &i64) -> (i64, i64) {
    (x / 5, x % 5)
}

fn to_snafu_tail(dec: &i64, snafu: String) -> String {
    match dec {
        0 => snafu,
        _ => {
            let (div, rem) = divmod(&dec);
            let next_dec = if rem > 2 { div + 1 } else { div };
            to_snafu_tail(
                &next_dec,
                format!(
                    "{}{snafu}",
                    String::from("012=-").chars().collect::<Vec<char>>()[rem as usize]
                ),
            )
        }
    }
}

impl day::Solution for Day25 {
    fn part1(s: &String) -> String {
        let dec_sum = s.split_whitespace().map(|x| to_decimal(x)).sum::<i64>();

        format!("{}", to_snafu_tail(&dec_sum, String::from("")))
    }

    fn part2(s: &String) -> String {
        format!("{}", 0)
    }
}
