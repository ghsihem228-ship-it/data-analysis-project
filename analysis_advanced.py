import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Calculate averages
averages = df.mean(numeric_only=True)

print("Average Scores:")
print(averages)

# Plot average scores
plt.figure()
averages.plot(kind='bar')
plt.title("Average Scores by Subject")
plt.ylabel("Score")
plt.xlabel("Subjects")
plt.tight_layout()

plt.savefig("average_scores.png")
plt.show()
