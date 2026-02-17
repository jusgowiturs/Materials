#  Cocotb Tutorial: 4-Bit Adder Verification

## Overview

This project demonstrates Python-based hardware verification of a 4-bit Verilog adder using **cocotb** with **Icarus Verilog**.

### Goals

- Python-driven hardware verification  
- Random stimulus generation  
- Assertion-based checking  
- Automated regression using Makefile  

---

##  Design Under Test (DUT)

A simple 4-bit adder.

[RTL File](./RTL/adder.v): `RTL/adder.v`

### Interface

- **Inputs**
  - `a` : 4-bit
  - `b` : 4-bit
- **Output**
  - `sum` : 5-bit

The adder supports values from **0 to 30**.

---

##  Testbench Description

 [Testbench File](./Testbench/test_adder.py): `Testbench/test_adder.py`

The testbench is written in Python using cocotb.

### adder_basic_test
- Generates 10 random input pairs
- Applies them to the DUT
- Waits 2 ns
- Computes expected result in Python
- Uses assertion to verify correctness

### adder_basic_test_2
- Same structure as above
- Demonstrates multiple test execution

---

###  Random Stimulus

```python
random.randint(0, 15)
```

## Expected Output

```bash
expected_sum = a + b
```
##  Simulation Guide

### Install Requirements

Make sure the following tools are installed:

- cocotb  
- Icarus Verilog  

---

### Activate Virtual Environment (If Used)

```bash
source <cocotb_venv>/bin/activate
```

### Run Simulation
```bash
make
```
### Expected output
```bash
TESTS=2 PASS=2 FAIL=0 SKIP=0
```
### Manual Execution of sim.vvp

When running manually, export the required environment variables (normally set automatically by `make`):

```bash
export COCOTB_TEST_MODULES=test_adder
export TOPLEVEL=adder
export TOPLEVEL_LANG=verilog
```
then
```bash
vvp -M <PATH>/site-packages/cocotb/libs \
    -m libcocotbvpi_icarus \
    sim_build/sim.vvp
```




# Cocotb Makefile Explanation

This [Makefile](./Makefile) is used to run cocotb simulations for the 4-bit adder.

---

##  `TOPLEVEL_LANG = verilog`

Specifies the HDL language of the **Design Under Test (dut)**.

- Here, the DUT is written in **Verilog**.  
- cocotb supports multiple HDL languages, so this tells cocotb how to interpret the source.

---

## `VERILOG_SOURCES = $(shell pwd)/RTL/adder.v`

Specifies the path to the Verilog source files.

- `$(shell pwd)` returns the **current working directory**.  
- `RTL/adder.v` is the file containing the adder module.  
- cocotb will pass this to the simulator to compile the dut.

---

## `TOPLEVEL = adder`

Defines the **top-level module name** in your HDL code.

- This is the module that cocotb will hook into for simulation.  
- In your project, the module name is `adder`.

---

## `COCOTB_TEST_MODULES = test_adder`

Specifies the **Python testbench module** to run.

- cocotb will import this Python module and execute all tests defined inside.  
- Here, the testbench file is `Testbench/test_adder.py` (without `.py`).

---

## `export PYTHONPATH := $(PWD)/Testbench:$(PYTHONPATH)`

Adds the testbench folder to Python’s import path.

- Ensures Python can find `test_adder.py` when cocotb imports it.  
- `$(PWD)/Testbench` is prepended to the existing `PYTHONPATH`.

---

## `SIM = icarus`

Specifies which **Verilog simulator** to use.

- Here, `icarus` refers to **Icarus Verilog**.  
- cocotb supports multiple simulators (VCS, ModelSim, Xcelium, etc.), and this tells it which one to invoke.

---

## `include $(shell cocotb-config --makefiles)/Makefile.sim`

Includes the **cocotb-provided Makefile** for simulation.

- `cocotb-config --makefiles` returns the path to cocotb’s standard Makefiles.  
- `Makefile.sim` contains all the boilerplate to compile, run, and report simulation results.  
- By including it, you don’t have to write the simulator commands manually — cocotb handles it automatically.

---
