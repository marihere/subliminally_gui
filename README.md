<img src="https://github.com/marihere/subliminally_gui/blob/main/images/banner.png">

#

<p align="center">Subliminally GUI is a program designed to make creating subliminal audios as easy as possible.</p>
<br>

## Table of contents
1. [Introduction](https://github.com/marihere/subliminally_gui#introduction)
2. [Getting started](https://github.com/marihere/subliminally_gui#getting-started)
3. [Usage](https://github.com/marihere/subliminally_gui#usage)
4. [Example](https://github.com/marihere/subliminally_gui#example)
5. [Unlicense](https://github.com/marihere/subliminally_gui#unlicense)

<br>

## Introduction

Subliminally GUI is program  written with Python designed to make creating subliminal audios as easy as possible.


### How does it work?

Subliminally requests four different inputs: the main affirmations, the booster affirmations, an image file, and an audio file (e.g. a song of choice). <br>
These four inputs are then elaborated using a pretty simple algorithm. Here a pretty simplified version of the main algorithm:
<br>

<img src="https://github.com/marihere/subliminally_gui/blob/main/images/algorithm.png">

<br>

The algorithm behind the creation of the subliminal audio is the most important one. Here it is:

<img src="https://github.com/marihere/subliminally_gui/blob/main/images/algorithm_subaudio.png">
<br>
<i>affs is the affirmations audio file; bg is the background audio file; affs_length and bg_length are the duration (in seconds) of the respective audio files.</i>

<br>

## Getting started

Subliminally has two different versions:
- the <b>graphical user interface</b> (GUI) version;
- the <b>command line interface</b> (CLI) version.

Let's see the differences between the two:
| CLI | GUI |
|:---:|:---:|
| Maybe harder to use for beginners. | It is generally easier to use. |
| It is faster. | It is much slower. |
| Affirmations must be written in a file, before running the script. | Affirmations can be written while the program is running. |

<i>Please keep in mind that the GUI version contains a bug that may cause the program to crash.</i>

### Installation

#### GUI version

```console
$ git clone https://github.com/marihere/subliminally_gui
$ cd subliminally_gui
$ python -m pip install --upgrade pip setuptools virtualenv
$ python -m virtualenv kivy_venv
$ kivy_venv\Scripts\activate
$ python -m pip install -r requirements.txt
$ python .\lib\main.py
```

#### CLI version

The CLI version can be found [here](https://github.com/marihere/subliminally).

<br>

## Usage

### Step 1
Give a title to your subliminal and write the affirmations.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_0.png">
<br>

---

### Step 2
Click on _Start_.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_1.png">
<br>

---

### Step 3
Select an image of your choice.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_2.png">
<br>

---

### Step 4
Select an audio file of your choice.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_3.png">
<br>

---

### Step 5
Wait. Please do not click anywhere in the app as it may cause the program to crash.<br>
This may take a while.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_4.png">
<br>

---

### Step 6
Once the subliminal is fully ready, the video version will open up.
You can play the video with the 1st button, pause it with the 2nd one, and exit the current screen with the 3rd one.
<br>
<br>
<img src="https://github.com/marihere/subliminally_gui/blob/main/images/tutorial_5.png">

<br>

## Example

[Audio result](https://github.com/marihere/subliminally_gui/blob/main/example/audios/mysubliminal.wav)

[Video result](https://github.com/marihere/subliminally_gui/blob/main/example/videos/mysubliminal.mp4)

<br>

## Unlicense

[The Unlicense](https://github.com/marihere/subliminally_gui/blob/main/UNLICENSE)

<br>
