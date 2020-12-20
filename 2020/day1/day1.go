package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func pt1(ints []int) {

	known := make(map[int]int)
	for i, n := range ints {
		if j, ok := known[2020-n]; ok {
			fmt.Printf("%d + %d = 2020 and %d * %d = %d\n", 2020-n, n, 2020-n, n, (2020-n)*n)
			fmt.Printf("%d was at index %d, %d at index %d (both zero-based)\n", n, i, 2020-n, j)
			break
		}
		known[n] = i
	}

}

func pt2(ints []int) {

	for i, v := range ints {
		for j, w := range ints {
			if i == j {
				continue
			}
			for k, u := range ints {
				if j == k {
					continue
				}
				if v+w+u != 2020 {
					continue
				}
				fmt.Printf("%d + %d + %d = 2020 and %d * %d * %d = %d\n", v, w, u, v, w, u, v*w*u)
				return
			}
		}
	}

}

func ReadExpenseReport(fileName string) []int {

	var ints []int

	file, err := os.Open("expense_report.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// TODO: Bytes to int
		s := scanner.Text()
		i, err := strconv.Atoi(s)
		if err != nil {
			log.Printf("Can't convert %v to int", s)
		}
		ints = append(ints, i)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return ints
}

func main() {

	ints := ReadExpenseReport("expense_report.txt")

	pt1(ints)
	pt2(ints)

}
