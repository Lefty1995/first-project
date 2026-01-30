import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Dati
date = pd.date_range("2023-01-01", periods=22, freq="M")
vendite = [10, 20, 12, 15, 25, 22, 24, 28, 30, 35,
        32, 27, 29, 31, 33, 34, 36, 38, 40, 42, 44, 45]

np.random.seed(42)
eta_clienti = np.random.randint(18, 65, 50)
spesa_media = eta_clienti * 2 + np.random.randint(-20, 20, 50)

# 1) Line plot vendite mensili
plt.figure(figsize=(8, 5))
plt.plot(date, vendite, marker="o", color="blue",
        linewidth=2, linestyle="--", label="vendite")
plt.title("Andamento mensile vendite - 2023")
plt.xlabel("Mese")
plt.ylabel("Vendite (migliaia $)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()

# 2) Istogramma età clienti
plt.figure(figsize=(7, 5))
plt.hist(eta_clienti, bins=8, color="skyblue",
        edgecolor="black", alpha=0.8)
plt.title("Distribuzione età dei clienti")
plt.xlabel("Età")
plt.ylabel("Frequenza")
plt.show()

# 3) Scatter età vs spesa media
plt.figure(figsize=(7, 5))
plt.scatter(eta_clienti, spesa_media, color="red",
            marker="o", alpha=0.7)
plt.title("Relazione tra età e spesa media")
plt.xlabel("Età dei clienti")
plt.ylabel("Spesa media ($)")
plt.grid(True, alpha=0.6)
plt.show()

# 4) Griglia 2x2 di subplot
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# 4.1 Vendite mensili
ax[0, 0].plot(date, vendite, marker="o", color="blue")
ax[0, 0].set_title("Vendite mensili")
ax[0, 0].grid(True, linestyle="--", alpha=0.4)

# 4.2 Istogramma età
ax[0, 1].hist(eta_clienti, bins=8, color="skyblue",
            edgecolor="black", alpha=0.8)
ax[0, 1].set_title("Distribuzione età")

# 4.3 Scatter età vs spesa
ax[1, 0].scatter(eta_clienti, spesa_media,
                color="green", alpha=0.7)
ax[1, 0].set_title("Età vs Spesa")

# 4.4 Area + linea vendite cumulative (esempio)
vendite_cum = np.cumsum(vendite)
ax[1, 1].fill_between(date, vendite_cum,
                    color="lightblue", alpha=0.6)
ax[1, 1].plot(date, vendite_cum, color="blue")
ax[1, 1].set_title("Vendite cumulative")

plt.tight_layout()
plt.show()
