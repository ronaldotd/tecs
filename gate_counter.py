import os
import os.path

nand_dff_count = {}

def get_hdl_files():
    hdl_files = {}
    for dirname, _, filenames in os.walk('.'):
        for filename in filenames:
            chip, ext = os.path.splitext(filename)
            if ext == '.hdl':
                hdl_files[chip] = os.path.join(dirname, filename)
    return hdl_files

def parse_chip(chip_name, hdl_files):
    f = open(hdl_files[chip_name])
    in_parts = False
    subchips = []
    for line in f.readlines():
        line = line.strip()
        if 'PARTS' in line:
            in_parts = True
            continue
        if in_parts:
            idx = line.find('(')
            if idx != -1:
                chip = line[:idx]
                subchips.append(chip)
    f.close()

    return subchips

def count_gates_in_chip(chip_name, hdl_files):
    if chip_name == 'Nand':
        return (1, 0)
    if chip_name == 'DFF':
        return (0, 1)

    nand_total = 0
    dff_total = 0

    for subchip in parse_chip(chip_name, hdl_files):
        if subchip in nand_dff_count:
            nand, dff = nand_dff_count[subchip]
        else:
            nand, dff = count_gates_in_chip(subchip, hdl_files)
            nand_dff_count[subchip] = (nand, dff)

        nand_total += nand
        dff_total += dff

    return (nand_total, dff_total)


if __name__ == '__main__':
    hdl_files = get_hdl_files()
    for chip in hdl_files:
        nand, dff = count_gates_in_chip(chip, hdl_files)
        print(f'{chip}\t\t\t\t\t{nand}\t\t\t\t\t{dff}')

