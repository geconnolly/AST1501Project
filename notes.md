# Research and Meeting Notes

## Week of 12/3/2024

- Plots
  - [1] and [17] Plots - Gain (Linear) and Amplitude

![download](https://github.com/user-attachments/assets/5f222d05-d28e-4f37-98d9-07e40dfc6284)
![download](https://github.com/user-attachments/assets/63584d4d-3c81-42fe-a5a4-af05aaba5017)
![download](https://github.com/user-attachments/assets/d386b441-3f66-4f74-81db-bf75405350fc)
![download](https://github.com/user-attachments/assets/fcc106eb-bf6a-4ae2-bb14-852e878aeab3)

  - $D_{1+17} = |A_1 + A_{17}|^2$

![download](https://github.com/user-attachments/assets/f056e51e-3757-4f6f-91d6-65d989fd208c)

  - $\sqrt{D_{1+17}}$

![download](https://github.com/user-attachments/assets/00503dd3-e49b-4139-b16d-96550c8f854f)


- dBi
  - $Gain$ $= 10^{Gain(dBi)/10}$
  - $G_{dBi} = 10*log_{10}G$
  - $G = {P_{antenna}/P_{isotropic}}$
 
- Converting to Linear
  - Convert dBi to Linear (unitless?)
  - Abs(Phi)[dBi] + Abs(Theta)[dBi] should = Abs(Dir.)[dBi] when converted to linear
    - True, ±.00004
   
- Equations
  - $A_i = \sqrt{D_i} * e^{j(\Phi + \Phi_i)}$
  - where $D_i = |A_i|^2$ and $D_{i+j} = |A_i + A_j|^2$
    - ~~D_i holds true for A_1 and A_{17} but not D_{tot}~~
    - ~~D_1 + D_{17} = |A_1|^2 + |A_{17}|^2~~
    - $D_{tot} \neq D_i + D_j$ !!!
  - $D_i = R(A_i)^2 + I(A_i)^2$
    - Holds true for data
  - $D \propto |A|^2 \propto |E|^2$
- Meeting Notes

![20241203_115130](https://github.com/user-attachments/assets/10fce7d9-d7e5-4eed-88bf-ffe25418b3b8)

## Week of 11/26/2024
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

- Equations

$Ae^{i(\phi + 2\pi*{dsin(\theta)/\lambda})}$

- Phase Shift Plots
  - Phase Shift determined by above equation ($2\pi*{dsin(\theta)/\lambda}$) added to $\phi$ value
  - Combined plot is the average of theta, phase + phi, and gain values

![image](https://github.com/user-attachments/assets/c1fface0-8d20-4d56-9fdc-99c87b1bb477)
![image](https://github.com/user-attachments/assets/b78733d6-0229-4b17-be7c-c3d861b09ccc)
![image](https://github.com/user-attachments/assets/c4486d5c-0273-423d-9f8c-aa95833e1927)

- Export from CST
  - Theta [deg]
  - Phi [deg]
  - Abs(Dir.) [dBi] or Gain
  - Abs(Theta)[dBi]
  - Phase(Theta)[deg]
  - Abs(Phi)[dBi]
  - Phase(Phi)[deg]
  - Ax.Ratio[dB]

- [Directivity vs. Gain](https://space.mit.edu/RADIO/CST_online/mergedProjects/3D/special_postpr/special_postpr_pp_farfield.htm)
  - The directivity of an antenna is defined as "the ratio of the radiation intensity in a given direction from the antenna to the radiation intensity averaged over all directions." The averaged radiation intensity is given by the total power radiated by the antenna divided by 4π
  - Accordingly, the gain is defined similarly but is related to the accepted power of the structure. In the case of a loss-free antenna (no conduction or dielectric losses), the gain is equal to the directivity. Note, that power flowing out any port is not considered as accepted by the structure.
- Circular-Directional Polarization/Ludwig 3

## Week of 11/19/2024
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
