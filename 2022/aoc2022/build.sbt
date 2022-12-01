val scala3Version = "3.2.1"

lazy val root = project
  .in(file("."))
  .settings(
    name := "aoc2022",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies ++= Seq(
      "org.scalatest" %% "scalatest" % "3.2.14" % Test
    )
  )
