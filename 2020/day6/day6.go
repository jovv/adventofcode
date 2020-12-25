package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
)

// Unique returns unique elements of a slice of strings
func Unique(ss []string) []string {
	known := make(map[string]bool)
	var uniq []string
	for _, s := range ss {
		if known[s] {
			continue
		}
		known[s] = true
		uniq = append(uniq, s)
	}
	return uniq
}

func affirmativeForGroup(ss []string, groupLen int) int {
	known := make(map[string]int)
	for _, s := range ss {
		known[s]++
	}

	var everyone int
	for _, v := range known {
		if v != groupLen {
			continue
		}
		everyone++
	}
	return everyone
}

func main() {

	fileName := flag.String("f", "", "puzzle input file")
	flag.Parse()

	file, err := os.Open(*fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var groupAnswers []string
	var groupLen int
	var cumSumPt1, cumSumPt2 int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		if len(line) == 0 {
			if len(groupAnswers) == 0 {
				continue
			}
			cumSumPt1 += len(Unique(groupAnswers))
			cumSumPt2 += affirmativeForGroup(groupAnswers, groupLen)
			//fmt.Println("cumSum: ", cumSum)
			groupAnswers = []string{}
			groupLen = 0
			continue
		}
		//fmt.Println("line: ", line)

		groupAnswers = append(groupAnswers, strings.Split(line, "")...)
		groupLen++
		//fmt.Println("group: ", groupAnswers)

	}

	cumSumPt1 += len(Unique(groupAnswers))
	cumSumPt2 += affirmativeForGroup(groupAnswers, groupLen)
	fmt.Println("sum Pt1: ", cumSumPt1)
	fmt.Println("sum Pt2: ", cumSumPt2)

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
