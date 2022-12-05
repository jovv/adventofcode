package aoc

import scala.annotation.tailrec
import scala.collection.mutable.Stack

object Day5 extends Day {


  override def part1(s: String): String =
    moveCrates9000(moves(s), crates).map(_.head).mkString

  override def part2(s: String): String =
    moveCrates9001(moves(s), crates).map(_.head).mkString

  case class Move(
                   nr: Int,
                   from: Int,
                   to: Int
                 )

  val crates = List(
    List('Z', 'P', 'M', 'H', 'R'),
    List('P', 'C', 'J', 'B'),
    List('S', 'N', 'H', 'G', 'L', 'C', 'D'),
    List('F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'),
    List('F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'),
    List('T', 'F', 'S', 'Z', 'B', 'G'),
    List('N', 'R', 'V'),
    List('P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'),
    List('W', 'Q', 'N', 'J', 'F', 'M', 'L')
  ).map(_.reverse)

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
