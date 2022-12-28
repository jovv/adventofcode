use aoc2022::day::{Day, Solution};
use aoc2022::day1::Day1;
use aoc2022::day12::Day12;
use aoc2022::day15::Day15;
use aoc2022::day2::Day2;
use aoc2022::day23::Day23;
use aoc2022::day25::Day25;
use aoc2022::day3::Day3;
use aoc2022::day4::Day4;
use aoc2022::day5::Day5;
use std::fs;

fn main() {
    let day: u8 = 5;
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    match fs::read_to_string(&puzzle_input_filename) {
        Ok(s) => println!("{}", solution(day, s)),
        Err(e) => panic!("Failed to get puzzle input for {puzzle_input_filename}, msg: {e}"),
    }
}

fn solution(day: u8, s: String) -> Day {
    match day {
        1 => Day1::new(s),
        2 => Day2::new(s),
        3 => Day3::new(s),
        4 => Day4::new(s),
        5 => Day5::new(s),
        12 => Day12::new(s),
        15 => Day15::new(s),
        23 => Day23::new(s),
        25 => Day25::new(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
