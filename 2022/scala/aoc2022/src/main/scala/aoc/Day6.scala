package aoc

import scala.annotation.tailrec

object Day6 extends Day {
  override def part1(s: String): String =
    marker(s, 0, 4).toString

  override def part2(s: String): String =
    marker(s, 0, 14).toString

  @tailrec
  def marker(s: String, i: Int, len: Int): Int =
    if (s.slice(i, i+len).distinct.length == len) i+len
    else marker(s, i+1, len)

}
