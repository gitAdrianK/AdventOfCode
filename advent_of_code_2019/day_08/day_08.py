def solve_day_08(input):
    f = open(input, "r")
    width = 25
    height = 6
    size = width*height
    pixels = f.readline().replace("\n", "")
    layers = [pixels[i:i+size] for i in range(0, len(pixels), size)]
    zeroes_in_layer = float("inf")
    zeroes_layer = None
    for layer in layers:
        zeroes = layer.count("0")
        if zeroes < zeroes_in_layer:
            zeroes_in_layer = zeroes
            zeroes_layer = layer
    p1 = zeroes_layer.count("1")*zeroes_layer.count("2")
    final_image = "2"*size
    for layer in layers:
        for index, c in enumerate(layer):
            if final_image[index] == "2":
                final_image = final_image[:index]+c+final_image[index+1:]
    # Fancy-fication
    for i in range(0, len(final_image), width):
        sub = final_image[i: i+width]
        sub = sub.replace("0", "⬛")
        sub = sub.replace("1", "⬜")
        print(sub)
    return p1


print(solve_day_08("input.txt"))
