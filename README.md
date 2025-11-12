# MITACS Blender Robotics Project

A comprehensive Blender-based robotics visualization and computer vision project for continuum/tendon robot arms, featuring 3D rendering, object detection, and camera calibration capabilities.

![Robot Visualization](side_and _tendons.png)

## 🎯 What This Project Does

This repository contains tools and scripts for:
- **Visualizing continuum/tendon robot arms** in 3D using Blender
- **Training custom object detection models** using YOLOv5
- **Calibrating cameras** for stereo vision systems
- **Rendering robot poses** from multiple camera angles
- **Working with URDF robot models** in Blender

## 📋 Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/leolorence12345/Mitacs_DeepLearningLab.git
   cd mitacs_blender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run a Blender script**
   ```bash
   blender --background --python render.py
   ```

See the [Installation](#installation) and [Usage](#usage) sections below for detailed instructions.

## Features

### 🎨 Blender Visualization
- Automated generation of robot backbone and tendon structures
- Multi-camera rendering (front view, side view)
- Disk placement along the backbone
- Material and lighting configuration
- Animation support for robot poses

### 🤖 Object Detection
- Custom YOLOv5 model training
- Dataset preparation and annotation tools
- Inference pipeline for robot component detection
- Bounding box visualization and label generation

### 📷 Camera Calibration
- Chessboard-based camera calibration
- Stereo camera calibration support
- Calibration result visualization

### 🔧 URDF Support
- Import robot models from URDF files
- Visualize robot assemblies in Blender
- Animation and pose manipulation

## 📁 Project Structure

```
mitacs_blender/
├── render.py              # Main rendering script for robot visualization
├── robot.py               # Robot pose manipulation
├── annot.py               # Annotation tools for object detection
├── calibration/           # Camera calibration scripts
│   └── cameraCalibration.py
├── Documentation/         # Project documentation and guides
│   ├── Backbone and tendons/  # Documentation for backbone setup
│   ├── Disks/                 # Disk configuration docs
│   └── Rendering/             # Rendering techniques
├── Custom_Object_Detection_using_YOLOv5.ipynb  # YOLOv5 training notebook
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore rules (excludes large files)
```

**Note**: Large files like `.blend` files, model checkpoints, and output folders are excluded from the repository but remain on your local machine.

## Requirements

### Software
- **Blender** 2.8+ (with Python API)
- **Python** 3.7+
- **PyTorch** (for YOLOv5)
- **OpenCV** (for camera calibration and image processing)
- **NumPy** (for numerical computations)

### Python Packages
```bash
pip install opencv-python numpy torch torchvision matplotlib
```

For YOLOv5:
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
```

## 📦 Installation

### Prerequisites
- **Blender 2.8+** - Download from [blender.org](https://www.blender.org/)
- **Python 3.7+** - Usually comes with Blender
- **Git** - For cloning the repository

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/leolorence12345/Mitacs_DeepLearningLab.git
   cd mitacs_blender
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Blender Python environment**
   - Blender comes with its own Python interpreter
   - For external scripts, you may need to install packages in Blender's Python
   - Or use Blender's bundled Python which includes many packages

## 🚀 Usage

### Rendering Robot Visualizations

Run the main rendering script in Blender:
```bash
blender --background --python render.py
```

Or open Blender and run the script:
```python
import bpy
exec(open("render.py").read())
```

The script will:
- Generate backbone and tendon structures based on position data
- Place disks along the backbone
- Render from multiple camera angles (front and side views)
- Save rendered images to the output folder

### Training Object Detection Model

1. Prepare your dataset with images and annotations
2. Open `Custom_Object_Detection_using_YOLOv5.ipynb` in Jupyter Notebook
3. Configure training parameters (epochs, batch size, etc.)
4. Run the training cells
5. Use the trained model for inference

### Camera Calibration

1. Capture calibration images using a chessboard pattern
2. Place images in the `calibration/` directory
3. Run the calibration script:
   ```bash
   python calibration/cameraCalibration.py
   ```
4. Review calibration results in `calibration/caliResult*.png`

### Annotating Images

Use the annotation tool to create bounding boxes and labels:
```python
python annot.py
```

Modify the script to specify:
- Image path
- Center points for bounding boxes
- Box dimensions
- Class labels

## ⚠️ Important Notes

### Path Configuration
Some scripts contain hardcoded Windows paths (e.g., `D:\\mitacs_blender\\`). You'll need to update these paths to match your local setup before running the scripts.

### Large Files Excluded
This repository excludes large files to keep it lightweight:
- **Blender files** (`.blend`, `.blend1`) - These are large binary files
- **Model checkpoints** (`.pt`, `.pth`) - Trained model weights
- **Media files** (`.mp4`, `.avi`, `.mkv`) - Video files
- **HDR/EXR files** - High dynamic range images
- **CAD files** (`.step`, `.STL`, `.SLDASM`) - 3D model files
- **Output folders** - Generated images and renders

These files remain on your local machine but are not tracked in git. See `.gitignore` for the complete list of excluded file types.

## Configuration

### Camera Settings
Modify camera configurations in `render.py`:
```python
camera_configurations = [
    {
        'location': (-0.6, 0, 0.70),
        'rotation_euler': (0, -math.pi/2, 0),
        'lens': 10,
        'filename': 'FRONT_view'
    },
    # Add more camera configurations...
]
```

### Robot Parameters
Adjust robot structure parameters in `render.py`:
- `bevel_depth`: Thickness of backbone and tendons
- `distance`: Distance between backbone and tendons
- `num_circles`: Number of disks along the backbone

## Output

Rendered images are saved to:
- `force/output_folder/` - Main rendering output
- `output_images/` - Additional image outputs
- `render_pose/` - Pose-specific renders

## Documentation

Additional documentation is available in the `Documentation/` folder:
- Backbone and tendons setup
- Disk configuration
- Rendering techniques
- MATLAB-Python integration

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is part of the MITACS research program. Please refer to the license file for details.

## Acknowledgments

- YOLOv5 by Ultralytics
- Blender Foundation
- OpenCV community

## Contact

For questions or issues, please open an issue on the repository.

---

**Note**: This project is under active development. Some features may be experimental or require additional configuration.
