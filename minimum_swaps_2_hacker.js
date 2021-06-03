
function minimumSwaps(arr) {
    let swap_count = 0;
    
    for (let i=0; i < arr.length; i++) {
        let correctValue = i + 1;
        if (arr[i] != correctValue) {
            let originalValue = arr[i];
            for (let j=i+1; j < arr.length; j++) {
                if (arr[j] == correctValue) {
                    arr[i] = correctValue;
                    arr[j] = originalValue;
                    swap_count++;
                    break;
                }
            }
        }
    }
    
    return swap_count

}

console.log(minimumSwaps([4, 3, 1, 2]))
// 3

console.log(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
// 3