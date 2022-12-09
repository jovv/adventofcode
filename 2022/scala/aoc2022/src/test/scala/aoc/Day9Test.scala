package aoc

import aoc.Day9.{Rope, RopeEnd, directionAndDistance, moveTailDiagonally, moveTailOrthogonally, parseAndFlattenInstructions}
import org.scalatest.*
import org.scalatest.flatspec.*
import org.scalatest.matchers.*

class Day9Test extends AnyFlatSpec with should.Matchers {

  it should "flatten the rope movement instructions" in {
    val testcase = List("R 4", "U 4", "L 3", "D 1")
    val expected = List("R", "R", "R", "R", "U", "U", "U", "U", "L", "L", "L", "D")
    parseAndFlattenInstructions(testcase) shouldBe expected
  }

  it should "verify if rope ends are touching" in {
    val testcases = Seq(
      (Rope(head = RopeEnd(0, 0), RopeEnd(0, 0)), true),
      (Rope(head = RopeEnd(1, 0), RopeEnd(0, 0)), true),
      (Rope(head = RopeEnd(1, 0), RopeEnd(0, -1)), true),
      (Rope(head = RopeEnd(-1, -1), RopeEnd(-2, -1)), true),
      (Rope(head = RopeEnd(1, 1), RopeEnd(2, 2)), true),
      (Rope(head = RopeEnd(0, 0), RopeEnd(2, 2)), false),
      (Rope(head = RopeEnd(-1, -1), RopeEnd(1, 1)), false),
      (Rope(head = RopeEnd(-3, -1), RopeEnd(-1, -1)), false),
    )
    testcases.map((rope, expected) => rope.endsAreTouching shouldBe expected)
  }

  it should "verify if rope ends are orthogonally separated" in {
    val testcases = Seq(
      (Rope(head = RopeEnd(0, 0), tail = RopeEnd(2, 0)), true),
      (Rope(head = RopeEnd(0, 0), RopeEnd(0, 2)), true),
      (Rope(head = RopeEnd(-3, 1), RopeEnd(-1, 1)), true),
      (Rope(head = RopeEnd(-1, -3), RopeEnd(-1, -1)), true),
      (Rope(head = RopeEnd(1, 1), RopeEnd(3, 3)), false),
    )
    testcases.map((rope, expected) => rope.endsAreOrthogonallySeparated shouldBe expected)
  }

  it should "move the rope head up by one" in {
    val testcases = Seq(
      (RopeEnd(0, 0), RopeEnd(0, 1)),
    )
    testcases.map((ropeEnd, expected) => ropeEnd.moveUp shouldBe expected)
  }

  it should "move a rope end down by one" in {
    val testcases = Seq(
      (RopeEnd(0, 0), RopeEnd(0, -1)),
    )
    testcases.map((ropeEnd, expected) => ropeEnd.moveDown shouldBe expected)
  }

  it should "move the rope head right by one" in {
    val testcases = Seq(
      (RopeEnd(0, 0), RopeEnd(1, 0)),
    )
    testcases.map((ropeEnd, expected) => ropeEnd.moveRight shouldBe expected)
  }

  it should "move the rope head left by one" in {
    val testcases = Seq(
      (RopeEnd(0, 0), RopeEnd(-1, 0)),
    )
    testcases.map((ropeEnd, expected) => ropeEnd.moveLeft shouldBe expected)
  }

  it should "get the direction and distance from a string with an instruction" in {
    directionAndDistance("U 4") shouldBe("U", 4)
  }

  it should "move the rope tail orthogonally towards the rope head" in {
    val testcases = Seq(
      (Rope(RopeEnd(0, 0), RopeEnd(0, 2)), RopeEnd(0, 1)),
      (Rope(RopeEnd(0, 0), RopeEnd(0, -2)), RopeEnd(0, -1)),
      (Rope(RopeEnd(0, 0), RopeEnd(2, 0)), RopeEnd(1, 0)),
      (Rope(RopeEnd(0, 0), RopeEnd(-2, 0)), RopeEnd(-1, 0)),
    )
    testcases.map((rope, expected) => moveTailOrthogonally(rope) shouldBe expected)
  }

  it should "move the rope tail diagonally towards the rope head" in {
    // all possible locations of T vs H
    //   -2 -1  0  1  2
    //  2 .  T  .  T  .
    //  1 T  .  .  .  T
    //  0 .  .  H  .  .
    // -1 T  .  .  .  T
    // -2 .  T  .  T  .

    val testcases = Seq(
      // top left
      (Rope(RopeEnd(0, 0), RopeEnd(-2, 1)), RopeEnd(-1, 0)),
      (Rope(RopeEnd(0, 0), RopeEnd(-1, 2)), RopeEnd(0, 1)),
      // bottom left
      (Rope(RopeEnd(0, 0), RopeEnd(-2, -1)), RopeEnd(-1, 0)),
      (Rope(RopeEnd(0, 0), RopeEnd(-1, -2)), RopeEnd(0, -1)),
      // top right
      (Rope(RopeEnd(0, 0), RopeEnd(1, 2)), RopeEnd(0, 1)),
      (Rope(RopeEnd(0, 0), RopeEnd(2, 1)), RopeEnd(1, 0)),
      // bottom right
      (Rope(RopeEnd(0, 0), RopeEnd(2, -1)), RopeEnd(1, 0)),
      (Rope(RopeEnd(0, 0), RopeEnd(1, -2)), RopeEnd(0, -1)),
    )
    testcases.map((rope, expected) => moveTailDiagonally(rope) shouldBe expected)
  }
}
