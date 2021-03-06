def merge_sort(array):

    def bottom_up(arr):
        if len(arr) < 2:
            return arr
        else:
            mid = len(arr) // 2
            left = bottom_up(arr[:mid])
            right = bottom_up(arr[mid:])

            i = 0
            j = 0
            out = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    out.append(left[i])
                    i += 1
                else:
                    out.append(right[j])
                    j += 1
            out.extend(left[i:])
            out.extend(right[j:])
        return out
    
    return bottom_up(array)


if __name__ == "__main__":
    a = [10, 7, 8, 9, 1, 5]
    print(merge_sort(a))
