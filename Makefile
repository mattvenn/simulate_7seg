all: sim

inputs.spice:
	python3 gen_inputs.py > inputs.spice

sim: inputs.spice simulation.spice
	# run the simulation
	ngspice simulation.spice

phony: clean
