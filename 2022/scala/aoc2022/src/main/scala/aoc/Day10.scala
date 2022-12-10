package aoc

import scala.annotation.tailrec

object Day10 extends Day {

  override def part1(s: String): String =
    val register = doOps(s.split("\n").toList, List(1)).reverse
    (20 to 220 by 40).map(
      i => i * register(i-1)
    ).sum.toString

  override def part2(s: String): String =
    val register = doOps(s.split("\n").toList, List(1)).reverse
    draw(register).grouped(40).map(l => s"${l.mkString}\n").mkString


  val addx_re = "addx (-?\\d+)".r

  def noOp(register: List[Int]): List[Int] =
    register.head :: register

  def doOp(op: String, register: List[Int]): List[Int] =
    val xs = noOp(register)
    op match
      case "noop" => xs
      case addx_re(s) =>
        (s.toInt + xs.head) :: xs

  @tailrec
  def doOps(ops: List[String], register: List[Int]): List[Int] =
    ops match
      case Nil => register
      case _ => doOps(ops.tail, doOp(ops.head, register))

  def drawPixel(r: Int, i: Int) =
    if ((r-1 to r+1).contains(i % 40)) "#" else "."

  def draw(register: List[Int]): List[String] = for
      (r, i) <- register.zip(0 to 239)
      pixel = drawPixel(r, i)
    yield pixel

}
