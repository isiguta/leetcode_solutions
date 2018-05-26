def flip_and_invert_image(a):
    return map(lambda x: [1 - n for n in x][::-1], a)
