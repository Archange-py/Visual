![Visual Banner](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/resources/logo/logo_visual_flag.png)

# Visual

[![GitHub Stars](https://img.shields.io/github/stars/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/network)
[![GitHub Issues](https://img.shields.io/github/issues/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/pulls)
[![GitHub License](https://img.shields.io/github/license/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/commits/main)
![Tests](https://github.com/Archange-py/Visual/actions/workflows/python-tests.yml/badge.svg)
![Visiteurs](https://visitor-badge.laobi.icu/badge?page_id=Archange-py.Visual)

[![PyPI Version](https://img.shields.io/pypi/v/visualcore.svg)](https://pypi.org/project/visualcore/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/visualcore.svg)](https://pypi.org/project/visualcore/)
[![Python Versions](https://img.shields.io/pypi/pyversions/visualcore.svg)](https://pypi.org/project/visualcore/)


###
Welcome! This project is designed for use with the Numworks graphing calculator. It allows you to add graphical functions, mainly around new drawing functions like line or circle drawing, but also mathematical classes like vectors or points, and much more!

But it's also an easy-to-use library available on PyPi, so you don't have to code on your calculator, thanks to the Numworks python emulator for computers.

[![Star History Chart](https://api.star-history.com/svg?repos=Archange-py/Visual&type=Date)](https://star-history.com/#Archange-py/Visual&Date)

## Table of Contents
***
1. [General Info](#general-info)
2. [How to use it](#how-to-use-it)
3. [Examples](#examples)
3. [Tree Fractals](#tree-fractals)
5. [Extensions](#extensions)
6. [QR-Codes](#qr-codes)
7. [FAQs](#faqs)

## General Info
***
I recommend that you test the example files on your own computer, as you can drastically increase their execution speeds. 

To install it on the Numworks, we have the choice :  
1. Just follow this link to the [Numworks website](https://my.numworks.com/python/archange/visual)  

2. You just need to copy and paste the code from the *[visual](./src/visual/visual.py)* file into a new script on your Numworks account. Then upload it to your calculator. 

> Here's another example of what you can do with the functions provided by Visual.  

![example.gif](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/examples.gif)

If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install the visualcore library on your computer !  

## How to use it
***

1. Simply use this command :
```bash
pip install visualcore
```

2. Or download the [github repository](https://github.com/Archange-py/Visual/archive/refs/heads/main.zip) in .zip or clone it via this url :
```bash
https://github.com/Archange-py/Visual.git
```

To use it properly, you need to install several python packages on your computer, either from the command line using the [requirements.txt](requirements.txt) file :
```bash
pip install -r requirements.txt
```

Or individually with each package.

* [Kandinsky](https://github.com/ZetaMap/Kandinsky-Numworks) :  
```bash
pip install kandinsky
```

* [Ion](https://github.com/ZetaMap/Ion-numworks) :  
```bash
pip install --pre ion-numworks
```

And python, of course, [here](https://www.python.org/downloads/) if you don't already have it.

> You can change the emulator's OS by pressing "_CTR+O_" to increase speed, so you can get the most out of it without seeing everything slow down !

## Examples
***
First of all, after you're on your computer, you need to start by importing it after installing it in the current directory, and write that on the first line of your project :

```Python
from visual import *
``` 
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal one *Jupiter Notebook* containing everything that can be shown in writing for the file [visual_example](src/visual/examples/functions/notebooks/visual_example.ipynb).

> Here's an example of what you can do with the calculator, using the compact [example file](./src/visual/examples/introduction/example.py). Click [here](https://my.numworks.com/python/archange/example_visual) to see it on the Numworks website.  

```Python
from visual import *

A = Point( 20,  20, 'A')
B = Point(160, 111, 'B')
C = Point( 20, 202, 'C')
D = Point(300,  20, 'D')
E = Point(300, 202, 'E')

F = milieu(D, E)
F.round()
F.name = 'F'

V = Vector(A, B, name='V')
W = Vector(B, C, name='W')
Y = Vector(F, D, name='Y')
X = Vector(F, E, name='X')

U = V + W
U.name = 'U'

def example():
  draw_points([A, B, C, D, E, F], 'r', style='.')
  draw_rectangle(A, E)
  draw_croix(B, 320)
  bezier_curve([A, B, C, E], 'orange')
  bezier_curve([E, B, D, A], 'orange')
  draw_circle(B, 50, 'r')
  fill_circle(B, 10, 'r')
  draw_droite(D, E, 'cyan', "d'")
  draw_droite(D, B, 'cyan', "d''")
  draw_droite(E, B, 'cyan', "d'''")
  draw_vector(A, V, 'g')
  draw_vector(B, W, 'g')
  draw_vector(A, U, 'g')
  draw_arrows([(F, D)], 'b', fill=True)
  draw_arrows([(F, E)], 'b', fill=True)
  draw_polygone(6, 50, B)
  fill_polygone(6, 50, B, 'yellow', alpha=0.5)

example()
``` 

![example_visual.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/introduction/pictures/example_visual.png)

Then there are plenty of example files for everything to do with graphics. You can see the results with the following images :

* **Function interpolation** : [example_interpolation.py](src/visual/examples/functions/example_interpolation.py)  

| Example 1 | Example 2 | Example 3 | Example 4 |
|-----------|-----------|-----------|-----------|
| ![example_interpolate_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_interpolate_1.png) | ![example_interpolate_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_interpolate_2.png) | ![example_interpolate_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_interpolate_3.png) | ![example_interpolate_4.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_interpolate_4.png) |

* **Function expend** : [example_vectoriel_geometry](src/visual/examples/functions/example_vectoriel_geometry.py)

* **Function findWithPoint** : [example_findwithpoint.py](src/visual/examples/functions/example_findwithpoint.py)

* **Function alpha_pixel and argument "alpha" in draw function** : [example_alpha_layer.py](src/visual/examples/functions/example_alpha_layer.py)

> We have to take a number less or equal to 0, and greater or equal to 1 for the alpha parameter


| Example 1 | Example 2 |
|-----------|-----------|
| ![example_alpha_layer_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_alpha_layer_1.png) | ![example_alpha_layer_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_alpha_layer_2.png) |

* **Function scatter** : [example_scatter.py](src/visual/examples/functions/example_scatter.py)

| Example 1 | Example 2 | Example 3 |
|-----------|-----------|-----------|
| ![example_scatter_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_scatter_1.png) | ![example_scatter_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_scatter_2.png) | ![example_scatter_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_scatter_3.png) |

* **Function plot** : [example_plot.py](src/visual/examples/functions/example_plot.py)

| Example 1 | Example 2 | Example 3 |
|-----------|-----------|-----------|
| ![example_plot_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_plot_1.png) | ![example_plot_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_plot_2.png) | ![example_plot_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_plot_3.png) |

* **Function set_lines** : [example_lines.py](src/visual/examples/functions/example_lines.py)

| Example |
|---------|
| ![example_lines.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_lines.png) |

* **Function draw_points** : [example_point.py](src/visual/examples/functions/example_point.py)

| Example |
|---------|
| ![example_points.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_points.png) |

* **Function draw_croix** : [example_croix.py](src/visual/examples/functions/example_croix.py)

| Example |
|---------|
| ![example_croix.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_croix.png) |

* **Function draw_arrows** : [example_arrows.py](src/visual/examples/functions/example_arrows.py)

| Example |
|---------|
| ![example_arrows.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_arrows.png) |

* **Function draw_vector** : [example_vectors.py](src/visual/examples/functions/example_vectors.py)

| Example |
|---------|
| ![example_vectors.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_vectors.png) |

* **Function draw_droite** : [example_droite.py](src/visual/examples/functions/example_droite.py)

| Example 1 | Example 2 |
|-----------|-----------|
| ![example_droite_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_droite_1.png) | ![example_droite_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_droite_2.png) |

* **Function fill_triangles** : [example_triangle.py](src/visual/examples/functions/example_triangle.py)

| Example |
|---------|
| ![example_triangles.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_triangles.png) |

* **Function draw_polygone and fill_polygone** : [example_polygone.py](src/visual/examples/functions/example_polygone.py)

| Example |
|---------|
| ![example_polygones.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_polygones.png) |

* **Function draw_circle and fill_circle** : [example_cercle.py](src/visual/examples/functions/example_cercle.py)

| Example |
|---------|
| ![example_cercle.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_cercle.png) |

* **Function bezier curve** : [example_bezier_curve](src/visual/examples/functions/example_bezier_curve.py)

| Example 1 | Example 2 |
|-----------|-----------|
| ![example_bezier_curve.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_bezier_curve.png) | ![example_bezier_curve.gif](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/functions/pictures/example_bezier_curve.gif) |

## Tree Fractals
The link to the example script: [example_fractal.py](src/visual/examples/fractal/example_fractal.py)  
And the source script: [fractal.py](src/visual/examples/fractal/fractal.py)  

***

![example_bezier_curve.gif](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/example_fractals.gif)

***

> Don't forget to install the lines extension [here](src/visual/extensions/lines/ext_lines.py) in your computer !

| Basic Tree | Palm Tree |
|------------|-----------|
| ![fractale_basic_tree_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_basic_tree_1.png) | ![fractale_palm_red_yellow_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_palm_red_yellow_1.png) |
| ![fractale_basic_tree_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_basic_tree_2.png) | ![fractale_palm_red_yellow_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_palm_red_yellow_2.png) |
| ![fractale_basic_tree_black_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_basic_tree_black_1.png) | ![fractale_palm_black_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_palm_black_1.png) |
| ![fractale_basic_tree_black_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_basic_tree_black_2.png) | ![fractale_palm_black_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_palm_black_2.png) |

**Magenta Trees**
|           |           |           |           |
|-----------|-----------|-----------|-----------|
| ![fractale_magenta_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_1.png) | ![fractale_magenta_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_2.png) | ![fractale_magenta_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_3.png) | ![fractale_magenta_4.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_4.png) |
| ![fractale_magenta_thickness_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_thickness_1.png) | ![fractale_magenta_thickness_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_thickness_2.png) | ![fractale_magenta_thickness_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_thickness_3.png) | ![fractale_magenta_thickness_4.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_magenta_thickness_4.png) |

**Cyan Trees**
|           |           |           |
|-----------|-----------|-----------|
| ![fractale_cyan_angle_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_1.png) | ![fractale_cyan_angle_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_2.png) | ![fractale_cyan_angle_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_3.png) |
| ![fractale_cyan_angle_4.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_4.png) | ![fractale_cyan_angle_5.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_5.png) | ![fractale_cyan_angle_6.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_6.png) |
| ![fractale_cyan_angle_7.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_7.png) | ![fractale_cyan_angle_8.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_8.png) | ![fractale_cyan_angle_9.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_9.png) |
| ![fractale_cyan_angle_10.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_10.png) | ![fractale_cyan_angle_11.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_11.png) | ![fractale_cyan_angle_12.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_12.png) |
| ![fractale_cyan_angle_13.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_cyan_angle_13.png) |

**Examples of Trees**
|           |           |           |
|-----------|-----------|-----------|
| ![fractale_tree_blue.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_blue.png) | ![fractale_tree_cyan.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_cyan.png) | ![fractale_tree_fushia.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_fushia.png) |
| ![fractale_tree_green.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_green.png) | ![fractale_tree_magenta.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_magenta.png) | ![fractale_tree_orange.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_orange.png) |
| ![fractale_tree_pink.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_pink.png) | ![fractale_tree_purple.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_purple.png) | ![fractale_tree_red.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_red.png) |
| ![fractale_tree_yellow.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_yellow.png) | ![fractale_tree_white.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_tree_white.png) | ![fractale_thickness_purple.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_thickness_purple.png) |

**Angle Tree**
|           |           |
|-----------|-----------|
| ![fractale_h_magenta_purple.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_h_magenta_purple.png) | ![fractale_h_black.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/examples/fractal/pictures/fractale_h_black.png) |


## Extensions
***
Here are some extensions designed to work with the calculator. However, the latest extension, Grapher, will only work on a computer. They include a number of extra features, notably a reproduction of the turtle module, and another, much simpler one, of the matplotlib.pyplot module. I'll let you discover them with some beautiful images!

> You need to copy and paste the code from the extension files into a new file created on the Numworks website.

* **Extension Lines** : [lines_example.py](src/visual/extensions/lines/lines_example.py)

| Example |
|---------|
| ![example_lines.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/lines/pictures/example_lines.png) |

* **Extension Ellipses** : [example_ellipse.py](src/visual/extensions/ellipses/ellipses_example.py)

| Example 1 | Example 2 |
|-----------|-----------|
| ![example_ellipses_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/ellipses/pictures/example_ellipses_1.png) | ![example_ellipses_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/ellipses/pictures/example_ellipses_2.png) |

* **Extension Turtle** : [turtle_example.py](src/visual/extensions/turtle/turtle_example.py)


> The turtle extension has both a compact and a non-compact file for use on the computer.

***

| Example 1 | Example 2 |
|-----------|-----------|
| ![example_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/turtle/pictures/example_2.png) | ![example_turtle.gif](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/turtle/pictures/example_turtle.gif) |

* **Extension Grapher** : [grapher_example.ipynb](src/visual/extensions/grapher/notebooks/grapher_example.ipynb)  

<table>
    <thead>
        <th>Keys</th>
        <th>Short</th>
    </thead>
    <tbody>
        <tr>
            <td>Arrows [Up, Down, Right, Left]</td>
            <td>allows you to move around the grapher</td>
        </tr>
        <tr>
            <td>'Maj'+'=' or '+'</td>
            <td>zoom in or out</td>
        </tr>
        <tr>
            <td>'Maj'+'à' or '0'</td>
            <td>refocuses the graphic</td>
        </tr>
        <tr>
            <td>'Ctr'+'o'</td>
            <td>changes the emulator, thus increasing speed</td>
        </tr>
    </tbody>
</table>

**Examples**
|           |           |           |
|-----------|-----------|-----------|
| ![example_fonction_axes_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_1.png) | ![example_fonction_axes_poo_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_1.png) | ![example_fonction_axes_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_2.png) |
| ![example_fonction_axes_poo_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_2.png) | ![example_fonction_axes_poo_3.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_3.png) | ![example_fonction_axes_poo_4.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_4.png) |
| ![example_fonction_axes_poo_5.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_5.png) | ![example_fonction_axes_poo_6.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_axes_poo_6.png) | ![example_fonction_scatter_and_points_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_scatter_and_points_2.png) |
| ![example_fonction_plot_and_lines_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_plot_and_lines_1.png) | ![example_fonction_vector_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_vector_1.png) | ![example_fonction_droite_1.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/src/visual/extensions/grapher/pictures/example_fonction_droite_1.png) |

## QR-Codes
***
Here are two QR codes to easily find the Visual library on GitHub and on the official Numworks website. Use them without restriction!


| GitHub | Numworks |
|:--------:|:----------:|
| ![example_2.png](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/resources/qr_codes/qr_code_site_github.png) | ![example_turtle.gif](https://raw.githubusercontent.com/Archange-py/Visual/refs/heads/main/resources/qr_codes/qr_code_site_numworks.png) |

## FAQs
***
A list of frequently asked questions (for the moment there is none).
