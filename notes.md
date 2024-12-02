# Research and Meeting Notes

## Week of 12/2/2024
- Adding [1] and [17] Antennas together
  - [1] and [17] share X and Z coordinates but vary by Y
      - petal x ([1]):
         - ymin: -190.637 mm
         - ymax: -187.5 mm
      - petal x1 ([17]):
        - ymin: 187.5 mm
        - ymax: 190.637 mm
  - $d$ is 375 mm or .375 m (distance from x ymax to x1 ymin - should this be from the middle of the petals?)
 - Plots of Antenna Gain across Theta and Phi

![image](https://github.com/user-attachments/assets/b74c52bd-02cb-4ac1-90a0-07322be7a26f)
![image](https://github.com/user-attachments/assets/7684f479-37d0-4827-becd-22ffd15b2f6f)

## Week of 11/25/2024
- [Project Proposal Presentation](https://github.com/user-attachments/files/17981823/Connolly_December_Presentation.pdf)
- Code from Keith (for plotting with HealPy/HealPix)
```
import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import pandas as pd

# Load data from the text file
filename = r'farfield (f=0.3) [1].txt'

data = pd.read_fwf(filename, skiprows=2, colspecs=[(0, 10), (12, 22), (34, 46)], 
                      names=['theta', 'phi', 'gain'])

data['theta'] = np.radians(data['theta'])
data['phi'] = np.radians(data['phi'])

nside=32
npix = hp.nside2npix(nside)
hpmap = np.zeros(npix)

pidx = hp.ang2pix(nside, data['theta'], data['phi'])
hpmap[pidx]=data['gain']

hp.mollview(hpmap)
```
- Meeting 11/26
![20241126_105015](https://github.com/user-attachments/assets/b9524237-5ae4-4ae1-be68-976a7fcd285f)
