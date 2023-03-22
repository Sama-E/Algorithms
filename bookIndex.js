/* 
Book Index
Given an array of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums
span a consecutive range.
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @returns {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */

function bookIndex(num) {
	var temp = [];
	for (var i = 0; i < num.length; i++) {
		if (num[i]+1 == num[i+1]) {
			var start = num[i];
			while (num[i]+1 == num[i+1]) {
				i++;
			}
		var end = num[i];
		temp.push(start + "-" + end);
		} else {
			temp.push(num[i]);
		}
	}
	var newstring = temp.join(',');
	return newstring
}

console.log(bookIndex(nums1));
console.log(bookIndex(nums2));
console.log(bookIndex(nums3));