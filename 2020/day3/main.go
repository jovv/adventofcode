package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type Position struct {
	x, y int
}

type Slope struct {
	r, d int
}

var slopes = []Slope{{r: 1, d: 1}, {r: 3, d: 1}, {r: 5, d: 1}, {r: 7, d: 1}, {r: 1, d: 2}}

func Terrain(fileName string) ([]string, int, int) {

	var t []string

	file, err := os.Open(fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		t = append(t, s)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return t, len(t[0]), len(t)
}

func main() {
	terrain, w, h := Terrain("input.txt")
	fmt.Println(terrain, w, h)

	var nrOfTrees int
	treesMultiplied := 1

	for _, slope := range slopes {

		positions := make([]Position, h)
		for i := 0; i < h/slope.d; i++ {
			positions[i] = Position{x: slope.r * i, y: slope.d * i}
		}

		for _, pos := range positions {
			if string(terrain[pos.y][pos.x%w]) == "#" {
				nrOfTrees += 1
			}
		}
		fmt.Println(nrOfTrees)
		treesMultiplied *= nrOfTrees
		nrOfTrees = 0
	}

	fmt.Println(treesMultiplied)

}
