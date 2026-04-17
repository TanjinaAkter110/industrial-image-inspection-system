def center_crop(img, size=200):
    h, w = img.shape[:2]
    start_x = w // 2 - size // 2
    start_y = h // 2 - size // 2
    return img[start_y:start_y+size, start_x:start_x+size]
