package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
)

// Position calculates the row or column position from a boarding pass code
func Position(row []rune, firstToken, lastToken rune, first, last int) int {
	low := first
	high := last
	for _, v := range row {
		split := (low + high) / 2
		switch v {
		case firstToken:
			high = split
		case lastToken:
			low = split + 1
		}
	}
	return low
}

func main() {

	fileName := flag.String("f", "", "puzzle input")
	flag.Parse()

	file, err := os.Open(*fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var maxSeatID int
	var seatIDs []int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		boardingPass := scanner.Text()
		row := Position([]rune(boardingPass)[:7], 'F', 'B', 0, 127)
		col := Position([]rune(boardingPass)[7:], 'L', 'R', 0, 7)
		seatID := row*8 + col

		seatIDs = append(seatIDs, seatID)

		if seatID < maxSeatID {
			continue
		}
		maxSeatID = seatID

	}
	fmt.Println(maxSeatID)

	sort.Ints(seatIDs)

	prev := seatIDs[0]
	var mySeatID int
	for _, v := range seatIDs[1:] {
		if v-1 != prev {
			mySeatID = v - 1
		}
		prev = v
	}

	fmt.Println(mySeatID)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
