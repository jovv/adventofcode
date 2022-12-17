use std::fs;
mod day;
mod day1;
mod day12;
mod day15;

use day::Solution;

fn main() {
    let day: u8 = 15;
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    match fs::read_to_string(&puzzle_input_filename) {
        Ok(s) => println!("{}", solution(day, s)),
        Err(e) => panic!("Failed to get puzzle input for {puzzle_input_filename}, msg: {e}"),
    }
}

fn solution(day: u8, s: String) -> day::Day {
    match day {
        1 => day1::Day1::new(s),
        12 => day12::Day12::new(s),
        15 => day15::Day15::new(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
