package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
)

var regexes = []*regexp.Regexp{
	regexp.MustCompile(``),
}

var files int64

func WalkFunc(path string, f os.FileInfo, err error) error {
	//fmt.Println("[+] FILE \t=>\t", f)
	for _, r := range regexes {

		if r.MatchString(path) {
			files += 1
			fmt.Print("[+] HIT \t=>\t", path)
			//time.Sleep(time.Millisecond * 1)
			fmt.Print("\r[+] Files Checked: ", files, "\n")
		}

	}
	return nil
}

func main() {

	root := os.Args[1]
	fmt.Println("[+] Root path supplied:", root)
	{

		if err := filepath.Walk(root, WalkFunc); err != nil {
			fmt.Println(err)

		}

	}
}
