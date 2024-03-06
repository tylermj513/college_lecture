module lab4(str_out, match, rst, str_in, clk);
	input clk, rst, str_in ;
	output match;

	output [2:0]str_out;
	reg match;
	parameter state0 = 0, state1 = 1, state2 =  2,state3 = 3;
	reg[2:0]str_out;  
	reg cur_state, next_state; 

  always@(cur_state or str_in)//next state 
		begin 
			case(cur_state || str_in)
				state0:
					next_state = (str_in==0)?state1:state0;//a:b => if 1:0 what happen
				state1:
					next_state = (str_in==0)?state2:state0;
				state2:
					next_state = (str_in==0)?state2:state3;
				state3:
					next_state = (str_in==0)?state1:state0;
			endcase
		end 
		
      always@(posedge clk)//current state  shift
        begin
			if(rst) cur_state <= state0;
			else
				str_out[0] <= str_in;
				str_out[1] <= str_out[0];
				str_out[2] <= str_out[1];
        end
        
     

		always@(cur_state or str_in)//output logic
			begin
				if(str_out[2] && str_out[1] && !str_out[0])
					match = 1;
				else
					match = 0;
			end  
endmodule