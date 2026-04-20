# ✅ AI-Based Product Recommendation & Optimization System
# (Covers Task 1, 2, 3, 4)

# -------------------------------
# 1. Import Libraries
# -------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 2. Product Dataset (Task 1)
# -------------------------------
data = {
    "Product": ["Laptop A", "Laptop B", "Laptop C", "Laptop D"],
    "Price": [50000, 70000, 90000, 120000],
    "RAM": [8, 16, 16, 32],
    "Storage": [256, 512, 1024, 1024],
    "Performance": [6, 8, 9, 10]
}

df = pd.DataFrame(data)

print("\n📊 Available Products:\n")
print(df)

# -------------------------------
# 3. User Input (Design Thinking - Empathize)
# -------------------------------
budget = int(input("\nEnter your budget (₹): "))
usage = input("Enter usage (basic/gaming/high): ").lower()

# -------------------------------
# 4. Define Problem (Task 2)
# Selecting best product under constraints
# -------------------------------

# -------------------------------
# 5. Apply C-K Theory Logic (Task 4)
# Concept = User need
# Knowledge = Dataset
# -------------------------------
if usage == "basic":
    min_perf = 5
elif usage == "gaming":
    min_perf = 8
else:
    min_perf = 9

filtered = df[(df["Price"] <= budget) & (df["Performance"] >= min_perf)]

# -------------------------------
# 6. Recommendation (Ideate + Prototype)
# -------------------------------
print("\n🔍 Filtered Products:\n")
print(filtered)

if not filtered.empty:
    best = filtered.sort_values(by="Performance", ascending=False).iloc[0]
    
    print("\n✅ Recommended Product:\n")
    print(best)
else:
    print("\n❌ No suitable product found within your budget.")

# -------------------------------
# 7. Visualization (Test Phase)
# -------------------------------
plt.figure()
plt.bar(df["Product"], df["Performance"])
plt.xlabel("Products")
plt.ylabel("Performance")
plt.title("Product Performance Comparison")
plt.show()

# -------------------------------
# 8. Final Insight (Result)
# -------------------------------
print("\n💡 Insight:")
print("This system helps users choose the best product based on budget and needs using structured problem-solving and optimization.")
