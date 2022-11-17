package aoc

import scala.annotation.tailrec

object Day2 {

  def solution(s: String): List[String] =
    List(
      part1(s).toString,
      part2(s).toString
    )

  def part1(s: String): Int =
    intCode(setInitialState(inputToInts(s), 12, 2), 0)

  def part2(s: String): Int =
    generateOutputs(inputToInts(s)).filter(_ != 0).head

  def inputToInts(s: String): Vector[Int] =
    s.trim.split(",").map(_.toInt).toVector

  def setInitialState(xs: Vector[Int], noun: Int, verb: Int): Vector[Int] =
    xs.updated(1, noun).updated(2, verb)

  def generateOutputs(xs: Vector[Int]): IndexedSeq[Int] = for
    noun <- 1 to 99
    verb <- 1 to 99
  yield
    intCode(setInitialState(xs, noun, verb), 0) match
      case 19690720 => 100 * noun + verb
      case _ => 0

  @tailrec
  def intCode(xs: Vector[Int], pos: Int): Int =
    xs(pos) match
      case 99 => xs(0)
      case _ =>
        xs.slice(pos, pos + 4) match
          case Vector(op, xPos, yPos, outputPos) =>
            val outputVal = op match
              case 1 => xs(xPos) + xs(yPos)
              case 2 => xs(xPos) * xs(yPos)
            intCode(xs.updated(outputPos, outputVal), pos + 4)

}
