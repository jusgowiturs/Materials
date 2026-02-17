`timescale 1ns/1ps

module adder_tb;

    // Testbench signals
    logic [3:0] a;
    logic [3:0] b;
    logic [4:0] sum;

    // Instantiate DUT
    adder dut (
        .a(a),
        .b(b),
        .sum(sum)
    );

    initial begin
        $display("Starting Adder Testbench");

        // Test 1
        a = 4'd3; b = 4'd2;
        #10;
        $display("a=%0d b=%0d sum=%0d", a, b, sum);

        // Test 2
        a = 4'd7; b = 4'd8;
        #10;
        $display("a=%0d b=%0d sum=%0d", a, b, sum);

        // Test 3
        a = 4'd15; b = 4'd15;
        #10;
        $display("a=%0d b=%0d sum=%0d", a, b, sum);

        $display("Testbench Completed");
        $finish;
    end

endmodule
