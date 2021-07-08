package main

import (
    "bufio"
    "fmt"
    "os"
    "io"
    "strconv"
    "strings"
    "math"
)

func timeRequired(a []int32) {
    var output float64 = 60
    var denom float64
    for _, aa := range a {
        denom += 1.0 / float64(aa)
    }
    fmt.Println(math.Round(output / denom))
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    nTemp, _ := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
    n := int32(nTemp)
    
    var a []int32

    for i := 0; i < int(n); i++ {
        aItemTemp, _ := strconv.ParseInt(strings.TrimSpace(readLine(reader)), 10, 64)
        aItem := int32(aItemTemp)
        a = append(a, aItem)
    }

    timeRequired(a)
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}
