# ASCII Render

ASCII Render is a Python project that converts images and videos into ASCII art, with an optional feature to add color to the output. The project provides a fun way to visualize media using text characters.

## Features

- **Image and Video Rendering**: Supports rendering both static images and video files into ASCII art.
- **Color Support**: Optionally render ASCII art with color based on the original image or video.
- **Customizable Character Set**: Switch between different character sets to achieve varying levels of detail in the ASCII output.

## Installation

### Prerequisites

- Python 3.6 or higher
- Virtual environment (optional but recommended)

### Steps

1. **Clone the repository**:

   ```bash
   git clone `https://github.com/davidumoru/ascii-render.git`
   cd ascii-render
   ```

2. **Create and activate a virtual environment**:
   - On macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     python3 -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

To convert an image or video file into ASCII art, run the following command:

```bash
python src/main.py <file-path> [options]
```

### Options

- `-c` : Enable color rendering of ASCII art.
- `-f` : Use a different character set for rendering.

### Examples

- Convert an image to ASCII art without color:

  ```bash
  python src/main.py src/assets/example.jpg
  ```

- Convert a video to ASCII art with color:

  ```bash
  python src/main.py src/assets/example.mp4 -c
  ```

- Convert an image to ASCII art using a custom character set:

  ```bash
  python src/main.py src/assets/example.png -f
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
