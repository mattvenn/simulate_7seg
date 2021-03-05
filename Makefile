all: sim

sim: simulation.spice
	# run the simulation
	ngspice $^

phony: clean
