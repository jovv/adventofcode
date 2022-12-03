package aoc

object Day3 extends Day {

  override def part1(s: String): String =
    sumOfPriorities(s).toString

  override def part2(s: String): String =
    sumOfGroupedPriorities(s).toString

  val lc_priorities = ('a' to 'z').zip(1 to 26).toMap
  val uc_priorities = ('A' to 'Z').zip(27 to 52).toMap

  def priority(c: Char): Int =
    if (c.isUpper) uc_priorities(c)
    else lc_priorities(c)

  def ruckSackPriority(s: String): Int =
    val (a, b) = s.splitAt(s.length / 2)
    priority(a.intersect(b).head)

  def sumOfPriorities(s: String): Int =
    s.split("\n").map(ruckSackPriority).sum

  def sumOfGroupedPriorities(s: String): Int =
    s.split("\n").grouped(3).map(g => g.reduce((a, b) => a.intersect(b))).map(x => priority(x.head)).sum
}
