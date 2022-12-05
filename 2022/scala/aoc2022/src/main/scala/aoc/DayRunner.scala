package aoc

import scala.util.{Failure, Success, Try}

object DayRunner {

  @main
  def run: Unit =
    val day = 5
    val fileName = s"day$day.txt"
    println(s"Running solution for day $day")
    InputReader.readFile(fileName) match
      case Success(s) => solution(day, s).foreach(println)
      case Failure(e) => println(s"Failed to get input for $fileName, msg: ${e.getMessage}")

    def solution(day: Int, s: String): List[String] =
      day match
        case 1 => Day1.solution(s)
        case 2 => Day2.solution(s)
        case 3 => Day3.solution(s)
        case 4 => Day4.solution(s)
        case 5 => Day5.solution(s)

}
