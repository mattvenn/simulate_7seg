module_inputs = {
    'io_in'     : 38,
    'la_data_in': 32,
    'wb_clk_i'  : 1,
    'wb_rst_i'  : 1,
    'wb_adr_i'  : 32,
    'wb_dat_i'  : 32,
    'wb_sel_i'  : 4,
    'wb_we_i'   : 1,
    }

for name, number in module_inputs.items():
    nodename = 'v' + name
    if number == 1:
        print("%s %s 0 0" % (nodename, name))
    else:
        for i in range(number):
            print("%s[%d] %s[%d] 0 0" % (nodename, i, name, i))
