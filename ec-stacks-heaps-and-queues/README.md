Submit a python file for a solution to the below problem along with a write-up explaining 
your work and time complexities (just like normal HW!)

```
Question: 
Given a integers read from a stream, develop a function that will calculate the running median of the integers. Time complexity must O(log(n)) to find the median when a new element is inserted (in this case, n is the total amount of integers you have seen so far). 

Example: 
runningMedian(5)   = 5
runningMedian(15) = 10 (Median of [5, 15])
runningMedian(1)   = 1 (Median of [1, 5, 15])
runningMedian(3)   = 4 (Median of [1, 3, 5, 15])

Edge Cases:
Remember when calculating the median of an odd amount of integers, we simply pick the middle one. But when there’s an even amount, we average the middle two. 
```