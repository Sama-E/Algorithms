const nums1 = [11, 3, 14, 10, 8, 6, 2, 7]; 
const nums2 = [11, 8, 14, 3, 3, 3, 6, 2, 7]; 
const nums3 = [1, 17, 12, 3, 9, 13, 21, 4, 27];  


function partition(nums=[], left=0, right=nums.length-1){
    let pivot = nums[Math.floor((left+right)/2)]
    i=left
    j = right

    while(i<=j){
        while(nums[i]<pivot){
        i++
    }

    while(nums[j]> pivot){
        j--
    }

    if(i<=j){
        [nums[i], nums[j]] = [ nums[j], nums[i]]
        i++
        j--
    }
    }
    return i
}

function quickSort(nums, left = 0, right=nums.length-1) {
    let index;
    if (nums.length > 1) {
        index = partition(nums, left, right); //index returned from partition
        if (left < index - 1) { //more elements on the left side of the pivot
            quickSort(nums, left, index - 1);
        }
        if (index < right) { //more elements on the right side of the pivot
            quickSort(nums, index, right);
        }
    }
    return nums;
}

console.log(quickSort(nums1))
console.log(quickSort(nums2))
console.log(quickSort(nums3))