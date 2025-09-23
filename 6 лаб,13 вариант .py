def analyze_array(arr):
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x > 0]
    
    if negatives:
        avg_negatives = sum(negatives) / len(negatives)
    else:
        avg_negatives = None  # No negative elements
    
    if positives:
        min_positives = min(positives)
    else:
        min_positives = None  # No positive elements
    
    return avg_negatives, min_positives

# Example array of 10 elements
A = [1.5, -3.2, 0.0, 4.1, -0.5, 7.8, -2.3, 3.3, -1.1, 6.0]

avg_neg, min_pos = analyze_array(A)

print(f"Average of negative elements: {avg_neg}")
print(f"Minimum of positive elements: {min_pos}")

def max_above_diagonal(matrix):
    n = len(matrix)
    elements_above_diag = [matrix[i][j] for i in range(n) for j in range(i+1, n)]
    return max(elements_above_diag) if elements_above_diag else None

# Example 4x4 matrix
A_2d = [
    [1, 5, 3, 4],
    [6, 2, 8, 7],
    [9, 1, 0, 2],
    [4, 3, 5, 6]
]

max_above = max_above_diagonal(A_2d)
print(f"Maximum element above main diagonal: {max_above}")
