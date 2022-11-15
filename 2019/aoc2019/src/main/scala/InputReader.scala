import scala.util.{Try, Using}

object InputReader {
  def readFile(filename: String): Try[String] =
    Using(io.Source.fromResource(filename)) { bufferedSource =>
      bufferedSource
        .getLines()
        .map(line => s"$line\n")
        .mkString
    }
}
