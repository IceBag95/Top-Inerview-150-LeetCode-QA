# NOTE:
# PLEASE COPY ONLY THE BODY OF THE FUNCTION AS THE REST WAS MODIFIED TO RUN LOCALY ON VSCODE

def majorityElement(nums: list[int]) -> int:

    # making the list a set to remove duplicates and then again list to use in creating a dict
    numbers_in_nums = list(set(nums))

    # here we use the dict "fromkey" method to create a dict from the list numbers_in_nums and set init values 0
    nums_dict = dict.fromkeys(numbers_in_nums, 0)

    # we examine each number from nums. this number functions as a key to our dict
    # we assign that number to key just to look cleaner
    # we find that key in our dict and add 1 to its value
    # if a value from a key exeeds half of the lists length it's the majority key and is returned 
    for number in nums:
        key = number
        nums_dict[key] += 1

        print(nums_dict)
        if nums_dict[key] > len(nums) // 2:
            return key



nums = [1,2,1,1,1,2,2]
print(f'Majority element: {majorityElement(nums)}')  