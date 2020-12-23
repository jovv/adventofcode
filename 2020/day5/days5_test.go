package main

import (
	"testing"
)

func TestPosition(t *testing.T) {
	type testCase struct {
		description           string
		pass                  []rune
		firstToken, lastToken rune
		first, last           int
		expected              int
	}
	testCasses := []testCase{
		{
			description: "calculcate row",
			pass:        []rune("FBFBBFFRLR"),
			firstToken:  'F',
			lastToken:   'B',
			first:       0,
			last:        127,
			expected:    44,
		},
		{
			description: "calculcate column",
			pass:        []rune("FBFBBFFRLR"),
			firstToken:  'L',
			lastToken:   'R',
			first:       0,
			last:        7,
			expected:    5,
		},
	}

	for _, tc := range testCasses {
		if actual := Position(
			tc.pass,
			tc.firstToken,
			tc.lastToken,
			tc.first,
			tc.last); actual != tc.expected {

			t.Errorf(
				"Expected %d got %d for pass %s",
				tc.expected, actual, string(tc.pass))

		}
	}

}
