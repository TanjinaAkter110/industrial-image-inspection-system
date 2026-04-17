import matplotlib.pyplot as plt

def plot_histogram(img):
    plt.hist(img.ravel(), bins=50)
    plt.title("Histogram")
    plt.show()
