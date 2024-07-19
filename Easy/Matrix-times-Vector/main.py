def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    #each sub-list represents a row
    #matrix size (m,n) * matrix size (n,p) --> matrix (m,p)
    
    #each case: does not match
    if len(a[0]) != len(b):
    	return -1
      
    #create result list
    result = []
    #for each row in a
    for i in a:
        val = 0
        #for each value index in a row
        for j in range(len(i)):
        #multiply row value with corresponding column value and add up 
            val += (i[j]*b[j])
        #append added-up value to the result list
        result.append(val)
    #append result list
    return result


# Example
matrixA = [[1,2],[2,4]]
vectorA = [1,2]
expectedA = [5, 10]
testA = matrix_dot_vector(matrixA, vectorA)

print("Example A passed?:", expectedA == testA)


testB = matrix_dot_vector([[1,2,3],[2,4,5],[6,8,9]],[1,2,3])
expectedB = [14, 25, 49]
print("Example B passed?:", expectedB == testB)
