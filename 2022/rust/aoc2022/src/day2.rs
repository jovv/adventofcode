use crate::day;
use int_enum::IntEnum;
use itertools::Itertools;
use std::str::FromStr;

pub struct Day2 {}

#[repr(u8)]
#[derive(Clone, Copy, Debug, Eq, PartialEq, IntEnum)]
enum ShapeScore {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl FromStr for ShapeScore {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" | "A" => Ok(ShapeScore::Rock),
            "Y" | "B" => Ok(ShapeScore::Paper),
            "Z" | "C" => Ok(ShapeScore::Scissors),
            _ => Err(()),
        }
    }
}

#[derive(Debug)]
struct Round {
    opponent: ShapeScore,
    player: ShapeScore,
}

impl Round {
    fn new(s: &str) -> Self {
        let (p1, p2) = s.split_whitespace().next_tuple().unwrap();
        Round {
            opponent: ShapeScore::from_str(p1).unwrap(),
            player: ShapeScore::from_str(p2).unwrap(),
        }
    }
}

#[repr(u8)]
#[derive(Clone, Copy, Debug, Eq, PartialEq, IntEnum)]
enum Outcome {
    Win = 6,
    Draw = 3,
    Loss = 0,
}

impl Outcome {
    fn new(player: ShapeScore, opponent: ShapeScore) -> Self {
        match player.int_value() as i8 - opponent.int_value() as i8 {
            0 => Outcome::Draw,
            1 | -2 => Outcome::Win,
            _ => Outcome::Loss,
        }
    }
}

impl day::Solution for Day2 {
    fn part1(s: &String) -> String {
        let rounds = s.split("\n").map(|s| Round::new(s)).collect::<Vec<Round>>();

        format!(
            "{:?}",
            rounds
                .iter()
                .map(
                    |r| (Outcome::new(r.player, r.opponent).int_value() + r.player.int_value())
                        as u16
                )
                .sum::<u16>()
        )
    }

    fn part2(s: &String) -> String {
        0.to_string()
        // s.to_string()
        // format!(
        //     "{}",
        //     s.split("\n")
        //         .map(|x| Self::apply_elves_score(x))
        //         .sum::<u8>()
        // )
    }
}
