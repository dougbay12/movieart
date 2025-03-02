# Movie Frame Extractor and Concatenator

This tool extracts I-frames from a movie file and concatenates them into a single image. It uses ffmpeg for frame extraction and ImageMagick for image concatenation.

## Requirements

- `ffmpeg` must be installed and available in your PATH.
- `ImageMagick` must be installed and available in your PATH.

## Installation

To install `ffmpeg` and `ImageMagick`, you can use the following commands:

### Ubuntu/Debian

```sh
sudo apt-get update
sudo apt-get install ffmpeg imagemagick