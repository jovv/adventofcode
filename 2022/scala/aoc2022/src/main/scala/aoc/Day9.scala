package aoc

import scala.annotation.tailrec

object Day9 extends Day {
  override def part1(s: String): String =
    moveRope(
      Rope(RopeEnd(0, 0), RopeEnd(0, 0)),
      parseAndFlattenInstructions(s.split("\n").toList),
      List[Rope]()
    ).map(_.tail).distinct.size.toString

  override def part2(s: String): String =
    moveRopeSections(
      Array.fill(9)(Rope(RopeEnd(0, 0), RopeEnd(0, 0))),
      parseAndFlattenInstructions(s.split("\n").toList),
      List[Rope]()
    ).map(_.tail).distinct.size.toString

  case class RopeEnd(
                      x: Int,
                      y: Int
                    ) {
    def moveUp = this.copy(x, y + 1)

    def moveDown = this.copy(x, y - 1)

    def moveLeft = this.copy(x - 1, y)

    def moveRight = this.copy(x + 1, y)
  }

  case class Rope(
                   head: RopeEnd,
                   tail: RopeEnd
                 ) {
    def endsAreTouching: Boolean =
      (tail.x - head.x).abs <= 1 && (tail.y - head.y).abs <= 1

    def endsAreOrthogonallySeparated: Boolean =
      (tail.x == head.x && tail.y != head.y) ||
        (tail.x != head.x && tail.y == head.y)

  }

  def directionAndDistance(s: String): (String, Int) =
    s.split(" ").toList match
      case List(dir, dist, _*) => (dir, dist.toInt)

  def parseAndFlattenInstructions(ss: List[String]): List[String] = (for
    instruction <- ss
    (direction, distance) = directionAndDistance(instruction)
    sublist = List.fill(distance)(direction)
  yield sublist).flatten


  def moveHead(ropeEnd: RopeEnd, direction: String): RopeEnd =
    direction match
      case "U" => ropeEnd.moveUp
      case "D" => ropeEnd.moveDown
      case "L" => ropeEnd.moveLeft
      case "R" => ropeEnd.moveRight

  def moveTail(rope: Rope): RopeEnd =
    if (rope.endsAreTouching) rope.tail
    else if (rope.endsAreOrthogonallySeparated) moveTailOrthogonally(rope)
    else moveTailDiagonally(rope)

  def moveTailOrthogonally(rope: Rope): RopeEnd =
    (math.signum(rope.head.x - rope.tail.x), math.signum(rope.head.y - rope.tail.y)) match
      case (1, 0) => rope.tail.moveRight
      case (-1, 0) => rope.tail.moveLeft
      case (0, 1) => rope.tail.moveUp
      case (0, -1) => rope.tail.moveDown

  def moveTailDiagonally(rope: Rope): RopeEnd =
    (math.signum(rope.head.x - rope.tail.x), math.signum(rope.head.y - rope.tail.y)) match
      case (-1, 1) => rope.tail.moveLeft.moveUp // bottom right
      case (-1, -1) => rope.tail.moveLeft.moveDown // top right
      case (1, 1) => rope.tail.moveRight.moveUp // bottom left
      case (1, -1) => rope.tail.moveRight.moveDown // top left

  def move(rope: Rope, direction: String): Rope =
    val newHead = moveHead(rope.head, direction)
    val newTail = moveTail(Rope(newHead, rope.tail))
    Rope(newHead, newTail)

  def moveSections(ropeSections: Array[Rope], direction: String): Array[Rope] =
    val newHead = moveHead(ropeSections(0).head, direction)
    val newTail = moveTail(Rope(newHead, ropeSections(0).tail))
    ropeSections(0) = Rope(newHead, newTail)
    // please close your eyes...
    for (n <- 1 to 8)
      ropeSections(n) = Rope(ropeSections(n-1).tail, moveTail(Rope(ropeSections(n-1).tail, ropeSections(n).tail)))
    ropeSections

  @tailrec
  def moveRope(rope: Rope, directions: List[String], acc: List[Rope]): List[Rope] =
    directions match
      case Nil => acc
      case _ =>
        val newRope = move(rope, directions.head)
        moveRope(newRope, directions.tail, newRope :: acc)

  @tailrec
  def moveRopeSections(ropeSections: Array[Rope], directions: List[String], acc: List[Rope]): List[Rope] =
    directions match
      case Nil => acc
      case _ =>
        val newRopeSections = moveSections(ropeSections, directions.head)
        moveRopeSections(newRopeSections, directions.tail, newRopeSections(8) :: acc)
}
