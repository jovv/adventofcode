package aoc

import org.scalatest.*
import org.scalatest.flatspec.*
import org.scalatest.matchers.*

class Day11Test extends AnyFlatSpec with should.Matchers {

  it should "execute the op string to produce a new worry level" in {
    val testcases = Seq(
      ("old * 2", 79, 158),
      ("old + 2", 79, 81),
      ("old * old", 79, 6241),
    )
    testcases.map((s, x, expected) =>  Day11.doOp(s, x) shouldBe expected)

  }

}
