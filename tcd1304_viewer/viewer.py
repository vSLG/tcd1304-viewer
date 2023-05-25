import numpy as np
import matplotlib.pyplot as plt


class Viewer:

    def update_data(self, data: np.array) -> None:
        plt.clf()

        plt.xlabel("Pixel")
        plt.ylabel("Tension (V)")
        # plt.legend()
        plt.ylim(0, 3.4)

        x = np.arange(1, len(data) + 1)

        plt.plot(x, data, label="Intensity")
        # plt.draw()

        self.show()
        self.pause()

    def show(self) -> None:
        plt.ion()
        plt.show(block=False)

    def pause(self, secs: float = 0.001) -> None:
        plt.pause(secs)