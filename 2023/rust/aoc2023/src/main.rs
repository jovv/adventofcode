use aoc2023::day1::Day1;
use aoc2023::day2::Day2;
use aoc2023::day3::Day3;
use std::fs;

fn main() {
    let day: u8 = 3;
    // let puzzle_input_filename = format!("./resources/day{day}-sample-pt1.txt");
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    let puzzle_input = fs::read_to_string(puzzle_input_filename).expect("a valid file");
    println!("{}", solve(day, &puzzle_input));
}

fn solve(day: u8, s: &str) -> String {
    match day {
        1 => Day1::solution(s),
        2 => Day2::solution(s),
        3 => Day3::solution(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
