def max_profit(array):

    def go(i, curr_min, profit):
        if i == len(array):
            return profit
        else:
            curr_min = min(array[i], curr_min)
            curr_max = max(array[i] - curr_min, profit)
            return go(i + 1, curr_min, curr_max)

    return go(1, array[0], 0)

if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]
    b = [7, 6, 4, 3, 1]
    print(max_profit(a))