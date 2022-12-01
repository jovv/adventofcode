package aoc

import scala.annotation.tailrec

object Day1 extends Day {

  override def part1(s: String): String =
    cargoPerElf(s)(_.max).toString


  override def part2(s: String): String =
    cargoPerElf(s)(_.sorted.reverse.take(3).sum).toString

  def cargoPerElf(s: String)(f: List[Int] => Int): Int =
    f(s.split("\n\n").toList.map(ss => ss.split("\n").toList.map(s => s.toInt)).map(_.sum))
}
