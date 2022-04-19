def print_daily_totals(rainfalls):
    """returns the total rainfall in each day"""
    for (day, days_rain) in enumerate(rainfalls):
        sum1 = 0
        print("Day {} total:".format(day), end="")
        for s in days_rain:
            sum1 += s
        print(" {}".format(sum1), end="")     
        print()

rainfalls = [ 
      [0, 9, 3, 7],
      [11, 9, 0, 0],
      [0, 10, 12, 20],
      [0, 0, 0, 0],
      [1, 3, 4, 1],
      [2, 8, 10, 0],
      [0, 0, 0, 0]
]
print_daily_totals(rainfalls)
print("-------------------------")
rainfalls = [ 
      [1, 7, 9],
      [],
      [9, 1, 2],
      [10, 5],
      [20]
]
print_daily_totals(rainfalls)