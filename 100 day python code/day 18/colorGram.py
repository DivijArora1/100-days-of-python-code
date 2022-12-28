import colorgram

rgb_colors = []
# Extract 6 colors from an image in the form of tupple in a list.
colors = colorgram.extract('day 18\imag.jpg', 110)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
# result 
color_list = [(250, 246, 241), (250, 244, 247), (242, 249, 246), (242, 245, 249), (207, 155, 102), (57, 107, 128), (162, 82, 43), 
(125, 79, 97), (122, 156, 171), (126, 175, 159), (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19), (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32), (41, 31, 33), (8, 30, 28), (81, 146, 165), (238, 167, 162), (156, 28, 21), (23, 80, 91), (233, 168, 173), (173, 206, 188), (106, 126, 157), (26, 87, 84), (164, 202, 208), (89, 69, 31), 
(52, 62, 82), (185, 189, 205)]