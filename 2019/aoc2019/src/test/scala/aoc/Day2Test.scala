package aoc

import org.scalatest.*
import org.scalatest.flatspec.*
import org.scalatest.matchers.*

class Day2Test extends AnyFlatSpec with should.Matchers {
  private val testcases = List(
    (Vector(1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50), 2, 12, 3500),
  )
  it should "have the correct output when the program halts" in {
    testcases.map(
      (vec, noun, verb, expected) => Day2.intCode(Day2.setInitialState(vec, noun, verb), 0) shouldBe expected
    )
  }

}
