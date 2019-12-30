# Epicycle Drawer

## Introduction
This is a tool that takes in a drawing as input from the user and draws it using epicycles.
### What are epicycles and epicycle drawings?
An epicycle is a circle, with a small radius, whose center revolves on the circumference of another circle of larger radius. The path traced by a point on the smaller circle can be manipulated to form various different shapes. This is demonstrated in the image below.
<br><br>
![epicycle-gif](img/epicycles.gif)
<br>
Multiple circles can be arranged and made to rotate at different speeds and in different phases. The path of a point on the last such circle can be traced, to create a drawing. The aim of this project is to take a desired drawing as input, and arrange circles in such a way that the path of a point on the last circle results in the desired drawing.

## Example

### Input
![drawing-input](img/drawing-input.gif)
### Epicycle Drawing
![epicycle-drawing](img/epicycle-drawing.gif)
### Plots
![3d-epicycle](img/epicycle-3d.gif)
![plot-1](img/plot-1.png)
![plot-2](img/plot-2.png)
![plot-3](img/plot-3.png)


## Usage

Clone this repo into a local directory.

It is recommended to run this project in a virtual environment, running Python 3(preferably Python 3.6).
Install and create the environment using
```shell
  pip3.6 install virtualenv
  virtualenv -p $(which python3.6) newvenv
```
Activate it using
```shell
  source newvenv/bin/activate
```
Install the necessary packages with
```shell
  pip install -r requirements.txt
```
Run the notebook with ```jupyter notebook``` <br>
The settings cell can be changed as required. <br>
You can either run the cells manually(use `Shift+Enter` to run a cell and move to the next one) or use the 'Run All Cells' option. <br>
To run the program again, use the `Restart and Clear Output` option.

###### NOTE
If the `save_anim` option is set to 1, then make sure to allow time for the animation to be saved, before running any other cells.

## To-Do
* [ ] Generate epicycles for pre-existing image
  * [ ] Get sample points in order of appearance

## Ideas & Software Used
* Python 3.6
* Fourier Transforms

## Author(s)
[Ahish Deshpande](https://github.com/Ahish9009)
