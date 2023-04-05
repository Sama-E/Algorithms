/* 
    https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/visualize/
    Stable sort

    Time Complexity
    - Best: O(n) linear when array is already sorted.
    - Average: O(n^2) quadratic.
    - Worst: O(n^2) quadratic when the array is reverse sorted.
    Space: O(1) constant.
    For review, create a function that uses BubbleSort to sort an unsorted array in-place.
    For every pair of adjacent indices, swap them if the item on the left is larger than the item on the right until array is fully sorted
*/

const numsOrdered = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const numsRandomOrder = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const numsReversed = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
const numsRandomOrder2 = [91, 22, 35, 46, 54, 63, 77, 10, 81, 98];

const expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];


function bubbleSort(nums) { 
    //For Loop: Iterate through array 1st time
    for (let x = 0; x < nums.length; x++) {
        //For Loop: During first iteration, iterate through array 2nd time
        for (let y = 0; y < nums.length; y++) {
            //If 2nd iteration the index is greater than index + 1
            if (nums[y] > nums[y + 1]) {
                //Store the index in temp
                let temp = nums[y];
                //Make the index equal to index + 1 
                nums[y] = nums[y + 1];
                //Make index + 1 equal temp
                nums[y + 1] = temp;
            }
        }
    }
    console.log(nums);
    return nums;
}

bubbleSort(numsOrdered);
bubbleSort(numsRandomOrder);
bubbleSort(numsReversed);
bubbleSort(numsRandomOrder2);    