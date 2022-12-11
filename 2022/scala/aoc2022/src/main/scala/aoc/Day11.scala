package aoc

import aoc.Day11InputParser.troop

import scala.annotation.tailrec
import scala.collection.SortedMap

object Day11 extends Day {

  val troopModulo = troop.map {
    case (_, m) => m.testDivBy
  }.product

  val nrOfMonkeys = troop.size

  override def part1(s: String): String =
    val nrOfRounds = 20
    monkeyRound(0, troop, nrOfRounds, 1).map {
      case (_, m) => m.activity
    }.toList.sorted.reverse.take(2).product.toString

  override def part2(s: String): String =
    val nrOfRounds = 10_000
    monkeyRound(0, troop, nrOfRounds, 2).map {
      case (_, m) => m.activity
    }.toList.sorted.reverse.take(2).product.toString

  case class Monkey(
                     items: Vector[Long],
                     activity: Long = 0,
                     opStr: String,
                     testDivBy: Long,
                     trueTarget: Int,
                     falseTarget: Int,
                   )

  type Troop = SortedMap[Int, Monkey]

  def throwTo(monkey: Monkey, level: Long): Int =
    if (level % monkey.testDivBy == 0) monkey.trueTarget else monkey.falseTarget

  val op_re = "old ([*+]) (old|\\d+)".r

  def monkeyOp(op: String, x: Long, y: Long): Long =
    op match
      case "+" => x + y
      case "*" => x * y

  def doOp(s: String, x: Long): Long =
    s match
      case op_re(op, y) =>
        monkeyOp(op, x, if (y == "old") x else y.toInt)

  def manageWorryLevel(x: Long, part: Long): Long =
    if (part == 1) x / 3 else x % troopModulo

  @tailrec
  def inspectMonkeyItem(monkeyNr: Int, monkeys: Troop, part: Int): Troop =
    monkeys(monkeyNr).items match
      case Vector() => monkeys
      case _ =>
        val monkey = monkeys(monkeyNr)
        val newLevel = manageWorryLevel(doOp(monkey.opStr, monkey.items.head), part)
        val toMonkey = throwTo(monkey, newLevel)
        val updatedTargetMonkey = monkeys(toMonkey).copy(items = monkeys(toMonkey).items :+ newLevel)
        val newCurrentMonkey = monkey.copy(items = monkey.items.tail, activity = monkey.activity + 1)
        val updatedTroop = monkeys + (toMonkey -> updatedTargetMonkey) + (monkeyNr -> newCurrentMonkey)
        inspectMonkeyItem(monkeyNr, updatedTroop, part)

  @tailrec
  def monkeyTurn(monkeyNr: Int, monkeys: Troop, part: Int): Troop =
    if (monkeyNr == nrOfMonkeys) monkeys
    else monkeyTurn(monkeyNr + 1, inspectMonkeyItem(monkeyNr, monkeys, part), part)

  @tailrec
  def monkeyRound(roundNr: Int, monkeys: Troop, nrOfRounds: Int, part: Int): Troop =
    if (roundNr == nrOfRounds) monkeys
    else monkeyRound(roundNr + 1, monkeyTurn(0, monkeys, part), nrOfRounds, part)
}
