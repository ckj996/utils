#!/usr/bin/env python3

# generate xdosc_logo.svg
# Copyright © 2017 CKJ <ckj996@gmail.com>
# MIT License
#
# Usage: ./logo-maker > xdosc_logo.svg
#

from math import sqrt

#
# custom parameters
#
canvas = 512    # canvas size
radius = 240    # radius of main circle
s_radius_ratio = .850   # ratio to radius
s_corner_ratio = .224   # ratio to radius
s_width_ratio = .092    # ratio to radius
s_color = "#212121"
bg_color = "#FAFAFA"
petal_colors = (
    "#F44336",  # 1 o'clock
    "#FF9800",  # 3 o'clock
    "#4CAF50",  # 7 o'clock
    "#FFEB3B",  # 5 o'clock
    "#2196F3",  # 9 o'clock
    "#9C27B0",  # 11 o'clock
)

#
# parameters - DO NOT change
#

s_radius = radius * s_radius_ratio
s_corner = radius * s_corner_ratio
s_width = radius * s_width_ratio

p_width_ratio = (1 - s_radius_ratio) * sqrt(3) / 2 - s_width_ratio / 2
p_radius_ratio = 1 - p_width_ratio / sqrt(3)
p_width = radius * p_width_ratio
p_radius = radius * p_radius_ratio

base = (canvas / 2, canvas / 2)
base_vectors = (
    (0, -2),
    (sqrt(3), -1),
    (sqrt(3), 1),
    (0, 2),
    (-sqrt(3), 1),
    (-sqrt(3), -1),
)
s_rules = (
    (1, (s_width * 0.75, s_width * 0.75 / sqrt(3))),
    (0, (0, 0)),
    (5, (0, 0)),
    (5, (0, s_corner)),
    (2, (0, -s_corner)),
    (2, (0, 0)),
    (3, (0, 0)),
    (4, (-s_width * 0.75, -s_width * 0.75 / sqrt(3))),
)

#
# vector functions
#
def scale(vector, factor):
    (x, y) = vector
    return (x * factor, y * factor)

def add(vector1, vector2):
    (x1, y1) = vector1
    (x2, y2) = vector2
    return (x1 + x2, y1 + y2)

def make_points(base, vector_set, factor):
    return [add(base, scale(vector, factor)) for vector in vector_set]

def make_points_by_rules(points, rules):
    return [add(points[i], vector) for (i, vector) in rules]

def make_points_attr(points):
    str = 'points="'
    (first_point, other_points) = (points[0], points[1:])
    str += "%f %f" % first_point
    for point in other_points:
        str += ", %f %f" % point
    str += '"'
    return str

def qrint(str):
    print(str, end = ' ')

def print_xml_header():
    print('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')

def print_svg_header(width, height):
    qrint('<svg version="1.1" baseProfile="full"')
    qrint('width="%d" height="%d"' % (width, height))
    print('xmlns="http://www.w3.org/2000/svg">')

def print_svg_footer():
    print('</svg>')

def print_polygon(points, fill, stroke, width):
    qrint("<polygon")
    qrint('fill="%s"' % fill)
    qrint('stroke="%s"' % stroke)
    qrint('stroke-width="%f"' % width)
    qrint('stroke-linecap="butt"')
    qrint('stroke-linejoin="miter"')
    qrint(make_points_attr(points))
    print("/>")

def print_polyline(points, fill, stroke, width):
    qrint("<polyline")
    qrint('fill="%s"' % fill)
    qrint('stroke="%s"' % stroke)
    qrint('stroke-width="%f"' % width)
    qrint('stroke-linecap="butt"')
    qrint('stroke-linejoin="miter"')
    qrint(make_points_attr(points))
    print("/>")

def print_petals(points):
    for i in range(0, 6):
        p, q, fill = points[i], points[(i + 1) % 6], petal_colors[i]
        qrint("<path")
        qrint('fill="%s"' % fill)
        qrint('d="M %f %f L %f %f A %f %f 0 0 0 %f %f"' % (p + q + (radius, radius) + p))
        print("/>")

outer_points = make_points(base, base_vectors, radius / 2)
padding_points = make_points(base, base_vectors, p_radius / 2)
inner_points = make_points(base, base_vectors, s_radius / 2)
s_points = make_points_by_rules(inner_points, s_rules)

print_xml_header()
print_svg_header(canvas, canvas)
print_polygon(outer_points, bg_color, "none", 0)
print_polyline(s_points, "none", s_color, s_width)
print_polygon(padding_points, "none", bg_color, p_width)
print_petals(outer_points)
print_svg_footer()
