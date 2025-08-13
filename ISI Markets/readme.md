# Excercise 1:
Write a Python script that calculates a path of stones and a frog, that wants to jump from the first to the last stone and returns back. The path is provided as an integer array starting with 0, each stone element has an unique value and the array is sorted in increasing order. 

for example:
stones_path = [0,3,8,15,20]

Important conditions are: 
The frog can jump on each stone only once 
The frog starts jumping from the first stone to the last one and then comes back to the first stone again.

The length of each jump is the absolute value difference between the values of the stones which the frog jumps on. For example, if the frog is at stones_path[i] and is jumping to stones_path[j], the length of the jump is |stones[i] - stones[j]|.

The cost of a path is the maximum length of a jump among all jumps in the path.

Return the minimum possible cost of a path for the frog.

Example 1:
Input: stones_path = [0,3,9]
Output: 9
Explanation: there are 2 possible paths here: 0->3->9->0 and 0->9->3->0 
Since the frog can jump on stone with value=3 only once it will have at least one jump from 0 to 9 or from 9 to 0.   
In such case, the length of each of these jumps will be 9 so the minimum achievable cost for the path is 9.

Example 2:
Input: stones_path = [0,2,5,6,7]
Output: 5
Explanation: The above number represents one of the optimal paths the frog can take.
The cost of this path is 5, which is equal to the maximum length of one of the jumps within the frog path.
Since it's impossible to achieve a cost of less than 5, we return this result.

Example 3:
Input: stones_path = [0,3,8,15,20,22,31,44,52]
Output: 22



Constraints:
2 <= len(stones_path) <= 100
stones_path[0] == 0
stones_path is sorted in a strictly increasing order.