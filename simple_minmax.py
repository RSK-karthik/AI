import math

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    # Base case: targetDepth reached or leaf node reached
    if curDepth == targetDepth or nodeIndex >= len(scores):
        return scores[nodeIndex]
    
    if maxTurn:
        # If it's the max player's turn, choose the maximum value of the child nodes
        return max(minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth))
    else:
        # If it's the min player's turn, choose the minimum value of the child nodes
        return min(minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth))

# Driver code
scores =  list(map(int,input("Enter the values of an array: ").split()))
treeDepth = int(math.log(len(scores), 2)) # Calculate the depth of the complete binary tree
print("The optimal value is: ", end="")
print(minimax(0, 0, True, scores, treeDepth))
