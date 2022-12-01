use std::fs;
mod day1;

fn main() {
    let day: u8 = 1;
    let puzzle_input_filename = format!("./resources/day{day}.txt");

    match fs::read_to_string(&puzzle_input_filename) {
        Ok(s) => {
            let (part1, part2) = solution(day, s);
            println!("{part1}\n{part2}");
        }
        Err(e) => panic!("Failed to get puzzle input for {puzzle_input_filename}, msg: {e}"),
    }
}

fn solution(day: u8, s: String) -> (String, String) {
    match day {
        1 => day1::solution(s),
        _ => panic!("No solution branch for day {day}"),
    }
}
