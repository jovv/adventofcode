use aoc2018::day1::Day1;
use std::fs;

fn main() {
    let day: u8 = 1;
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    let puzzle_input = fs::read_to_string(puzzle_input_filename).unwrap();
    println!("{}", solve(day, &puzzle_input));
}

fn solve(day: u8, s: &str) -> String {
    match day {
        1 => Day1::solution(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
