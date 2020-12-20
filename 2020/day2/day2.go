package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type PasswordRecord struct {
	Min      int
	Max      int
	Token    string
	Password string
}

var linePattern = regexp.MustCompile(`(?P<Min>\d{1,})-(?P<Max>\d{1,}) (?P<Char>[a-z]{1}): (?P<Password>[a-z]+)`)

func isValidPasswordPt1(min, max int, c, pw string) bool {
	cnt := strings.Count(pw, c)
	if min <= cnt && cnt <= max {
		return true
	}
	return false
}

func isValidPasswordPt2(pos1, pos2 int, c, pw string) bool {
	if (string(pw[pos1-1]) == c || string(pw[pos2-1]) == c) && !(string(pw[pos1-1]) == c && string(pw[pos2-1]) == c) {
		return true
	}
	return false
}

func main() {

	var validCnt int

	file, err := os.Open("passwords.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		fmt.Println(s)
		grps := linePattern.FindStringSubmatch(s)
		fmt.Println(grps)
		i, _ := strconv.Atoi(grps[1])
		j, _ := strconv.Atoi(grps[2])
		if isValidPasswordPt2(i, j, grps[3], grps[4]) {
			validCnt += 1
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(validCnt)
}
