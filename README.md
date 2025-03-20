# Data Science Workbench

This repository contains various data science experiments and tutorials using RAPIDS, Polars, Pandas, and other data processing tools.

## Requirements

To run the code in this repository, you'll need:

- Python 3.8+
- RAPIDS cuDF (GPU-accelerated DataFrame library)
- Polars (Rust-based DataFrame library)
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Installation

1. Install RAPIDS cuDF following the official instructions:
   ```bash
   # Follow installation guide at:
   https://github.com/rapidsai/cudf
   ```

2. Install other Python dependencies:
   ```bash
   pip install polars pandas numpy matplotlib seaborn
   ```

## Project Details

### 10minstocudf
Contains practice files for the RAPIDS cuDF tutorial:
- Based on: https://docs.rapids.ai/api/cudf/nightly/user_guide/10min/
- Main dependencies: `cudf`, `cupy`, `dask_cudf`, `pandas`

### nvidia_summit
Contains practice files from NVIDIA Summit 2023 training:
- Based on: https://www.nvidia.com/en-us/on-demand/session/nvaidatasciencesummit23-02/
- Includes examples using Ibis and other GPU-accelerated tools

#
## Usage

To run any of the notebooks or scripts:

1. Ensure you have the required dependencies installed
2. For GPU-accelerated code, make sure you have compatible NVIDIA hardware
3. Download the QEDCorpus dataset for the Arabic dataset experiments

```bash
# Example: Running the 10minstocudf tutorial
cd 10minstocudf
python main.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
