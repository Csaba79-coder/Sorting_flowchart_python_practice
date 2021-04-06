# write your code here


def main():
    print("I am sorting_flowchart: {}".format(__name__))


    def bubble_sorting_algorithm():
        list = [1, 2, 56, 32, 51, 2, 8, 92, 15]
        x = 0
        y = 0
        for x in range(len(list)):
            for y in range(len(list)-1):
                if list[y] > list[y + 1]:
                    list[y], list[y + 1] = list[y + 1], list[y]
        print(list)
    bubble_sorting_algorithm()


    def binary_search_algorithm():

        arr = [1, 2, 4, 7, 11, 22, 38, 42, 43]
        start = 0
        end = len(arr)
        a = 42 # teszt szám! output 7. index, azaz 8. elem

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == a:
                print(mid)
                break
            else:
                if arr[mid] > a:
                    end = mid - 1
                else:
                    start = mid + 1
        else:
            print('-1')
        
    binary_search_algorithm()

    
    def prime(number):
        for divider in range(2, number):
            if number % divider == 0:
                return False
        return True


    primes = [x for x in range(2, 100 + 1) if prime(x)]
    print("Prím számok 1-100-ig:")
    print(primes)


if __name__ == "__main__":
        # execute only if run as a script
    main()