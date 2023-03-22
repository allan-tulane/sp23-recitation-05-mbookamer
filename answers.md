# CMPS 2200 Reciation 5
## Answers

**Name:**_Mackenzie Bookamer


Place all written answers from `recitation-06.md` here for easier grading.







- **1b.**

The asymptomtic running time for qsort_fixed_pivot is expected to be $O(logn)$.
The asymptomtic running time for qsort_random_pivot is expected to be $O(n\logn)$.
The asymptomtic running time for select_sort is expected to be $O(n^2)$.
The data below matches these predictions. 

|      n |   qsort-fixed-pivot |   qsort-random-pivot |
|--------|---------------------|----------------------|
|    100 |               0.000 |                0.005 |
|    200 |               0.000 |                0.002 |
|    500 |               0.000 |                0.001 |
|   1000 |               0.000 |                0.001 |
|   2000 |               0.000 |                0.001 |
|   5000 |               0.001 |                0.003 |
|  10000 |               0.001 |                0.003 |
|  20000 |               0.002 |                0.004 |
|  50000 |               0.003 |                0.009 |
| 100000 |               0.003 |                0.009 |

|    n |   qsort-fixed-pivot |   select-sort |
|------|---------------------|---------------|
|   10 |               0.001 |         0.009 |
|   20 |               0.000 |         0.015 |
|   50 |               0.001 |         0.068 |
|  100 |               0.001 |         0.198 |
|  250 |               0.001 |         0.861 |
|  500 |               0.000 |         3.438 |
| 1000 |               0.001 |        12.688 |
| 1500 |               0.001 |        28.995 |
| 2000 |               0.001 |        51.525 |
| 2250 |               0.001 |        62.787 |

select-sort took so long that I did decreased the size of the list in order to get the results. 




- **1c.**
|     n |   qsort-fixed-pivot |   timsort |
|-------|---------------------|-----------|
|   100 |               0.001 |     0.003 |
|   200 |               0.000 |     0.003 |
|   500 |               0.000 |     0.004 |
|  1000 |               0.000 |     0.007 |
|  5000 |               0.001 |     0.054 |
| 10000 |               0.001 |     0.076 |
| 15000 |               0.000 |     0.177 |
| 20000 |               0.000 |     0.333 |
| 25000 |               0.000 |     0.259 |
| 50000 |               0.001 |     0.525 |
