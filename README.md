# Attempt at simulation of an extracted netlist

Aim is to measure maximum current of the circuit during one clock cycle.

* Used magic to extract wrapped_seven_segment.spice
* include skywater libs and wrapped_seven_segment.spice
* hold active low
* use pulse to make a single clock 
* try to plot current

# Questions

* Can I just leave all the subckt nodes unconnected? I am only interested in VGND, VPWR, wb_clk_i and active. 
* I'm getting a warning about vactive being a singular matrix, but I can't work out why. Something to do with subckt nodes?
* Don't know why spice is complaining about valid modelnames, as the sky130 lib is included

# Current issues

    warning, can't find model sky130_fd_pr__res_generic_po

many errors like this:

    Error on line 0 :
      m.xtest.xfiller_94_361.x0.msky130_fd_pr__pfet_01v8_hvt vpwr vgnd vpwr vpwr xtest.xfiller_94_361.x0:sky130_fd_pr__pfet_01v8_hvt__model l=    4.72999999999999954e+00   w=    8.69999999999999996e-01   ad=    0.00000000000000000e+00   as=    0.000000000000
      00000e+00   pd=    0.00000000000000000e+00   ps=    0.00000000000000000e+00   nrd=    0.00000000000000000e+00   nrs=    0.00000000000000000e+00   sa=    0.00000000000000000e+00   sb=    0.00000000000000000e+00   sd=    0.00000000000000000e+00   nf=    1.
      00000000000000000e+00
      could not find a valid modelname

Followed by these:

    Warning: include: has no value, DC 0 assumed                                                                                                                                                                                                                  
    Warning: r.xtest.x_1270_.r1: resistance to low, set to 1 mOhm
    Warning: r.xtest.x_1270_.r0: resistance to low, set to 1 mOhm
    Warning: vclk: no DC value, transient time 0 value used
    Warning: singular matrix:  check nodes vactive#branch and vactive#branch

    doAnalyses: iteration limit reached

    run simulation(s) aborted
    Error: no such vector i(vdd)
