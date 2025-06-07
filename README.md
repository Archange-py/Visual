<p align="center" width="100%">
<img src=".\resources\logo\logo_visual_flag.png" alt="Visual">
</p>

# Visual

[![GitHub Stars](https://img.shields.io/github/stars/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/network)
[![GitHub Issues](https://img.shields.io/github/issues/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/pulls)
[![GitHub License](https://img.shields.io/github/license/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/Archange-py/Visual.svg)](https://github.com/Archange-py/Visual/commits/main)
![Visiteurs](https://visitor-badge.laobi.icu/badge?page_id=Archange-py.Visual)

[![Tests](https://github.com/Archange-py/Visual/actions/workflows/tests.yml/badge.svg)](https://github.com/Archange-py/Visual/actions/workflows/tests.yml)
[![Build](https://github.com/Archange-py/Visual/actions/workflows/build.yml/badge.svg)](https://github.com/Archange-py/Visual/actions/workflows/build.yml)

[![PyPI Version](https://img.shields.io/pypi/v/visual.svg)](https://pypi.org/project/visual/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/visual.svg)](https://pypi.org/project/visual/)
[![Python Versions](https://img.shields.io/pypi/pyversions/visual.svg)](https://pypi.org/project/visual/)


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

2. You just need to copy and paste the code from the *[visual](.\src\visual\visual.py)* file into a new script on your Numworks account. Then upload it to your calculator. 

> Here's an example of what you can do with the calculator, using the [example file](.\src\visual\examples\introduction\visuel_first_example.py). Click [here](https://my.numworks.com/python/archange/example_visual) to see it on the Numworks website.  
> <img src="src\visual\examples\introduction\pictures\example_visuel.png">


> Here's another example of what you can do with the functions provided by Visual.
> <img src="src/visual/examples/functions/pictures/examples.gif">

If you have any questions, go to the [FAQs section](#faqs), or explore all the examples [here](#examples) after visiting this [page](#how-to-use-it) to install **kandinsky** and **ion** on your computer !  

## How to use it
***

1. Simply use this command :
```bash
pip install kandinsky
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
After that, you need to understand how this script is organized, with points and vectors for example, and how it works, with its functions. For this purpose, you have at your disposal one *Jupiter Notebook* containing everything that can be shown in writing for the file [visual_example](src\visual\examples\functions\notebooks\visuel_example.ipynb). Then there are plenty of example files for everything to do with graphics. You can see the results with the following images :

* **Function interpolation** : [example_interpolation.py](src\visual\examples\functions\example_interpolation.py)  

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
            <th align="center">Example 3</th>
            <th align="center">Example 4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_interpolate_1.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_interpolate_2.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_interpolate_3.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_interpolate_4.png"> </td>
        </tr>
    </tbody>
</table>

* **Function expend** : [example_vectoriel_geometry](src\visual\examples\functions\example_vectoriel_geometry.py)

* **Function findWithPoint** : [example_findwithpoint.py](src\visual\examples\functions\example_findwithpoint.py)

* **Function alpha_pixel and argument "alpha" in draw function** : [example_alpha_layer.py](src\visual\examples\functions\example_alpha_layer.py)

> We have to take a number less or equal to 0, and greater or equal to 1 for the alpha parameter

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_alpha_layer_1.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_alpha_layer_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Function scatter** : [example_scatter.py](src\visual\examples\functions\example_scatter.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
            <th align="center">Example 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_scatter_1.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_scatter_2.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_scatter_3.png"> </td>
        </tr>
    </tbody>
</table>

* **Function plot** : [example_plot.py](src\visual\examples\functions\example_plot.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
            <th align="center">Example 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_plot_1.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_plot_2.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_plot_3.png"> </td>
        </tr>
    </tbody>
</table>

* **Function set_lines** : [example_lines.py](src\visual\examples\functions\example_lines.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_lines.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_points** : [example_point.py](src\visual\examples\functions\example_point.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_points.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_croix** : [example_croix.py](src\visual\examples\functions\example_croix.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_croix.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_arrows** : [example_arrows.py](src\visual\examples\functions\example_arrows.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_arrows.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_vector** : [example_vectors.py](src\visual\examples\functions\example_vectors.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_vectors.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_droite** : [example_droite.py](src\visual\examples\functions\example_droite.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_droite_1.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_droite_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Function fill_triangles** : [example_triangle.py](src\visual\examples\functions\example_triangle.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_triangles.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_polygone and fill_polygone** : [example_polygone.py](src\visual\examples\functions\example_polygone.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_polygones.png"> </td>
        </tr>
    </tbody>
</table>

* **Function draw_circle and fill_circle** : [example_cercle.py](src\visual\examples\functions\example_cercle.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_cercle.png"> </td>
        </tr>
    </tbody>
</table>

* **Function bezier curve** : [example_bezier_curve](src\visual\examples\functions\example_bezier_curve.py)

<table>
    <thead>
        <tr>
            <th align="center">Examples</th>
            <th align="center">Examples</th>
            <th align="center">Examples</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_2.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_3.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_4.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_5.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_6.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_7.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_8.png"> </td>
            <td> <img src="src\visual\examples\functions\pictures\example_bezier_curve_9.png"> </td>
        </tr>
    </tbody>
</table>

## Tree Fractals
The link to the example script: [example_fractal.py](src\visual\examples\fractal\example_fractal.py)  
And the source script: [fractal.py](src\visual\examples\fractal\fractal.py)  

***

<img src="src\visual\examples\fractal\pictures\example_fractals.gif" alt="Visuel">

***

> Don't forget to install the lines extension [here](src\visual\extensions\lines\ext_lines.py) in your computer !

<table>
    <thead>
        <tr>
            <th align="center">Basics Tree</th>
            <th align="center">Palmier</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_basic_tree_1.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_palm_red_yellow_1.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_basic_tree_2.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_palm_red_yellow_2.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_basic_tree_black_1.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_palm_black_1.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_basic_tree_black_2.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_palm_black_2.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
            <th align="center">Cyan Tree</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_1.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_2.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_3.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_4.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_thickness_1.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_thickness_2.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_thickness_3.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_magenta_thickness_4.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Magenta Tree</th>
            <th align="center">Magenta Tree</th>
            <th align="center">Magenta Tree</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_1.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_2.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_3.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_4.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_5.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_6.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_7.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_8.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_9.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_10.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_11.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_12.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_cyan_angle_13.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Examples Trees</th>
            <th align="center">Examples Trees</th>
            <th align="center">Examples Trees</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_blue.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_cyan.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_fushia.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_green.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_magenta.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_orange.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_pink.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_purple.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_red.png"> </td>
        </tr>
    </tbody>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_yellow.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_tree_white.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_thickness_purple.png"> </td>
        </tr>
    </tbody>
</table>

<table>
    <thead>
        <tr>
            <th align="center">Angle Tree </th>
            <th align="center">Angle Tree </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_h_magenta_purple.png"> </td>
            <td> <img src="src\visual\examples\fractal\pictures\fractale_h_black.png"> </td>
        </tr>
    </tbody>
</table>

## Extensions
***
Here are some extensions designed to work with the calculator. However, the latest extension, Grapher, will only work on a computer. They include a number of extra features, notably a reproduction of the turtle module, and another, much simpler one, of the matplotlib.pyplot module. I'll let you discover them with some beautiful images!

> You need to copy and paste the code from the extension files into a new file created on the Numworks website.

* **Extension Lines** : [lines_example.py](src\visual\extensions\lines\lines_example.py)

<table>
    <thead>
        <tr>
            <th align="center">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\extensions\lines\pictures\example_lines.png"> </td>
        </tr>
    </tbody>
</table>


* **Extension Ellipses** : [example_ellipse.py](src\visual\extensions\ellipses\ellipses_example.py)

<table>
    <thead>
        <tr>
            <th align="center">Example 1</th>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\extensions\ellipses\pictures\example_ellipses_1.png"> </td>
            <td> <img src="src\visual\extensions\ellipses\pictures\example_ellipses_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Extension Turtle** : [turtle_example.py](src\visual\extensions\turtle\turtle_example.py)


> The turtle extension has both a compact and a non-compact file for use on the computer.

***

<img src="src\visual\extensions\turtle\pictures\example_turtle.gif" alt="Visuel">


<table>
    <thead>
        <tr>
            <th align="center">Example 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src=".\src\visual\extensions\turtle\pictures\example_2.png"> </td>
        </tr>
    </tbody>
</table>

* **Extension Grapher** : [grapher_example.ipynb](src\visual\extensions\grapher\notebooks\grapher_example.ipynb)  

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

<table>
    <thead>
        <tr>
            <th align="center">Examples :</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_1.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_1.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_2.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_2.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_3.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_4.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_5.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_axes_poo_6.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_scatter_and_points_2.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_plot_and_lines_1.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_vector_1.png"> </td>
        </tr>
        <tr>
            <td> <img src="src\visual\extensions\grapher\pictures\example_fonction_droite_1.png"> </td>
        </tr>
    </tbody>
</table>

## QR-Codes
***
Here are two QR codes to easily find the Visual library on GitHub and on the official Numworks website. Use them without restriction!

<style>
.qr {
    width: 300px;
    height: 300px;
    object-fit: cover;
}
</style>

<table>
    <thead>
        <tr>
            <th>GitHub</th>
            <th>Numworks</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="./resources/qr_codes/qr_code_site_github.png" class="qr"></td>
            <td><img src="./resources/qr_codes/qr_code_site_numworks.png" class="qr"></td>
        </tr>
    </tbody>
</table>

## FAQs
***
A list of frequently asked questions (for the moment there is none).
