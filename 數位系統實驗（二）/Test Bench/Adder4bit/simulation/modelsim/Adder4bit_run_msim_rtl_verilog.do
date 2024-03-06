transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vlog -vlog01compat -work work +incdir+C:/altera/91sp2/quartus/Adder4bit {C:/altera/91sp2/quartus/Adder4bit/Adder4bit.v}

vlog -vlog01compat -work work +incdir+C:/altera/91sp2/quartus/Adder4bit {C:/altera/91sp2/quartus/Adder4bit/Adder4bit_tb.v}

vsim -t 1ps -L altera_ver -L lpm_ver -L sgate_ver -L altera_mf_ver -L stratixii_ver -L rtl_work -L work -voptargs="+acc" Adder4bit_tb

add wave *
view structure
view signals
run -all
