use crate::day;
use enum_iterator::Sequence;
use int_enum::IntEnum;
use itertools::Itertools;
use std::str::FromStr;

pub struct Day2 {}

#[repr(u8)]
#[derive(Clone, Copy, Debug, Eq, PartialEq, IntEnum, Sequence)]
enum Shape {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl FromStr for Shape {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" | "A" => Ok(Shape::Rock),
            "Y" | "B" => Ok(Shape::Paper),
            "Z" | "C" => Ok(Shape::Scissors),
            _ => Err(()),
        }
    }
}

impl Shape {
    fn new(shape: Shape, outcome: Outcome) -> Self {
        match outcome {
            Outcome::Draw => shape,
            Outcome::Win => enum_iterator::next_cycle(&shape).unwrap(),
            Outcome::Loss => enum_iterator::previous_cycle(&shape).unwrap(),
        }
    }
}

#[derive(Debug)]
struct Part1Round {
    opponent: Shape,
    player: Shape,
}

impl Part1Round {
    fn new(s: &str) -> Self {
        let (p1, p2) = s.split_whitespace().next_tuple().unwrap();
        Part1Round {
            opponent: Shape::from_str(p1).unwrap(),
            player: Shape::from_str(p2).unwrap(),
        }
    }
}

struct Part2Round {
    opponent: Shape,
    outcome: Outcome,
}

impl Part2Round {
    fn new(s: &str) -> Self {
        let (p, o) = s.split_whitespace().next_tuple().unwrap();
        Part2Round {
            opponent: Shape::from_str(p).unwrap(),
            outcome: Outcome::from_str(o).unwrap(),
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
    fn new(player: Shape, opponent: Shape) -> Self {
        if opponent == player {
            Outcome::Draw
        } else if opponent == enum_iterator::next_cycle(&player).unwrap() {
            Outcome::Loss
        } else {
            Outcome::Win
        }
    }
}

impl FromStr for Outcome {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(Outcome::Loss),
            "Y" => Ok(Outcome::Draw),
            "Z" => Ok(Outcome::Win),
            _ => Err(()),
        }
    }
}

impl day::Solution for Day2 {
    fn part1(s: &String) -> String {
        let rounds = s
            .split("\n")
            .map(|s| Part1Round::new(s))
            .collect::<Vec<Part1Round>>();

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
        let rounds = s
            .split("\n")
            .map(|s| Part2Round::new(s))
            .collect::<Vec<Part2Round>>();

        format!(
            "{}",
            rounds
                .iter()
                .map(
                    |r| (r.outcome.int_value() + Shape::new(r.opponent, r.outcome).int_value())
                        as u16
                )
                .sum::<u16>()
        )
    }
}
