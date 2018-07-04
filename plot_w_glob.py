## Auto Multi-plots for sequential files in a directory
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

filenames = sorted(glob.glob('C:/Users/Owner/heliopy/data/helios/E1_experiment/New_proton_corefit_data_2017/ascii/helios2/1976/*.csv', recursive=True))
filenames = filenames[0:1] # choose number of filenames you want
for f in filenames:
    print(f)
    data = pd.read_csv(f)
    print(data.keys())

    fig, axs = plt.subplots(3, 1, sharex=True)
    axs[0].plot(data['n_p'])
    axs[1].plot(data['vp_x'])
    axs[1].plot(data['vp_y'])
    axs[1].plot(data['vp_z'])
    axs[2].plot(data['Tp_perp'])
    axs[2].plot(data['Tp_par'])
    
    for ax in axs:
        ax.legend()
        fig.tight_layout()
    plt.show()
