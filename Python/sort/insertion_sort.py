# Note: this is not a complete program.
#
# The insertion_sort function performs an insertion sort
# algorithm on a list of integers.

def insertion_sort(arr):
  # Set index to 1 for the outer loop.
  index = 1

  # The outer loop steps the index variable through
  # each subscript in the list, starting at 1. This
  # is because element 0 is considered already sorted.
  while index < len(arr):
    # The first element outside the sorted subset is
    # arr[index]. Assign the value of this element
    # to unsorted_value.
    unsorted_value = arr[index]

    # Start the scan variable at the subscript of the
    # first element outside the sorted subset.
    scan = index

    # Move the first element outside the sorted subset
    # into its proper position within the sorted subset.
    while scan > 0 and arr[scan - 1] > unsorted_value:
      arr[scan] = arr[scan - 1]
      scan = scan - 1

    # Insert the unsorted value in its proper position
    # within the sorted subset.
    arr[scan] = unsorted_value

    # Increment index.
    index = index + 1