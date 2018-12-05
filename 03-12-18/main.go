package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type claim struct {
	id, leftOffset, topOffset, width, height int
}

type status uint8

type cloth [][]status

const (
	unused status = iota
	onceUsed
	overused
)

func newClaim(id, leftOffset, topOffset, width, height int) *claim {
	return &claim{
		id:         id,
		leftOffset: leftOffset,
		topOffset:  topOffset,
		width:      width,
		height:     height,
	}
}

func getCloth() cloth {
	var outer = make(cloth, 0, 1000)
	for i := 0; i < 1000; i++ {
		outer = append(outer, make([]status, 0, 1000))
	}
	return outer
}

func countOverused(in cloth) int {
	counter := 0
	for i, row := range in {
		for j := range row {
			if in[i][j] == overused {
				counter++
			}
		}
	}
	return counter
}

func cutClaim(in cloth, c *claim) {
	for i := c.leftOffset; i < c.leftOffset+c.width; i++ {
		for j := c.topOffset; j < c.topOffset+c.height; j++ {
			switch in[i][j] {
			case unused:
				in[i][j] = onceUsed
			case onceUsed:
				in[i][j] = overused
			}
		}
	}
}

func readClaims() []*claim {
	var res = make([]*claim, 0, 2048)
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		next := parseClaim(scanner.Text())
		res = append(res, next)
	}
	return res
}

func parseClaim(line string) *claim {
	var firstSpace = strings.Index(line, " ")
	var comma = strings.Index(line, ",")
	var colon = strings.Index(line, ":")
	var ex = strings.Index(line, "x")

	var identifier, err = strconv.Atoi(line[1:firstSpace])
	if err != nil {
		log.Fatal(err)
	}

	leftOffset, err := strconv.Atoi(line[firstSpace+3 : comma])
	if err != nil {
		log.Fatal(err)
	}
	topOffSet, err := strconv.Atoi(line[comma+1 : colon])
	if err != nil {
		log.Fatal(err)
	}
	width, err := strconv.Atoi(line[colon+2 : ex])
	if err != nil {
		log.Fatal(err)
	}
	height, err := strconv.Atoi(line[ex+1:])
	if err != nil {
		log.Fatal(err)
	}
	return &claim{
		id:         identifier,
		leftOffset: leftOffset,
		topOffset:  topOffSet,
		width:      width,
		height:     height,
	}
}

func main() {
	claims := readClaims()
	for i, claim := range claims {
		var overlapped = false
		fmt.Printf("Attmpting Claim #%v\n", claim.id)
		for _, opposition := range append(claims[:i], claims[i+1:]...) {
			cloth := getCloth()
			cutClaim(cloth, claim)
			cutClaim(cloth, opposition)
			if countOverused(cloth) > 0 {
				overlapped = true
				break
			}
		}
		if !overlapped {
			fmt.Printf("%v\n", claim.id)
			os.Exit(0)
		}
	}
}
