import json
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import warnings

from pymatgen.electronic_structure.bandstructure import BandStructureSymmLine
from pymatgen.electronic_structure.dos import CompleteDos
from pymatgen.electronic_structure.plotter import BSDOSPlotter

def plot(material_id, data_directory):

    # get bands data
    filename_bands = data_directory+f"/bands/{material_id}.json"
    if not os.path.isfile(filename_bands):
        raise FileNotFoundError("No such file %s" % filename_bands)
        
    bands_dict=json.load(open(filename_bands))
    bands=BandStructureSymmLine.from_dict(bands_dict)

    # create plotter object
    bsp=BSDOSPlotter(font="DejaVu Sans")

    filename_dos = data_directory+f"/dos/{material_id}.json"
    if os.path.isfile(filename_dos):
        dos_dict=json.load(open(filename_dos))
        dos=CompleteDos.from_dict(dos_dict)
        ax = bsp.get_plot(bands, dos=dos)
    else:
        ax = bsp.get_plot(bands)  
    plt.show()