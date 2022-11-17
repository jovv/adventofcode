package aoc

import org.scalatest.*
import org.scalatest.flatspec.*
import org.scalatest.matchers.*

class Day1Test extends AnyFlatSpec with should.Matchers {
  val testcases: Seq[(Int, Int)] = Seq(
    (14, 2),
    (1969, 966),
    (100756, 50346)
  )
  it should "calculate fuel requirements recursively" in {
    testcases.map ((mass, expected) => Day1.fuelRequirementForMassPt2(mass, 0) shouldBe expected
    )
  }

}
