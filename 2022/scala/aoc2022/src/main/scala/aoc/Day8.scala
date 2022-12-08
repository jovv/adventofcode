package aoc

object Day8 extends Day {
  override def part1(s: String): String =
    val grid = inputToGrid(s)
    (nrOfTreesOnPerimeter(grid) + visibleTrees(grid).size).toString

  override def part2(s: String): String =
    val grid = inputToGrid(s)
    scenicScores(grid).max.toString

  type TreeGrid = List[List[Int]]
  type TreeLine = List[Int]

  case class Tree(
                   x: Int,
                   y: Int,
                   height: Int
                 )

  def nrOfTreesOnPerimeter(grid: TreeGrid): Int =
    (grid.size - 1 + grid.head.size - 1) * 2

  def inputToGrid(s: String): TreeGrid =
    s.split("\n").map(_.map(_.toString.toInt).toList).toList

  def isPerimeter(tree: Tree, gridWidth: Int, gridHeight: Int): Boolean =
    tree.x == 0 || tree.y == 0 || tree.x == (gridWidth - 1) || tree.y == (gridHeight - 1)

  def treesLeft(grid: TreeGrid, x: Int, y: Int): TreeLine =
    grid(y).take(x)

  def treesRight(grid: TreeGrid, x: Int, y: Int): TreeLine =
    grid(y).drop(x + 1)

  def treesUp(grid: TreeGrid, x: Int, y: Int): TreeLine = for
    row <- grid.take(y)
    tree = row(x)
  yield tree

  def treesDown(grid: TreeGrid, x: Int, y: Int): TreeLine = for
    row <- grid.drop(y + 1)
    tree = row(x)
  yield tree

  def isVisibleFrom(treeHeight: Int, treeLine: TreeLine): Boolean = (for
    tree <- treeLine
    v = treeHeight > tree
  yield v).forall(_ == true)

  def isVisible(tree: Tree, grid: TreeGrid): Boolean =
    isVisibleFrom(tree.height, treesLeft(grid, tree.x, tree.y)) ||
      isVisibleFrom(tree.height, treesRight(grid, tree.x, tree.y)) ||
      isVisibleFrom(tree.height, treesUp(grid, tree.x, tree.y)) ||
      isVisibleFrom(tree.height, treesDown(grid, tree.x, tree.y))

  def scenicScoreFromDirection(treeHeight: Int, treeLine: TreeLine): Int =
    (treeLine.span(treeHeight > _) match
      case (h, t) => h ::: t.take(1)).size

  def treeScenicScore(tree: Tree, grid: TreeGrid): Int =
    scenicScoreFromDirection(tree.height, treesLeft(grid, tree.x, tree.y).reverse) *
      scenicScoreFromDirection(tree.height, treesRight(grid, tree.x, tree.y)) *
      scenicScoreFromDirection(tree.height, treesUp(grid, tree.x, tree.y).reverse) *
      scenicScoreFromDirection(tree.height, treesDown(grid, tree.x, tree.y))

  def visibleTrees(grid: TreeGrid): List[Tree] = for
    row <- grid.zipWithIndex
    col <- row._1.zipWithIndex
    tree = Tree(x = col._2, y = row._2, height = col._1)
    if !isPerimeter(tree, grid.head.size, grid.size)
    if isVisible(tree, grid)
  yield tree

  def scenicScores(grid: TreeGrid): List[Int] = for
    row <- grid.zipWithIndex
    col <- row._1.zipWithIndex
    tree = Tree(x = col._2, y = row._2, height = col._1)
    if !isPerimeter(tree, grid.head.size, grid.size)
    score = treeScenicScore(tree, grid)
  yield score
}
