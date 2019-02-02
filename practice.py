
Bob is preparing to pass IQ test. The most frequent task in this test is *****to find out which one of the given numbers differs from the others.**** Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)



def iq_test(numbers):
            # initialize the variable to iterate thru
            # iterate and split values into seprate indaces
    odd_keep = [int(i) % 2 for i in numbers.split()]        
    odd = 0 
    if odd_keep.count(1) > odd_keep.count(0):
        odd = 0
    else:
        odd = 1
    return odd_keep.index(odd) + 1
    # the % returns an even number the + 1 to odd_keep gives the odd value