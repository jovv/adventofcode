package aoc

object Day2 extends Day {

  override def part1(s: String): String =
    totalScore(s)(guessStrategyScore).toString


  override def part2(s: String): String =
    totalScore(s)(applyElvesStrategyScore).toString

  val shapeScores = Map(
    'X' -> 1,
    'Y' -> 2,
    'Z' -> 3,
  )

  val gameResultScores = Map(
    'X' -> 0,
    'Y' -> 3,
    'Z' -> 6,
  )

  val gameScores = Map(
    ('A', 'X') -> 3,
    ('B', 'X') -> 0,
    ('C', 'X') -> 6,
    ('A', 'Y') -> 6,
    ('B', 'Y') -> 3,
    ('C', 'Y') -> 0,
    ('A', 'Z') -> 0,
    ('B', 'Z') -> 6,
    ('C', 'Z') -> 3,
  )

  val playerShapesFromGameScores = gameScores.map{
    case ((p1, p2), v) => (p1, v) -> p2
  }

  def guessStrategyScore(s: String): Int =
    shapeScores(s(2)) + gameScores((s(0), s(2)))

  def applyElvesStrategyScore(s: String): Int =
    gameResultScores(s(2)) + shapeScores((playerShapesFromGameScores((s(0), gameResultScores(s(2))))))

  def totalScore(s: String)(f: String => Int): Int =
    s.split("\n").map(f(_)).sum

}
