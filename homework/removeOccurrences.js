// const removeOccurrences = (inputArr, valueToRemove) => {
//     arr = inputArr
//     // console.log(count)
//     for (var value = 0; value < arr.length; value++) {
//         console.log(value)
//         if (arr[value] === valueToRemove) {
//             console.log('value', value)
//             arr.slice(value, 1)
//             console.log(arr)
//         // } else {
//         //     count += 1
//         }
//     }
//     console.log(arr)
//     return arr
// }



// UPER Framework

// Understand 
// Input: array of numbers, specific values to remove
// Output: inputed array with specific values removed

// Plan
// Option 1
// for loop on input arr
// if value = value to remove
// remove it
// return modified/new arr

// Option 2
// filter out values to remove
// return modified arr

// Execute
const removeOccurrences = (arr, valueToRemove) => {
    return arr.filter(value => value !== valueToRemove);  
}

// Revise
// Update arr paramater to be more descriptive

console.log(removeOccurrences([1, 2, 3, 2, 4,], 2))