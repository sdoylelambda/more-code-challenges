# Determine how long it would take for 7 billion people to come from 600 million with each person having 5 kids



# UPER

# Understand
# input: none/600 million
# output: number of years - centuries
# 2 people make 10 people in their lifetime - 5 each


def generation_calculator():
    people = 600000000
    parents = 600
    count_num_of_centuries = 0
    while people < 7000000000:
        people *= 5 
        count_num_of_centuries += 1

    print(count_num_of_centuries)
    return count_num_of_centuries


generation_calculator()