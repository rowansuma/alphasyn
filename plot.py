import pandas as pd
import matplotlib.pyplot as plt

path = "data.csv"

df = pd.read_csv(path)

# plt.plot(df["step"], df["seed_count"], label="Seed Count")
# plt.plot(df["step"], df["monomer_count"], label="Monomer Count")
# plt.plot(df["step"], df["agg_length"], label="Aggregate Length")

plt.xlabel("Simulation Step")
plt.ylabel("Value")
plt.title("Simulation Metrics")
plt.legend()
plt.grid()

plt.show()