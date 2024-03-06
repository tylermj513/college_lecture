`timescale 1ns / 10ps
module Adder4bit_tb;
reg [3:0]a,b;
reg c_input;
wire [3:0]s;
wire c_output;
Adder4bit fatest(
 .a(a),
 .b(b),
 .c_input(c_input),
 .s(s),
 .c_output(c_output)
);

 initial begin 
 a=0;b=0;c_input=0;
 #10 a=4'b1011;b=4'b0100;c_input=0;
 #10 a=4'b0111;b=4'b1101;c_input=1;
 #10 $finish; 
 end 
 initial $monitor("a=%b,b=%b,c_input=%b,s=%b,c_output=%b",a,b,c_input,s,c_output); 
 //%b binary monitor variable
 endmodule