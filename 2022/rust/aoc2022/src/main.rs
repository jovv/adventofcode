use std::fs;
mod day1;

use day1::Solution;

fn main() {
    let day: u8 = 1;
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    match fs::read_to_string(&puzzle_input_filename) {
        Ok(s) => println!("{}", solution(day, s)),
        Err(e) => panic!("Failed to get puzzle input for {puzzle_input_filename}, msg: {e}"),
    }
}

fn solution(day: u8, s: String) -> day1::Day {
    match day {
        1 => day1::Day::new(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
