def solve_day_08(input):
    f = open(input, "r")
    width = 25
    height = 6
    pixels = f.readline().replace("\n", "")
    layers = [pixels[i:i+width*height] for i in range(0, len(pixels), width*height)]
    zeroes_in_layer = float("inf")
    zeroes_layer = None
    for layer in layers:
        zeroes = layer.count("0")
        if zeroes < zeroes_in_layer:
            zeroes_in_layer = zeroes
            zeroes_layer = layer
    p1 = zeroes_layer.count("1")*zeroes_layer.count("2")
    return p1


print(solve_day_08("input.txt"))
