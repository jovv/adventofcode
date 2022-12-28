use aoc2022::{day::Solution, day6::Day6};

mod common;

#[test]
fn day6_part1() {
    assert_eq!(Day6::part1(&common::get_test_input(6)), "7");
}

#[test]
fn day6_part2() {
    assert_eq!(Day6::part2(&common::get_test_input(6)), "19");
}
