package main

import (
	"testing"
)

type testCase struct {
	description string
	i, j        int
	c, pw       string
	pt1, pt2    bool
}

var testCases = []testCase{
	{
		description: "1-3 a: abcde",
		i:           1,
		j:           3,
		c:           "a",
		pw:          "abcde",
		pt1:         true,
		pt2:         true,
	},
	{
		description: "1-3 b: cdefg",
		i:           1,
		j:           3,
		c:           "b",
		pw:          "cdefg",
		pt1:         false,
		pt2:         false,
	},
	{
		description: "2-9 c: ccccccccc",
		i:           2,
		j:           9,
		c:           "c",
		pw:          "ccccccccc",
		pt1:         true,
		pt2:         false,
	},
	{
		description: "4-5 v: vpsdlnvvbvvvpfqvvvv",
		i:           4,
		j:           5,
		c:           "v",
		pw:          "vpsdlnvvbvvvpfqvvvv",
		pt1:         false,
		pt2:         false,
	},
}

func TestIsValidPasswordPt1(t *testing.T) {
	for _, tc := range testCases {
		if actual := isValidPasswordPt1(tc.i, tc.j, tc.c, tc.pw); actual != tc.pt1 {
			t.Errorf("%s pt1 %t but got %t", tc.description, tc.pt1, actual)
		}
	}
}

func TestIsValidPasswordPt2(t *testing.T) {
	for _, tc := range testCases {
		if actual := isValidPasswordPt2(tc.i, tc.j, tc.c, tc.pw); actual != tc.pt2 {
			t.Errorf("%s pt2 %t but got %t", tc.description, tc.pt2, actual)
		}
	}
}
