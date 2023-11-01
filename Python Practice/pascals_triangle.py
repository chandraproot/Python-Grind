

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]  # Special case: the first row

        # Initialize the first row
        current_row = [1]

        # Loop to generate subsequent rows
        for i in range(1, rowIndex + 1):
            next_row = [1]  # First element of each row is 1

            # Calculate the elements in between
            for j in range(1, i):
                next_row.append(current_row[j - 1] + current_row[j])

            next_row.append(1)  # Last element of each row is 1
            current_row = next_row

        return current_row
  
        