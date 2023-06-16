/**
 * @param {number[]} nums
 * @return {number[]}
 * O(n)
 */

const nums = [1,2,3,4];
const nums1 = [10,20,30,40];

function runningSum(nums) {
    //Make newArray same size as nums array
    let newArray = new Array(nums.length);
    newArray[0] = nums[0]
    //For loop though index [i] nums
    for (let i = 1; i < nums.length; i++)
        //For nums[i] add nums[i-1]
        newArray[i] = newArray[i-1] + nums[i];
    //Return newArray
    return newArray;
    
};


console.log(runningSum(nums));
console.log(runningSum(nums1));