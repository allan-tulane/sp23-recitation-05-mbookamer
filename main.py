import random, time
#import tabulate


def ssort(L):
    for i in range(len(L)):
        #print(L)
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L

#we want to differentiate between a random pivot chosen or a fixed pivot chosen so we declare the functions below
def pivot_random(a):
    return random.choice(a)
def pivot_first(a):
    return a[0]
def pivot_last(a):
    return a[-1]

def qsort(a, pivot_fn):
    ## TO DO
    if len(a) <= 1:
        return L #if we have a list of 0 or 1 elements we just want to return the list since there is no sorting to do
    else:
        y = pivot_fn(a) #call the pivot function to start sorting the list 
        #now we want to split the list into parts dependent on what our x value is
        left = list(filter(lambda x: x < y, a))
        equal = list(filter(lambda x: x == y, a))
        right = list(filter(lambda x: x > y, a))
        #we want to return a list that is sorted on the left and right side of the pivot point with the pivot point being in the middle
        return qsort(left, pivot_fn) + equal + qsort(right, pivot_fn)
 
    pass
    
def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ###

def compare_sort(sizes=[100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison
    qsort_fixed_pivot = pivot_random(a) 
    qsort_random_pivot = pivot_first(a)
    tim_sort = lambda a: sorted(a)
    result = []
    for size in sizes:
        # create list in ascending order
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            time_search(tim_sort, mylist)
        ])
    return result
    ###

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-fixed-pivot', 'qsort-random-pivot'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
