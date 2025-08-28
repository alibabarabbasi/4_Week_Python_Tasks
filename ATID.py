import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("\n--- Analyzing Iris Dataset ---")
iris = sns.load_dataset("iris")
print("\nDataset Head:\n", iris.head())
print("\nSummary:\n", iris.describe())
print("\nGrouped by Species:\n", iris.groupby("species").mean())


iris.groupby("species")["petal_length"].mean().plot(kind="bar")
plt.title("Average Petal Length by Species")
plt.show()


plt.plot(iris["sepal_length"], iris["sepal_width"], "o")
plt.title("Sepal Length vs Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()


iris["petal_length"].hist()
plt.title("Petal Length Distribution")
plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.show()


plt.figure(figsize=(6, 4))
sns.heatmap(iris.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()