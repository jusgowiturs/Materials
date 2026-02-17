import cocotb
from cocotb.triggers import Timer
import random




@cocotb.test()
async def adder_basic_test(dut):
    """Test the adder with random inputs"""
    for _ in range(10):
        a = random.randint(0, 15)
        b = random.randint(0, 15)

        dut.a.value = a
        dut.b.value = b

        
        await Timer(2, unit="ns")  # Wait 2ns for simulation

        expected_sum = a + b
        actual_sum = int(dut.sum.value)
        assert actual_sum == expected_sum, f"Addition of {a} and {b} result is incorrect: {actual_sum} != {expected_sum}"

    dut._log.info("All tests passed!")


@cocotb.test()
async def adder_basic_test_2(dut):
    """Test the adder with random inputs"""
    for _ in range(10):
        a = random.randint(0, 15)
        b = random.randint(0, 15)

        dut.a.value = a
        dut.b.value = b

        
        await Timer(2, unit="ns")  # Wait 2ns for simulation

        expected_sum = a + b
        actual_sum = int(dut.sum.value)
        assert actual_sum == expected_sum, f"Addition of {a} and {b} result is incorrect: {actual_sum} != {expected_sum}"

    dut._log.info("All tests passed!")