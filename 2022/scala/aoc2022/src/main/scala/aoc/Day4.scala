package aoc

object Day4 extends Day {
  override def part1(s: String): String =
    s.split("\n").count(hasFullyContainedPair).toString

  override def part2(s: String): String =
    s.split("\n").count(hasOverlappingPairs).toString

  private def sections(s: String): (Int, Int, Int, Int) =
    s.split(",").flatMap(s => s.split("-").map(_.toInt)).toList match
      case List(x1, x2, y1, y2, _*) => (x1, x2, y1, y2)

  private def hasFullyContainedPair(s: String): Boolean =
    val (x1, x2, y1, y2) = sections(s)
    val xs = (x1 to x2).intersect(y1 to y2)
    xs == (x1 to x2) || xs == (y1 to y2)

  private def hasOverlappingPairs(s: String): Boolean =
    val (x1, x2, y1, y2) = sections(s)
    (x1 to x2).intersect(y1 to y2).nonEmpty

}
