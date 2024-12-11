module SimpleDUT (
    input clk, 
    input [3:0] din,
    output [3:0] dout
);
    // Logic for the DUT
    assign dout = din;
endmodule
