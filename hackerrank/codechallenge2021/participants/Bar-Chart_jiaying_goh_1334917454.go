package main

import (
    "bufio"
    "fmt"
    "os"
    "io"
    "strconv"
    "strings"
)

func printBar(a []int64) {
    var maxCol int64
    for _, aa := range a {
        if aa > maxCol {
            maxCol = aa
        }
    }
    numRows := len(a)
    
    arrOutput := make([][]string, maxCol)
    for i := range arrOutput {
        arrOutput[i] = make([]string, numRows)
    }
    for idx, aa := range a {
        for i := int64(0); i < maxCol; i++ {
            if aa > i {
                arrOutput[maxCol - i - 1][idx] = "+"
            } else {
                arrOutput[maxCol - i - 1][idx] = " "
            }
        }
    }
    
    for _, ao := range arrOutput {
        fmt.Println(strings.Join(ao, ""))
    }
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)
    
    aTemp := strings.Split(strings.TrimSpace(readLine(reader)), " ")
    aTemp = strings.Split(aTemp[0], ",")
    var a []int64
    for _, aT := range aTemp {
        aTint, _ := strconv.ParseInt(aT, 10, 64)
        a = append(a, aTint)
    }

    for {
        line := readLine(reader)
        if line == "" {
            break
        }
        aTemp := strings.Split(strings.TrimSpace(line), " ")
        aTemp = strings.Split(aTemp[0], ",")
        for i, aT := range aTemp {
            aTint, _ := strconv.ParseInt(aT, 10, 64)
            if (aTint > a[i]) {
                a[i] = aTint
            }
        }
    }

    printBar(a)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}
