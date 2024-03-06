module FA(A, B, S, C_in, C_out);
input A, B, C_in;
output S, C_out;
assign S = A ^ B ^ C_in,
 C_out = ((A ^ B) & C_in) | (A & B);
endmodule

module Adder4bit(a, b, s, c_input, c_output);
input [3:0]a, b;
input c_input;
output [3:0]s;
output c_output;
wire [3:0]c;
FA U0(.A(a[0]), .B(b[0]) ,.S(s[0]), .C_in(c_input), .C_out(c[1]));
FA U1(.A(a[1]), .B(b[1]) ,.S(s[1]), .C_in(c[1]), .C_out(c[2]));
FA U2(.A(a[2]), .B(b[2]) ,.S(s[2]), .C_in(c[2]), .C_out(c[3]));
FA U3(.A(a[3]), .B(b[3]) ,.S(s[3]), .C_in(c[3]), .C_out(c_output));
endmodule