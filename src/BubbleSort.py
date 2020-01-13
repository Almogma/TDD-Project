class BubbleSort:

    @staticmethod
    def bubbleSort(arr):
     try:
                arr = list(arr)
                n = len(arr)

            # Traverse through all array elements
                for i in range(n):

                    # Last i elements are already in place
                    for j in range(0, n - i - 1):

                        # traverse the array from 0 to n-i-1
                        # Swap if the element found is greater
                        # than the next element
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]

                return arr
     except TypeError:
        return "Invalid_Values"

    def Refactoring_BubbleSort(arr):

        return map(lambda a,b: (a,b) for (b,a) ,filter(lambda j: arr[j] > arr[j+1],arr)

    print(Refactoring_BubbleSort([1,2]))