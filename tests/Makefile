SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/SimpleDUT.v
VERILOG_SOURCES += $(PWD)/wrappers/SimpleDUT_test.v
all: SimpleDUT 
SimpleDUT:
	rm -rf sim_build
	$(MAKE) sim MODULE=SimpleDUT_test TOPLEVEL=SimpleDUT_test
include $(shell cocotb-config --makefiles)/Makefile.sim
