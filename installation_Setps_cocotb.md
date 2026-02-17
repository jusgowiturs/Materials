<!-- # Step 0
sudo apt update
sudo apt install -y python3 python3-pip python3-venv iverilog

python3 --version
python3 -m pip --version
iverilog -V
# Step 1 Creation of environmental Variable 
source .venv/bin/activate
(.venv) jusgowiturs@NPTEL007:~/cocotb$

## Verification
which python
/home/jusgowiturs/cocotb/.venv/bin/python
## Install Cocotb
pip install --upgrade pip
pip install cocotb

python -c "import cocotb; print(cocotb.__version__)"



# Pyhone Error assertion
 pip install pytest
# WAVE Output
sudo apt install gtkwave   



# AXI interface
pip install cocotbext-axi
# For varification
python -c "from cocotbext.axi import AxiLiteBus, AxiLiteMaster; print('OK')"


# Uninstall verilator
sudo apt remove verilator # 2️⃣ Remove the package
# Remove completely (including configs)
sudo apt purge verilator 
# Clean up unused dependencies
sudo apt autoremove      
# install Verilator
sudo apt update
sudo apt install verilator
verilator --version
## Find method to install verilator >5.39
 -->
# Cocotb + AXI + Verilator Setup Guide

This guide explains how to set up a Python virtual environment for Cocotb, install required packages, configure waveform viewing, and manage Verilator.

---

## Step 0: System Preparation

Update packages and install required tools:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv iverilog
Verify installations:

python3 --version
python3 -m pip --version
iverilog -V
```
## Step 1: Create and Activate Python Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
Verify the active Python environment:

which python
```
## Step 2: Install Cocotb
-   Upgrade pip and install Cocotb:
    ```bash
    pip install --upgrade pip
    pip install cocotb
    ```
-   Verify installation:
    ```bash
    python -c "import cocotb; print(cocotb.__version__)"
    ```
## Step 3: Additional Python Packages
-   Install pytest:
```bash
pip install pytest
```
-   Install Cocotb AXI extension:
```bash
pip install cocotbext-axi
```
-   Verify AXI installation:
```bash
python -c "from cocotbext.axi import AxiLiteBus, AxiLiteMaster; print('OK')"
```

## Step 4: Waveform Viewer
-   Install GTKWave for waveform visualization:
```bash
sudo apt install gtkwave
```
## Step 5: Verilator Installation / Upgrade
-   Remove existing Verilator (if any):
```bash
sudo apt remove verilator
sudo apt purge verilator
sudo apt autoremove
```
## Install Verilator:
```bash
sudo apt update
sudo apt install verilator
verilator --version
```
-   Optional: For Verilator >5.39, build from source:

```bash
sudo apt install git autoconf g++ flex bison
git clone https://github.com/verilator/verilator.git
cd verilator
git checkout stable  # or a specific version tag
autoconf
./configure
make -j$(nproc)
sudo make install
verilator --version
```
Step 6: Using the Environment
-   Activate the virtual environment before running simulations:
```bash
source .venv/bin/activate
```
Run Cocotb simulations:

```bash
    make
```