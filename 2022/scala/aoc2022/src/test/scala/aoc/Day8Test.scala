package aoc

import aoc.Day8.Tree
import org.scalatest.*
import org.scalatest.flatspec.*
import org.scalatest.matchers.*

class Day8Test extends AnyFlatSpec with should.Matchers {

  val grid = List(List(3, 0, 3, 7, 3), List(2, 5, 5, 1, 2), List(6, 5, 3, 3, 2), List(3, 3, 5, 4, 9), List(3, 5, 3, 9, 0))

  it should "get trees left of a specified tree" in {
    Day8.treesLeft(grid, 2, 1) shouldBe List(2, 5)
  }
  it should "get trees right of a specified tree" in {
    Day8.treesRight(grid, 2, 1) shouldBe List(1, 2)
  }
  it should "get trees up from a specified tree" in {
    Day8.treesUp(grid, 2, 1) shouldBe List(3)
  }
  it should "get trees down from a specified tree" in {
    Day8.treesDown(grid, 2, 1) shouldBe List(3, 5, 3)
  }

  it should "calculate the nr of trees on the perimeter" in {
    Day8.nrOfTreesOnPerimeter(grid) shouldBe 16
  }

  it should "verify is a tree is on the perimeter" in {
    Day8.isPerimeter(tree = Tree(0, 1, 5), gridWidth = grid.head.size, gridHeight = grid.size) shouldBe true
  }

  it should "verify if a tree is visible from a direction" in {
    Day8.isVisibleFrom(5, List(2, 5)) shouldBe false
    Day8.isVisibleFrom(5, List(1, 2)) shouldBe true
  }

  it should "calculate the nr of trees visible from outside the perimeter" in {
    Day8.visibleTrees(grid).size shouldBe 5
  }

  it should "calculate the scenic score from a direction" in {
    Day8.scenicScoreFromDirection(5, List(2, 5).reverse) shouldBe 1
    Day8.scenicScoreFromDirection(5, List(1, 2)) shouldBe 2
    Day8.scenicScoreFromDirection(3, List(3, 5).reverse) shouldBe 1
    Day8.scenicScoreFromDirection(5, List(3, 5)) shouldBe 2
  }
}
