use std::fs;

pub fn get_test_input(day: u8) -> String {
    let puzzle_input_filename = format!("./tests/resources/day{day}-test.txt");
    match fs::read_to_string(&puzzle_input_filename) {
        Ok(s) => s,
        Err(e) => panic!("Failed to get puzzle input for {puzzle_input_filename}, msg: {e}"),
    }
}
