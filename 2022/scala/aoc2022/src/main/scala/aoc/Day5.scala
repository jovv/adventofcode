package aoc

import scala.annotation.tailrec
import scala.collection.mutable.Stack

object Day5 extends Day {


  override def part1(s: String): String =
    moveCrates9000(moves(s), crates(s)).map(_.head).mkString

  override def part2(s: String): String =
    moveCrates9001(moves(s), crates(s)).map(_.head).mkString

  case class Move(
                   nr: Int,
                   from: Int,
                   to: Int
                 )

  def cratesInputStrList(s: String): List[String] =
    s.split("\n\n").head.split("\n").toList

  def crates(s: String): List[List[Char]] =
    val padTo = cratesInputStrList(s).map(_.length).max
    cratesInputStrList(s)
      .map(_.padTo(padTo, ' '))
      .transpose
      .map(_.reverse)
      .filter(_.head != ' ')
      .map(_.tail)
      .map(_.filter(_ != ' '))
      .map(_.reverse)

  val moves_re = "move (\\d+) from (\\d+) to (\\d+)".r

  def moveStrToMove(s: String): Move =
    s match {
      case moves_re(nr, from, to) => Move(nr.toInt, from.toInt, to.toInt)
    }

  def strToMoveStrList(s: String) =
    s.split("\n\n").drop(1).head.split("\n")

  private def moves(s: String): List[Move] =
    strToMoveStrList(s).map(moveStrToMove).toList

  private def singleMove(from: Int, to: Int, cs: List[List[Char]]): List[List[Char]] =
    val a = cs(from - 1).head
    cs
      .updated(from - 1, cs(from - 1).tail)
      .updated(to - 1, a :: cs(to - 1))

  private def moveBulk(n: Int, from: Int, to: Int, cs: List[List[Char]]): List[List[Char]] =
    val (a, b) = (cs(from - 1).take(n), cs(from - 1).drop(n))
    cs
      .updated(from - 1, b)
      .updated(to - 1, a ::: cs(to - 1))

  @tailrec
  private def doMove(m: Move, acc: List[List[Char]]): List[List[Char]] =
    m match
      case Move(1, f, t) => singleMove(f, t, acc)
      case Move(n, f, t) => doMove(Move(n - 1, f, t), singleMove(f, t, acc))

  private def doMove9001(m: Move, acc: List[List[Char]]): List[List[Char]] =
    m match
      case Move(1, f, t) => singleMove(f, t, acc)
      case Move(n, f, t) => moveBulk(n, f, t, acc)

  @tailrec
  private def moveCrates9000(ms: List[Move], acc: List[List[Char]]): List[List[Char]] =
    ms match
      case Nil => acc
      case _ => moveCrates9000(ms.tail, doMove(ms.head, acc))

  @tailrec
  private def moveCrates9001(ms: List[Move], acc: List[List[Char]]): List[List[Char]] =
    ms match
      case Nil => acc
      case _ => moveCrates9001(ms.tail, doMove9001(ms.head, acc))
}
