use aoc2022::{day::Solution, day5::Day5};

mod common;

#[test]
fn day5_part1() {
    assert_eq!(Day5::part1(&common::get_test_input(5)), "CMZ");
}

#[test]
fn day5_part2() {
    assert_eq!(Day5::part2(&common::get_test_input(5)), "MCD");
}
