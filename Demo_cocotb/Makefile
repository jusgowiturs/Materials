TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/RTL/adder.v
TOPLEVEL = adder
COCOTB_TEST_MODULES  = test_adder
export PYTHONPATH := $(PWD)/Testbench:$(PYTHONPATH)

SIM = icarus

include $(shell cocotb-config --makefiles)/Makefile.sim
