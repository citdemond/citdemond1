import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, FallingEdge
from cocotb_bus.drivers import BusDriver
from cocotb.result import TestFailure
from cocotb.triggers import Event
#The SimpleDUTDriver is responsible for driving inputs to the din signal of the DUT.
class SimpleDUTDriver(BusDriver):
    _signals = ["din"]  # Define the list of signals to be driven

    def __init__(self, dut, clock):
        BusDriver.__init__(self, dut, None, dut.clk)  # Connect to the clock signal


@cocotb.coroutine
# The stimulus coroutine drives inputs to the DUT's din signal using the dut.din assignment. It uses the RisingEdge trigger to synchronize with the DUT's clock.
async def stimulus(dut):
    dut._log.info("Running stimulus...")

    # Drive some inputs
    for i in range(16):
        dut.din = i
        await FallingEdge(dut.clk)

    dut._log.info("Stimulus complete.")

@cocotb.coroutine
# The check_output coroutine verifies the DUT's output by comparing it with the expected values. It raises a TestFailure if the output does not match the expected value.
async def check_output(dut):
    dut._log.info("Checking output...")
    await Timer(1, "ns")
    # Verify the output
    for i in range(16):
        expected_output = i
        if dut.dout != expected_output:
            raise TestFailure(f"Output mismatch: Expected {expected_output}, got {dut.dout}")
        
        await RisingEdge(dut.clk)

    dut._log.info("Output check passed.")

@cocotb.test()
async def test_simple_dut(dut):
    # Create an event
    # the test case my_test creates an instance of the Event class called my_event
    my_event = Event()
    
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())
    cocotb.start_soon(stimulus(dut))
    
    # Start a coroutine that waits for the event
# It then starts a coroutine wait_for_event that waits for the event to be triggered using await event.wait().
    # event_waiter = cocotb.fork(wait_for_event(my_event))
    
    #cocotb.fork(Clock(dut.clk, 10, "ns").start())
    #cocotb.fork(stimulus(dut))
    #By using await check_output(dut), the test function will pause its execution at that point and resume only when the check_output coroutine has completed. 
    await check_output(dut)


