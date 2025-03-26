# Note: This is not a complete program.
#
# The selection_sort function performs the selection sort
# algorithm on a list of integers.

def selection_sort(arr):
  # Set start_scan to 0. This is necessary for
  # the outer loop. It is the starting position
  # of the scan.
  start_scan = 0

  # The outer loop iterates once for each element in the
  # list. The start_scan variable marks the position where
  # the scan should begin.
  while start_scan < len(arr) - 1:
    # Assume the first element in the scannable area
    # is the smallest value.
    min_index = start_scan
    min_value = arr[start_scan]

    # Initialize index for the inner loop.
    index = start_scan + 1

    # Scan the list, starting at the 2nd element in
    # the scannable area. We are looking for the smallest
    # value in the scannable area.
    while index < len(arr):
      if arr[index] < min_value:
        min_value = arr[index]
        min_index = index
      # Increment index.
      index = index + 1

    # Swap the element with the smallest value
    # with the first element in the scannable area.
    arr[min_index] = arr[start_scan]
    arr[start_scan] = min_value

    # Increment start_scan.
    start_scan = start_scan + 1