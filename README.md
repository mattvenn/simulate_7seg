# Attempt at simulation of an extracted netlist

Aim is to measure average current of the circuit for first 50ps

* Used magic to extract wrapped_seven_segment.spice
* include skywater libs and wrapped_seven_segment.spice
* hold all inputs low
* plot current
* measure average current: -9.396809e-09 A
* takes about 8 mins on my newish desktop

![current](current.png)

# Setup

* ensure $PDK_ROOT/skywater-pdk/libraries/sky130_fd_pr/latest is checked out, otherwise you will need to do a git submodule init and update
* copy sky130.lib_tt.spice to $PDK_ROOT/skywater-pdk/libraries/sky130_fd_pr/latest/models/ (this includes all needed files and only the tt corner which makes simulation faster)
* Adjust the include on line 2 of simulation.spice to include the new sky130.lib_tt.spice
* make sure you are using a recent ngspice (34), older ones have memory leaks

# Questions

* Can I just leave all the subckt nodes unconnected? I am only interested in VGND, VPWR, wb_clk_i and active. 
    * gen_inputs.py generates all inputs set to 0
