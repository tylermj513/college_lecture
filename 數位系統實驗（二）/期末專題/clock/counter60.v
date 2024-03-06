
module counter60 (
 input clk,
 input clr,
 input load,
 input en,
 input [3:0] d0,
 input [3:0] d1,
 output reg [3:0] q0,
 output reg [2:0] q1,
 output co
);

assign co = q1[2] & q1[0] & q0[3] & q0[0]; // 101 1001 = 59

always@(posedge clk) begin
 if (clr) begin
 q0 <=0;
 q1 <=0;
 end
 else if (load) begin
 q0 <= d0;
 q1 <= d1;
 end
 else if (en) begin
 if (q0 ==9) begin
 q0 <=0;

 if (q1 ==5)
 q1 <=0;
 else
 q1 <= q1 +1;
 end
 else
 q0 <= q0 +1;
 end
 else begin
 q0 <= q0;
 q1 <= q1;
 end
end

endmodule