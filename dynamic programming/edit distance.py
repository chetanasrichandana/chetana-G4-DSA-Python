def edit_distance(word1, word2): 
    distance = helper(word1, word2, 0, 0) 
    return distance 
 
def helper(word1, word2, i, j): 
    if i == len(word1): 
        return len(word2) - j 
    if j == len(word2): 
        return len(word1) - i 
     
    if word1[i] == word2[j]: 
        return helper(word1, word2, i + 1, j + 1) 
     
    insert_operation = helper(word1, word2, i, j + 1)   
    remove_operation = helper(word1, word2, i + 1, j)    
    replace_operation = helper(word1, word2, i + 1, j + 1)     
    return 1 + min(insert_operation, remove_operation, replace_operation) 
 
str1 = "kitten" 
str2 = "sitting" 
print(edit_distance(str1, str2))  
