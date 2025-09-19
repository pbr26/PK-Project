import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("data/exmple_pk_data.csv")
print("First 5 rows:")
print(df.head())

# plot time vs conc
plt.plot(df["time"], df["conc"], marker="o")
plt.xlabel("Time (h)")
plt.ylabel("Concentration (mg/L)")
plt.title("PK Data: Plasma concentration vs time")
plt.grid(True)
plt.show()

import numpy as np

auc = np.trapz(df["conc"], df["time"])
print("AUC (0–12 h) =", auc, "mg·h/L")
