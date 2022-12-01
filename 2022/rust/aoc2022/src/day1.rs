pub fn solution(s: String) -> (String, String) {
    (part1(s.clone()), part2(s))
}

fn part1(s: String) -> String {
    format!("{}", cargo_per_elf(s).iter().max().unwrap())
}

fn part2(s: String) -> String {
    let mut cpe = cargo_per_elf(s);
    cpe.sort();
    cpe.reverse();
    format!("{}", cpe[0..3].iter().sum::<u32>())
}

fn cargo_per_elf(s: String) -> Vec<u32> {
    s.clone()
        .split("\n\n")
        .map(|s| s.split_whitespace().map(|s| s.parse::<u32>().unwrap()))
        .map(|xs| xs.sum())
        .collect()
}
