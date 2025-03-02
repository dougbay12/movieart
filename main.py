import os
import subprocess
import argparse
# this script automates the process of extracting key frames from a video and combining them into a single image


def concatenate_frames():
    input_folder = "i_frames_output"
    output_image = "concat_pic_out/image.jpg"

    # Construct the ImageMagick command to concatenate frames horizontally
    imagemagick_command = [
        "convert",
        f"{input_folder}/*.jpg",
        "+append",
        output_image
    ]

    # Run the command and capture any errors
    try:
        subprocess.run(imagemagick_command, check=True)
        print(f"All frames have been concatenated into {output_image}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("ImageMagick is not installed or not in your PATH environment variable.")


def extract_iframes(video_file):
    output_folder = "i_frames_output/"
    os.makedirs(output_folder, exist_ok=True)
    # Construct the ffmpeg command to extract I-frames
    ffmpeg_command = [
        "ffmpeg",
        "-i", video_file,
        # "-t", "60",
        "-vf", "select='eq(pict_type,I)',scale=2:320",
        "-vsync", "vfr",
        f"{output_folder}/frame_%04d.jpg"
    ]

    # Run the command and capture any errors
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"All I-frames have been exported to {output_folder}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
    except FileNotFoundError:
        print("ffmpeg is not installed or not in your PATH environment variable.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract I-frames from a video file and concatenate them into a single image.")
    parser.add_argument("video_file", help="Path to the video file")
    args = parser.parse_args()

    print(f"Video file: {args.video_file}")

    extract_iframes(args.video_file)
    concatenate_frames()
