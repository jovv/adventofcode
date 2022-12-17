use lazy_static::lazy_static;
use regex::Regex;
use std::cmp;
use std::collections::HashSet;

use crate::day;

pub struct Day15 {}

impl Day15 {
    fn sensor_coverages(lines: &Vec<&str>, row: i32) -> (Vec<(i32, i32)>, HashSet<(i32, i32)>) {
        lazy_static! {
            static ref COORDS: Regex = Regex::new(
                r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
            )
            .unwrap();
        }
        let mut coverage = Vec::<(i32, i32)>::new();
        let mut row_beacons = HashSet::<(i32, i32)>::new();

        for line in lines {
            let groups = COORDS.captures(line).expect("Regex didn't match");
            let (sensor_x, sensor_y, beacon_x, beacon_y) = (
                groups[1].parse::<i32>().unwrap(),
                groups[2].parse::<i32>().unwrap(),
                groups[3].parse::<i32>().unwrap(),
                groups[4].parse::<i32>().unwrap(),
            );
            if beacon_y == row {
                row_beacons.insert((beacon_x, beacon_y));
            }
            let manhattan_distance = (sensor_x - beacon_x).abs() + (sensor_y - beacon_y).abs();
            // break up the full distance in a Y and X part
            let remaining_distance = manhattan_distance - (row - sensor_y).abs();
            if remaining_distance < 0 {
                println!("{}", remaining_distance);
                continue;
            }
            // get the coverage on the x axis and store it
            coverage.push((sensor_x - remaining_distance, sensor_x + remaining_distance))
        }
        (coverage, row_beacons)
    }

    fn span_at_row(coverages: &Vec<(i32, i32)>, row_beacons: &HashSet<(i32, i32)>) -> i32 {
        let mut beacons_in_coverage = 0i32;
        let coverage = coverages
            .iter()
            .copied()
            .reduce(|acc, cov| (cmp::min(acc.0, cov.0), cmp::max(acc.1, cov.1)))
            .expect("Couldn't reduce intervals");
        for row_beacon in row_beacons {
            if (coverage.0..=coverage.1).contains(&row_beacon.0) {
                beacons_in_coverage += 1;
            }
        }
        coverage.1 - coverage.0 - beacons_in_coverage + 1
    }
}

impl day::Solution for Day15 {
    fn part1(s: &String) -> String {
        let lines = s.split("\n").collect::<Vec<&str>>();
        // let row = 10i32;
        let row = 2000000i32;
        let (coverages, row_beacons) = Self::sensor_coverages(&lines, row);
        println!("{:?}\n{:?}", coverages, row_beacons);
        format!("{}", Self::span_at_row(&coverages, &row_beacons))
    }

    fn part2(s: &String) -> String {
        format!("{:?}", 0)
    }
}
