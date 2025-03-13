# Conda

RAPIDS can be used with any conda distribution.

Below is an installation guide using miniforge.

## 1. Download and Run Install Script

Copy the command below to download and run the miniforge install script:

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh"
```

## 2. Customize Conda and Run the Install

Use the terminal window to finish installation. Note, we recommend enabling `conda-init`.

## 3. Start Conda

Open a new terminal window, which should now show Conda initialized.

## 4. Check Conda Configuration

Installing RAPIDS requires you to use `channel_priority: flexible`. You can check this and change it, if required, by doing:

```bash
conda config --show channel_priority
conda config --set channel_priority flexible
```

```bash
conda create -n rapids-25.02 -c rapidsai -c conda-forge -c nvidia  \  rapids=25.02 python=3.10 'cuda-version>=12.0,<=12.8'
```
important! say yes to everything

```bash
conda activate rapids-25.02
```
once we do this we can test if it´s working on the terminal writing:

```bash
python
import cudf
print(cudf.Series([1,2,3]))
---------
0       1
1       2
2       3
---------
```
we can also do `code .` to open vscode and inside there execute any code we want.
another option, and my preference is to use the wsl terminal inside vscode, go to our python file with the console, and do ``python main.py``