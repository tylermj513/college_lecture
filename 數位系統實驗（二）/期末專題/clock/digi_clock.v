
module digi_clock (
 input CLOCK_50,
 input [17:0] SW,
 input [3:0] KEY,
 output [6:0] HEX2,
 output [6:0] HEX3,
 output [6:0] HEX4,
 output [6:0] HEX5,
 output [6:0] HEX6,
 output [6:0] HEX7
);

wire clk_1;
wire [3:0] w_sq0;
wire [2:0] w_sq1;
wire [3:0] w_mq0;
wire [2:0] w_mq1;
wire [3:0] w_hq0;
wire [2:0] w_hq1;

// 1Hz clock
divn # (.WIDTH(26), .N(50000000))
u0 (
 .clk(CLOCK_50),
 .rst_n(KEY[0]),
 .o_clk(clk_1)
);

clock u1 (
 .clk(clk_1),
 .en(SW[17]), // input enable
 .clr(SW[16]), // input clear
 .load(SW[15]), // input load
 .sd0(4'h0), // input second digit 0
 .sd1(3'h0), // input second digit 1
 .md0(SW[3:0]), // input minute digit 0
 .md1(SW[6:4]), // input minute digit 1
 .hd0(SW[10:7]), // input hour digit 0
 .hd1(SW[13:11]), // input hour digit 1
 .sq0(w_sq0), // output second digit 0
 .sq1(w_sq1), // output second digit 1
 .mq0(w_mq0), // output minute digit 0
 .mq1(w_mq1), // output minute digit 1
 .hq0(w_hq0), // output minute digit 0
 .hq1(w_hq1) // output minute digit 1
);

// sec. dig0 to seg7
seg7_lut u2 (
 .i_dig(w_sq0),
 .o_seg(HEX2)
);

// sec. dig1 to seg7
seg7_lut u3 (
 .i_dig({1'b0, w_sq1}),
 .o_seg(HEX3)
);

// min. dig0 to seg7
seg7_lut u4 (
 .i_dig(w_mq0),
 .o_seg(HEX4)
);

// min. dig1 to seg7
seg7_lut u5 (
 .i_dig({1'b0, w_mq1}),
 .o_seg(HEX5)
);

// hour dig0 to seg7
seg7_lut u6 (
 .i_dig(w_hq0),
 .o_seg(HEX6)
);

// hour dig1 to seg7
seg7_lut u7 (
 .i_dig({1'b0, w_hq1}),
 .o_seg(HEX7)
);

endmodule