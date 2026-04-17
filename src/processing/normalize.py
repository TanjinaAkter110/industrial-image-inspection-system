import numpy as np

def normalize_image(img):
    img = img.astype(float)
    return (img - img.min()) / (img.max() - img.min() + 1e-8)
