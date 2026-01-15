import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.arange(1, 11)

quadrati = arr**2
cubi = arr**3

df = pd.DataFrame({
    "Numero": arr,
    "Quadrato": quadrati,
    "Cubo": cubi
})

print(df)

#grafico

plt.plot(df["Numero"], df["Quadrato"], label="Quadrato")
plt.plot(df["Numero"], df["Cubo"], label="Cubo")
plt.xlabel("Numero")
plt.ylabel("Valore")
plt.title("Grafico dei Quadrati e Cubi")
plt.legend()
plt.show()
