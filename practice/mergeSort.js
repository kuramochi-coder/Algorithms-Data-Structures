arr = [5, 2, 4, 6, 1, 3]

// Merge Sort Implentation (Recursion)
function mergeSort (unsortedArray) {
    // No need to sort the array if the array only has one element or empty
    if (unsortedArray.length <= 1) {
      return unsortedArray;
    }
    // In order to divide the array in half, we need to figure out the middle
    const middle = Math.floor(unsortedArray.length / 2);
  
    // This is where we will be dividing the array into left and right
    const left = unsortedArray.slice(0, middle);
    const right = unsortedArray.slice(middle);
  
    // Using recursion to combine the left and right
    return merge(
      mergeSort(left), mergeSort(right)
    );
  }

  // Merge the two arrays: left and right
function merge (left, right) {
    let resultArray = [], leftIndex = 0, rightIndex = 0;
  
    // We will concatenate values into the resultArray in order
    while (leftIndex < left.length && rightIndex < right.length) {
      if (left[leftIndex] < right[rightIndex]) {
        resultArray.push(left[leftIndex]);
        leftIndex++; // move left array cursor
      } else {
        resultArray.push(right[rightIndex]);
        rightIndex++; // move right array cursor
      }
    }

    // Check for elements remaining from either left OR the right
    while (leftIndex < left.length) {
          resultArray.push(left[leftIndex]);
          leftIndex++; // move left array cursor
      }
    while (rightIndex < right.length) {
        resultArray.push(right[rightIndex]);
        rightIndex++; // move left array cursor
    }
  
    return resultArray
  }


result = mergeSort(arr)
console.log("mergeSort result:", result);