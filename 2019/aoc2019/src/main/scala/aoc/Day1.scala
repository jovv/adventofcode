package aoc

import scala.annotation.tailrec

object Day1 {
  def solution(s: String): List[String] =
    List(
      totalFuelRequirement(s, calculateTotalFuel),
      totalFuelRequirement(s, calculateTotalFuelPt2)
    )

  def totalFuelRequirement(s: String, f: Seq[Int] => Int): String =
    f(s.split("\n").map(_.toInt)).toString

  def calculateTotalFuel(xs: Seq[Int]): Int =
    xs.map(x => fuelRequirementForMass(x)).sum

  def calculateTotalFuelPt2(xs: Seq[Int]): Int =
    xs.map(x => fuelRequirementForMassPt2(x, 0)).sum

  def fuelRequirementForMass(x: Int): Int =
    val y = x / 3 - 2
    if (y > 0) y else 0

  @tailrec
  def fuelRequirementForMassPt2(x: Int, acc: Int): Int = {
    x.sign match
      case -1 | 0 => acc
      case _ =>
        val y = fuelRequirementForMass(x)
        fuelRequirementForMassPt2(y, acc + y)
  }
}
