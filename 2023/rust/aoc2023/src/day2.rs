use std::cmp;

pub struct Day2 {}

const RED_LIMIT: u32 = 12;
const GREEN_LIMIT: u32 = 13;
const BLUE_LIMIT: u32 = 14;

impl Day2 {
    pub fn solution(puzzle_input: &str) -> String {
        format!(
            "{}\n{}",
            Self::part1(puzzle_input),
            Self::part2(puzzle_input)
        )
    }

    fn game_id(game: &str) -> u32 {
        game.split(':')
            .nth(0)
            .unwrap()
            .split(' ')
            .nth(1)
            .unwrap()
            .parse::<u32>()
            .unwrap()
    }

    fn pt1_game_data(game: &str) -> Option<u32> {
        let id = Self::game_id(game);
        let colors = game.split(':').nth(1).unwrap().trim();
        let set = colors.split(';').map(|s| s.trim());
        for score in set {
            let cubes = score.split(',').map(|s| s.trim());
            for cube in cubes {
                let (num, color) = cube.split_once(' ').unwrap();
                let cnt = num.parse::<u32>().unwrap();
                match color {
                    "red" => {
                        if cnt > RED_LIMIT {
                            return None;
                        }
                    }
                    "green" => {
                        if cnt > GREEN_LIMIT {
                            return None;
                        }
                    }
                    "blue" => {
                        if cnt > BLUE_LIMIT {
                            return None;
                        }
                    }
                    _ => panic!("color not recognized"),
                }
            }
        }
        Some(id)
    }

    fn pt2_game_power(game: &str) -> u32 {
        let colors = game.split(':').nth(1).unwrap();
        let color_quantities = colors.split(&[';', ','][..]).map(|s| s.trim());
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        for cq in color_quantities {
            let (num, color) = cq.split_once(' ').unwrap();
            let cnt = num.parse::<u32>().unwrap();
            match color {
                "red" => red = cmp::max(red, cnt),
                "green" => green = cmp::max(green, cnt),
                "blue" => blue = cmp::max(blue, cnt),
                _ => panic!("color not recognized"),
            }
        }
        red * green * blue
    }

    fn part1(s: &str) -> String {
        format!(
            "{}",
            s.split('\n')
                .map(Self::pt1_game_data)
                .filter(|x| x.is_some())
                .flatten()
                .sum::<u32>()
        )
    }
    fn part2(s: &str) -> String {
        format!("{}", s.split('\n').map(Self::pt2_game_power).sum::<u32>())
    }
}

// Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
// Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
// Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
// Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
// Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_game_id() {
        assert_eq!(
            Day2::game_id("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
            1
        )
    }

    #[test]
    fn test_game_data() {
        assert_eq!(
            Day2::pt2_game_power("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"),
            48
        );
        assert_eq!(
            Day2::pt2_game_power(
                "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
            ),
            12
        );
        assert_eq!(
            Day2::pt2_game_power(
                "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
            ),
            1560
        );
        assert_eq!(
            Day2::pt2_game_power(
                "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
            ),
            630
        );
        assert_eq!(
            Day2::pt2_game_power("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"),
            36
        );
    }

    #[test]
    fn test_pt1() {
        assert_eq!(
            Day2::part1(
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n\
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n\
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n\
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
            ),
            "8"
        )
    }

    #[test]
    fn test_pt2() {
        assert_eq!(
            Day2::part2(
                "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n\
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n\
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n\
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n\
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
            ),
            "2286"
        )
    }
}
