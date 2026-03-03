import numpy as np

np.random.seed(42)

scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)
print("\n3rd student, 2nd subject:")
print(scores[2, 1])

print("\nLast 2 students:")
print(scores[-2:, :])

print("\nFirst 3 students, subjects 2 and 3:")
print(scores[:3, 1:3])


column_means = np.round(np.mean(scores, axis=0), 2)
print("\nColumn-wise mean:")
print(column_means)

curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved Scores:\n", curved_scores)

row_max = np.max(curved_scores, axis=1)
print("\nRow-wise max (best subject per student):")
print(row_max)


row_min = np.min(curved_scores, axis=1, keepdims=True)
row_max = np.max(curved_scores, axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized Scores:\n", normalized)


max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nHighest normalized score at (student, subject):")
print(max_index)

above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:")
print(above_90)