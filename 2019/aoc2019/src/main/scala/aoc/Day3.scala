package aoc

import scala.annotation.tailrec

object Day3 extends Day {

  override def part1(s: String): String =
    distanceToClosestIntersection(s).toString

  override def part2(s: String): String =
    minSignalDelay(s).toString

  case class Point(
                    x: Int,
                    y: Int
                  )

  case class SignalDelay(
                          value: Int
                        )

  case class Position(
                       point: Point,
                       signalDelay: SignalDelay
                     )

  def directionsFromInput(s: String): Seq[String] =
    s.split(",")

  def lineFromDirections(s: String, pos: Position): Seq[Position] =
    val direction = s.head
    val distance = s.tail.mkString.toInt
    for
      i <- 1 to distance
      line = direction match
        case 'R' => Position(Point(pos.point.x + i, pos.point.y), SignalDelay(pos.signalDelay.value + i))
        case 'U' => Position(Point(pos.point.x, pos.point.y + i), SignalDelay(pos.signalDelay.value + i))
        case 'D' => Position(Point(pos.point.x, pos.point.y - i), SignalDelay(pos.signalDelay.value + i))
        case 'L' => Position(Point(pos.point.x - i, pos.point.y), SignalDelay(pos.signalDelay.value + i))
    yield line

  @tailrec
  def wirePositions(ss: Seq[String], p: Position, acc: Seq[Seq[Position]]): Seq[Seq[Position]] =
    ss match
      case Nil => acc
      case _ =>
        val line = lineFromDirections(ss.head, p)
        wirePositions(ss.tail, line.last, acc :+ line)

  def positionsPerWire(s: String): Seq[Seq[Position]] =
    for
      wireInput <- s.split("\n")
      wire = directionsFromInput(wireInput)
      points = wirePositions(wire, Position(Point(0, 0), SignalDelay(0)), Seq()).flatten
    yield points

  def distanceToClosestIntersection(s: String): Int =
    val wires = positionsPerWire(s)
    val wire1 = wires(0)
    val wire2 = wires(1)
    wire1.map(_.point).intersect(wire2.map(_.point)).map(p => p.x.abs + p.y.abs).min

  def minSignalDelay(s: String): Int =
    def positionToMap(xs: Seq[Position]): Map[Point, SignalDelay] =
      xs.foldLeft(Map[Point, SignalDelay]()) { (m, pos) => m + (pos.point -> pos.signalDelay)}

    val wires = positionsPerWire(s)
    val wire1 = wires(0)
    val wire2 = wires(1)
    val intersections = wire1.map(_.point).intersect(wire2.map(_.point))
    intersections.map(p => positionToMap(wire1)(p).value + positionToMap(wire2)(p).value).min


}
