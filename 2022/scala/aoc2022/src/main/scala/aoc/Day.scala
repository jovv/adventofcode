package aoc

trait Day {
  def solution(s: String): List[String] =
    List(
      part1(s),
      part2(s)
    )

  def part1(s: String): String = ???
  def part2(s: String): String = ???
}
