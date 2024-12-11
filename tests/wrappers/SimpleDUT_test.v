module SimpleDUT_test(
    input clk,     
	input [3:0] din,
    output [3:0] dout
);
SimpleDUT SimpleDUT (
  .clk(clk), 
  .din(din), // input [3:0]  din,
  .dout(dout)); // output [3:0] dout

initial begin
	$dumpfile("SimpleDUT.vcd");
	$dumpvars;
end
endmodule
