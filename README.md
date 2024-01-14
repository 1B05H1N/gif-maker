# gif-maker

A simple and efficient Python script that takes a series of images from a specified directory and compiles them into a single GIF animation.

## Features

- **Easy to Use**: Just run the script with the directory of images, and get a GIF!
- **Flexible**: Specify the duration of each frame in the GIF.
- **Custom Output**: Save the GIF in a specified output directory.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- PIL (Pillow) library installed (`pip install pillow`)

## Installation

To install gif-maker, follow these steps:

Linux and macOS:

```bash
git clone https://github.com/yourusername/gif-maker.git
cd gif-maker
```

Windows:

```bash
git clone https://github.com/yourusername/gif-maker.git
cd gif-maker
```

## Using gif-maker

To use gif-maker, follow these steps:

```bash
python3 gif-maker.py <input_folder> <output_folder> <duration_ms>
```

Where:
- `<input_folder>` is the directory containing the images you want to make a GIF from.
- `<output_folder>` is the directory where the GIF will be saved.
- `<duration_ms>` is the duration each image will show in the GIF in milliseconds.

For example:

```bash
python3 gif-maker.py ./images ./output 50
```

This will compile all images in `./images` into a GIF and save it to `./output` with each frame lasting 50 milliseconds.

## Contributing to gif-maker

To contribute to gif-maker, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).
