package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
)

var fieldRe = regexp.MustCompile(`[a-z]{3}:[#a-z0-9]+`)
var hgtRe = regexp.MustCompile(`(?P<Height>[0-9]{2,3})(?P<Unit>in|cm)`)

var yearPtrn = `[0-9]{4}`
var hclPtrn = `^#[0-9a-f]{6}`
var eclPtrn = `amb|blu|brn|gry|grn|hzl|oth`
var pidPtrn = `[0-9]{9}`

func isValidPassportPt1(parts []string) bool {
	if len(parts) == 8 {
		return true
	}
	if len(parts) == 7 {
		for _, part := range parts {
			if strings.Contains(part, "cid") {
				return false
			}
		}
		return true
	}
	return false
}

func isValidField(field, pattern string) int {
	b, err := regexp.MatchString(pattern, field)
	if err != nil {
		log.Fatal(err)
	}
	if !b {
		return 0
	}
	return 1
}

func isValidYear(yr string, min, max int) int {

	b, err := regexp.MatchString(yearPtrn, yr)
	if err != nil {
		log.Fatalf("Failed regex match for pattern %s on %s, %v", yearPtrn, yr, err)
	}
	if !b {
		return 0
	}
	year, err := strconv.Atoi(yr)
	if err != nil {
		log.Fatalf("Failed to convert %s to int, %v", yr, err)
	}
	if year < min || year > max {
		return 0
	}
	return 1
}

func isValidHeight(hgt string) int {
	grps := hgtRe.FindStringSubmatch(hgt)
	if len(grps) == 0 {
		return 0
	}
	height, err := strconv.Atoi(grps[1])
	if err != nil {
		log.Fatal(err)
	}
	if grps[2] == "cm" && (height < 150 || height > 193) {
		return 0
	}
	if grps[2] == "in" && (height < 59 || height > 76) {
		return 0
	}
	return 1
}

// TODO: 138 too high, fix this
func isValidPassportPt2(parts []string) bool {
	if len(parts) <= 6 || len(parts) > 8 {
		return false
	}
	var validFields int
	for _, part := range parts {
		field := strings.Split(part, ":")
		switch field[0] {
		case "byr":
			i := isValidYear(field[1], 1920, 2002)
			if i == 0 {
				return false
			}
			validFields++
		case "iyr":
			i := isValidYear(field[1], 2010, 2020)
			if i == 0 {
				return false
			}
			validFields++
		case "eyr":
			i := isValidYear(field[1], 2020, 2030)
			if i == 0 {
				return false
			}
			validFields++
		case "hgt":
			i := isValidHeight(field[1])
			if i == 0 {
				return false
			}
			validFields++
		case "hcl":
			i := isValidField(field[1], hclPtrn)
			if i == 0 {
				return false
			}
			validFields++
		case "ecl":
			i := isValidField(field[1], eclPtrn)
			if i == 0 {
				return false
			}
			validFields++
		case "pid":
			i := isValidField(field[1], pidPtrn)
			if i == 0 {
				return false
			}
			validFields++
		case "cid":
			validFields++
		default:
			fmt.Println("default", parts)
			return false
		}
	}
	if validFields == 7 && strings.Contains(strings.Join(parts, ";"), "cid:") {
		return false
	}
	fmt.Println(parts, validFields, true)
	return true
}

func main() {

	fileName := flag.String("f", "", "puzzle input file")
	flag.Parse()

	file, err := os.Open(*fileName)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var passportParts []string
	var validPassports int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		s := scanner.Text()
		line := fieldRe.FindAllString(s, -1)
		passportParts = append(passportParts, line...)
		if len(line) == 0 {
			if isValidPassportPt2(passportParts) {
				validPassports++
			}
			passportParts = []string{}
		}
	}

	fmt.Println(validPassports)
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

}
