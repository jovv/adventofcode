use std::fs;

pub fn get_test_input(day: u8) -> String {
    let puzzle_input_filename = format!("./resources/day{day}-test.txt");
    fs::read_to_string(&puzzle_input_filename).ok().unwrap()
}
