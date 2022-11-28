package aoc

object Day4 extends Day {
  override def part1(s: String): String =
    nrOfDifferentPasswords(s).toString

  override def part2(s: String): String =
    0.toString

  def inputToRange(s: String): Range =
    val ss = s.trim().split("-").map(_.toInt)
    ss(0) to ss(1)

  def isPassword(i: Int): Boolean =
    val s = i.toString
    val s_opt = s.lift
    s.sorted == s && s.zipWithIndex.map((c, i) => c == s_opt(i - 1).getOrElse(false) || c == s_opt(i + 1).getOrElse(false)).exists(x => x)

  def nrOfDifferentPasswords(s: String): Int =
    val r = inputToRange(s)
    r.filter(isPassword).toSet.size

}
