def two_sum(data, target):
    """
    we define a value map for the indices 
    we then create a container for the list as results
    
    """
    index_map = {}
    list_of_results = []

    for i, values in enumerate(data):
        # define a compliment
        compliment = target - values

        # if compliment we store it results
        if compliment in index_map:
            list_of_results.append([index_map[compliment], i])
        
        index_map[values] = i 

    return list_of_results


dtr = [2 , 7, 1, 8]
tgr = 9 
output = two_sum(dtr, tgr)
print(output)
