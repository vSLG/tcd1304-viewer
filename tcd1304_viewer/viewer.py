import numpy as np
import matplotlib.pyplot as plt


class Viewer:

    def update_data(self, data: np.array) -> None:
        plt.clf()

        plt.xlabel("Pixel")
        plt.ylabel("Tension (V)")
        plt.legend()

        x = np.arange(1, len(data) + 1)

        plt.plot(x, data, label="Intensity")

    def show(self) -> None:
        plt.show()