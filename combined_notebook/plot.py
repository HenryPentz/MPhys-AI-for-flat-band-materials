import json
import sys
import os
from pathlib import Path
import matplotlib.pyplot as plt
import warnings

from pymatgen.electronic_structure.bandstructure import BandStructureSymmLine
from pymatgen.electronic_structure.dos import CompleteDos
from pymatgen.electronic_structure.plotter import BSDOSPlotter

def plot(material_id, data_directory, e_bounds=[-4, 4]):

    # get bands data
    filename_bands = data_directory+f"/bands/{material_id}.json"
    if not os.path.isfile(filename_bands):
        raise FileNotFoundError("No such file %s" % filename_bands)
        
    bands_dict=json.load(open(filename_bands))
    bands=BandStructureSymmLine.from_dict(bands_dict)

    # create plotter object
    bsp=BSDOSPlotter(vb_energy_range=-e_bounds[0], cb_energy_range=e_bounds[1], fixed_cb_energy=True, font="DejaVu Sans")

    filename_dos = data_directory+f"/dos/{material_id}.json"
    if os.path.isfile(filename_dos):
        dos_dict=json.load(open(filename_dos))
        dos=CompleteDos.from_dict(dos_dict)
        ax = bsp.get_plot(bands, dos=dos)
    else:
        ax = bsp.get_plot(bands)  
    plt.show()

def bare_plot(material_id, data_directory, plot_dos=False, e_bounds=[-4, 4]):
    # get bands data
    filename_bands = data_directory+f"/bands/{material_id}.json"
    if not os.path.isfile(filename_bands):
        raise FileNotFoundError("No such file %s" % filename_bands)
        
    bands_dict=json.load(open(filename_bands))
    bands=BandStructureSymmLine.from_dict(bands_dict)

    # create plotter object
    bsp=BSDOSPlotter(vb_energy_range=-e_bounds[0], cb_energy_range=e_bounds[1], fixed_cb_energy=True, font="DejaVu Sans", axis_fontsize=0, tick_fontsize=0, legend_fontsize=0, bs_legend=None, rgb_legend=False, fig_size=(8, 8))

    filename_dos = data_directory+f"/dos/{material_id}.json"
    if os.path.isfile(filename_dos) and plot_dos:
        dos_dict=json.load(open(filename_dos))
        dos=CompleteDos.from_dict(dos_dict)
        ax = bsp.get_plot(bands, dos=dos)

        for axi in ax:
            axi.spines['left'].set_visible(False)
            axi.spines['bottom'].set_visible(False)
            axi.spines['right'].set_visible(False)
            axi.spines['top'].set_visible(False)
            axi.tick_params(left=False, bottom=False)
            
        plt.subplots_adjust(wspace=None, hspace=None)
        
    else:
        ax = bsp.get_plot(bands)  

        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.tick_params(left=False, bottom=False)
    
    plt.subplots_adjust(left=-0.001, right=1, top=1+0.001, bottom=0)
    plt.savefig('out.png', bbox_inches=0, pad_inches=0)

    
