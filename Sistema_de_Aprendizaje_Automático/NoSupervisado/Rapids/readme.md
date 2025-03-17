# Conda Installation for RAPIDS  

RAPIDS can be used with any Conda distribution. This guide covers installation using **Miniforge**.  

## 1. Download and Install Miniforge  

Run the following command to **download and execute** the Miniforge installation script:  

```bash
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
```

Follow the prompts to complete the installation. We **recommend enabling `conda-init`** when prompted.  

## 2. Verify Conda Installation  

Open a **new terminal window** to ensure Conda is initialized properly.  

Check the Conda configuration for `channel_priority`:  

```bash
conda config --show channel_priority
```

Ensure it's set to `flexible`:  

```bash
conda config --set channel_priority flexible
```

## 3. Install RAPIDS  

Create a Conda environment for RAPIDS:  

```bash
conda create -n rapids-25.02 -c rapidsai -c conda-forge -c nvidia  \
  rapids=25.02 python=3.10 'cuda-version>=12.0,<=12.8'
```

⚠️ **Important:** Accept all prompts during installation (`y` to everything).  

Once installed, activate the environment:  

```bash
conda activate rapids-25.02
```

## 4. Test the Installation  

To verify RAPIDS is working, run the following in the terminal:  

```bash
python
import cudf
print(cudf.Series([1, 2, 3]))
```

Expected output:  

```
0    1
1    2
2    3
dtype: int64
```

## 5. Running Code in VS Code  

To open **VS Code** in the current directory:  

```bash
code .
```

### Preferred Setup: WSL Terminal in VS Code  

1. Open **VS Code** and use the **WSL terminal**.  
2. Navigate to your Python file directory:  

   ```bash
   cd /path/to/your/project
   ```

3. Run your script:  

   ```bash
   main.py
   ```

This ensures a smooth RAPIDS experience inside VS Code with WSL. 🚀