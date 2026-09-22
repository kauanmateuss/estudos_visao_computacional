import pandas as pd
import matplotlib.pyplot as plt
import saeborn as sns


from sklearn.datasets import make_moons

# Criando os dados 2D sintéticos
X, y = make_moons(n_sample = 300, noise = 0.3, random_state = 42)

# Criando um DataFrame
df = pd.DataFrame(X, columns = ["Feature 1", "Feature 2"], hue = "Target", palette = "Set1")
