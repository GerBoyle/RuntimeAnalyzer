import time
from random import randint
from demos import quicksort, mergesort, bubblesort


def rand_num_gen(size, max_val):
    list1 = [randint(1,int(max_val)) for num in range(int(size))]
    return list1
    


def analyze_funct(func, arr):
    tic = time.time()
    func(rand_list)
    tock = time.time()
    seconds = tock - tic
    print(f"{func.__name__.capitalize()}\t-> Elapsed time: {seconds:.5f}")

size = int(input('What size list do you want to create? '))
max = int(input('What is the max value of the range? '))
run_times = int(input('How many times do you want to run? '))

rand_list = rand_num_gen(size, max)

for num in range(run_times):
    print(f"Run: {num + 1}")
    analyze_funct(bubblesort, rand_list.copy())
    analyze_funct(quicksort, rand_list)
    analyze_funct(mergesort, rand_list)
    print("-" * 40)
