from visual import Point, set_lines

#   Example 1
A, B, C, D = Point(50, 50), Point(270, 50), Point(270, 172), Point(50, 172)

set_lines([(A, B), (B, C), (C, D), (D, A)], 'red')
set_lines([(A, C), (D, B)], 'red')
