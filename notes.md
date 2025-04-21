# Research and Meeting Notes

## Week of 4/14/2025

- Weighting
  - Want to weight larger signals over smaller signals: $1/\sigma^2$ bigger for larger signals
  - $N$ vs $N^2$
    - noise: signal/feeds?
    - signal goes up as $N^2$ _in power space_
    - amplitude of noise signal: $\sqrt{N}$
    - power of noise signal: N
  - sum vs. weighted average
    - weighted average of signal vs weighted average of noise

## Week of 4/8/2025

[Final Presentation](https://github.com/user-attachments/files/19742252/Final_Presentation.pdf)

- Weighting
  - Weighting by $D$ value at the center for individual feeds and stacks
  - Value at the center for stacks 5 and 13 are 2-3 orders of magnitude smaller than every other value (~0.0002)
    - Feeds that are facing the sides
  - Stack 9 also has a low value (~0.02)
    - Feeds that are facing the back
   
- Center of each stack
![image](https://github.com/user-attachments/assets/e2f5b83a-ba73-4601-bcc6-ad08e6a2fb7d)

|Max Power|
|---------|
|1.7634585028393124|

|Stack|Power @ Center|
|-----|--------------|
|1|1.6244255282867|
|2|1.7510090560518297|
|3|1.2117650527715131|
|4|1.2867771018268348|
|5|0.0002405889919858276|
|6|1.1571023623380903|
|7|0.44393454172140956|
|8|0.2952031820062026|
|9|0.022715434731680324|
|10|0.2950526979019993|
|11|0.4414369425565773|
|12|1.1548902387809774|
|13|0.00023947266405845128|
|14|1.283919437290192|
|15|1.2084406178216345|
|16|1.7489155792290854|

<!--
|Stack|Power @ Center|
|-----|--------------|
|1|1.241665687194915|
||2.5200717255543155|
||2.5763462842407963|
||1.2622018869706109|
|2|1.3971093746435994|
||2.4574126635070943|
||2.4981780691827504|
||1.4051968422758039|
|3|1.0725105691602503|
||1.4193521645991332|
||1.433075474715111|
||1.0581050042646591|
-->

## Week of 4/1/2025

- Asymmetry/Map Popilation
  - For each pixel, added amplitude values at given pixel, then divided by total number of amplitude values (bin value)
  - Seems to have solved asymmetry issue, but multiple stacks (past 7) are still acting strange
    - 9 Stacks includes the feeds pointing to the sides, the power doesn't increase but the total number of stacks (N) increases
 
![image](https://github.com/user-attachments/assets/609b4159-7e40-4834-8361-8cd0dff6bbf6)

- CHIME/CHORD RFI Working Group Meeting
  - [Slides](https://docs.google.com/presentation/d/1T9Rd0A4GXHd8M42H4B1pBUGZf7E3zPQJkcgTgTHk4Nk/edit?usp=sharing)

## Week of 3/25/2025

- Map Popultation
  - $A_1$ and $A_2$ are made from $\alpha$ from the CST data
    - shape of 259920
  - `pidx` is made from $\theta$ and $\phi$ values from CST data
    - also shape of 259920
  - `pidx` looks like: [0, 0, 4, 12, 12, ...]
    - means that the value in the pixel is the last inputed value

- Asymmetry
  - Subtract mirror image - if symmetric, should see no difference
  - Is CST symmetric? HealPix _should_ be
 
- Normalize Beam
  - Normalize by sum of D (max value 1)

## Week of 3/18/2025

[Final Report](https://www.overleaf.com/read/krfcgrgzzqms#2f924e)

- Weighted Sum
  - Needed to divide the sum by the total number of stacks
  - `return_value = np.abs(sum_A)**2/len(stacks)`
 
- Variance on bore sight
  - Weight the bigger values more - weighted to the pixel value at the center
  - Goal is to maximize $\frac{D}{\sqrt{T_{sys}}}$

## Week of 3/11/2025

- Signal to Noise Ratio
  - Need to weight everything by the variance
  - $\frac{\sum_i y_i/\sigma_i^2}{\sum_i (1/\sigma^2)}$
  - What, physically, is $\sigma^2$? D value on boresight?
 
- Phase Shifting
  - `np.arctan2` gives phase from $-\pi$ to $\pi$
    - given $arg(a + bi)$ then $\phi = arctan(\frac{b}{a})$
  - Need to "unwrap"?
  - Need to get rid of the interference from phase
  - $Stack Total = e^{-i\phi_1}stack_1 + e^{-i\phi_2}stack_2 + ...$

## Week of 3/4/2025

- Signal to Noise Ratio
  - Scale Signal by inverse variance $1/\\sigma^2$
  - Used `np.std` for $\\sigma$
  - Shape does not change, but power increases dramatically

![image](https://github.com/user-attachments/assets/3284c0e4-c9b5-4949-a2b4-184f65c2292b)
![image](https://github.com/user-attachments/assets/6dbceef8-7803-480f-8713-257c3934ebf2)

- Phase Shift

## Week of 2/25/2025

- Plots: Original, Rotated, Combined

![download](https://github.com/user-attachments/assets/650ff9b6-ee2c-42fe-bd4a-b08af9391866)
![download](https://github.com/user-attachments/assets/986829f4-31b7-47c0-9f34-8a3bf557441c)
![download](https://github.com/user-attachments/assets/ede1834b-c34e-4fee-9dcd-7a82e2b8ce37)

- Plot Naming Conventions
  - Naming each stack of four feeds after the bottom-most feed in CST Model

![image](https://github.com/user-attachments/assets/4d46e6e6-f37c-41d8-be16-72debbb4630c)

- Plots: Original, 22.5 rot, 45 rot, All Feeds Combined

![download](https://github.com/user-attachments/assets/5fc00d70-956e-4b99-9963-4ca7588354a7)
![download](https://github.com/user-attachments/assets/8acd57b9-fae1-4ac7-b36b-78658b97c8e3)
![download](https://github.com/user-attachments/assets/b357ed62-8f6f-4234-b7bf-5e130ebfecc0)
![download](https://github.com/user-attachments/assets/e30bea32-140a-4ad1-8a03-5d4e5bbf7143)

- Power vs Degree Plots
  - Drop off in Power for 7 Stacks and beyond

![download](https://github.com/user-attachments/assets/050f5a76-d153-4907-9f3f-b9a68ee721a5)
![download](https://github.com/user-attachments/assets/1091e8b0-d63f-4916-877e-2b2af041da2a)

- Rotating Stacks Code
```
def plot_rotated_stacks(filename1, filename2, stacks):
    '''
    Parameters:
    ==========
    filename1, filename 2: strings
        recursive strings of imported files of individual feeds 
    stacks: int or list of ints
        stack numbers 1 - 16 (# of bottom most feed of stack)
    
    Returns:
    =======
    map: aray of floats
        array of power values for selected stacks at HealPy pixel values
    '''

    # importing files 
    
    data1 = pd.read_fwf(filename1, skiprows=2, 
                    colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135), (135, 145)], 
                    names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data1['theta'] = np.radians(data1['theta'])
    data1['phi'] = np.radians(data1['phi'])
    data1['alpha'] = np.radians(data1['alpha'])
    data1['beta'] = np.radians(data1['beta'])

    data2 = pd.read_fwf(filename2, skiprows=2,
                    colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135), (135, 145)], 
                    names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data2['theta'] = np.radians(data2['theta'])
    data2['phi'] = np.radians(data2['phi'])
    data2['alpha'] = np.radians(data2['alpha'])
    data2['beta'] = np.radians(data2['beta'])
    
    # plot
    
    nside=64
    npix = hp.nside2npix(nside)
    hpmap = np.zeros(npix)
    
    hpmap_A_1 = np.zeros(npix, dtype=complex)
    hpmap_A_2 = np.zeros(npix, dtype=complex)
    hpmap_A_3 = np.zeros(npix, dtype=complex)
    hpmap_A_4 = np.zeros(npix, dtype=complex)
    
    pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
    
    pidx_flip = hp.ang2pix(nside, data1['theta'], -data1['phi'])
        
    # equations
        
    G_1 = 10**(data1['abs(theta)']/10)
    A_1 = np.sqrt(G_1)*np.exp(1j*(data1['alpha']))

    G_2 = 10**(data2['abs(theta)']/10)
    A_2 = np.sqrt(G_2)*np.exp(1j*(data2['alpha']))
    
    D_tot = np.abs(A_1+A_2)**2
    
    # flip
    
    hpmap_A_1[pidx] = A_1
    hpmap_A_2[pidx] = A_2
    hpmap_A_3[pidx_flip] = A_2
    hpmap_A_4[pidx_flip] = A_1
    
    # rotation
    
    stack_rotations = np.arange(0, 360, 22.5)
    
    sum_A = 0
    
    for stack in stacks:
        
        rot = hp.rotator.Rotator(rot=(0, stack_rotations[stack-1], 90))
        
        rot_A_1 = rot.rotate_map_pixel(hpmap_A_1)
        rot_A_2 = rot.rotate_map_pixel(hpmap_A_2)
        rot_A_3 = rot.rotate_map_pixel(hpmap_A_3)
        rot_A_4 = rot.rotate_map_pixel(hpmap_A_4)
        
        sum_A += rot_A_1 + rot_A_2 + rot_A_3 + rot_A_4
    
    return np.abs(sum_A)**2
```

## Week of 2/18/2025

- Adding Plots
  - $\ D_{tot} = |A_1 + A_2 + A_1 ' + A_2 '|^2$
  - However, the flip happens with the `hpmap`, not when solving the $A$ values
 
```
def plot_four_feeds(filename1, filename2):

    # importing files 
    
    data1 = pd.read_fwf(filename1, skiprows=2, colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135),
                                                  (135, 145)], 
                      names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data1['theta'] = np.radians(data1['theta'])
    data1['phi'] = np.radians(data1['phi'])
    data1['alpha'] = np.radians(data1['alpha'])
    data1['beta'] = np.radians(data1['beta'])

    data2 = pd.read_fwf(filename2, skiprows=2, colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135),
                                                  (135, 145)], 
                      names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data2['theta'] = np.radians(data2['theta'])
    data2['phi'] = np.radians(data2['phi'])
    data2['alpha'] = np.radians(data2['alpha'])
    data2['beta'] = np.radians(data2['beta'])
    
    # plot
    
    nside=64
    npix = hp.nside2npix(nside)
    hpmap = np.zeros(npix)
    
    hpmap_A_1 = np.zeros(npix, dtype=complex)
    hpmap_A_2 = np.zeros(npix, dtype=complex)
    hpmap_A_3 = np.zeros(npix, dtype=complex)
    hpmap_A_4 = np.zeros(npix, dtype=complex)
    
    pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
    
    pidx_flip = hp.ang2pix(nside, data1['theta'], -data1['phi'])
        
    # equations
        
    G_1 = 10**(data1['abs(theta)']/10)
    A_1 = np.sqrt(G_1)*np.exp(1j*(data1['alpha']))

    G_2 = 10**(data2['abs(theta)']/10)
    A_2 = np.sqrt(G_2)*np.exp(1j*(data2['alpha']))
    
    D_tot = np.abs(A_1+A_2)**2
    
    hpmap_A_1[pidx] = A_1
    hpmap_A_2[pidx] = A_2
    hpmap_A_3[pidx_flip] = A_2
    hpmap_A_4[pidx_flip] = A_1
    
    return np.abs(hpmap_A_1 + hpmap_A_2 + hpmap_A_3 + hpmap_A_4)**2
```

- Plots

![download](https://github.com/user-attachments/assets/5945540a-9ce4-4f23-a290-372caf485360)
<!---![download](https://github.com/user-attachments/assets/ef93f91c-dbd2-4f91-bbf2-d74480d9a743)--->

- Comparing Different Antenna Combination Plots

![download](https://github.com/user-attachments/assets/ad79e861-425c-4fcc-9654-0cf690b7aa5f)
![download](https://github.com/user-attachments/assets/e1541779-96ad-476a-b032-b999dce9c262)
![download](https://github.com/user-attachments/assets/c3dad89d-4315-49e8-ae30-af337bfd5878)
![download](https://github.com/user-attachments/assets/3ce5bf33-e5f0-46d0-92b4-79ec79a4f63a)
![download](https://github.com/user-attachments/assets/f957f06b-89b9-478e-b0c5-0f1fd47df9db)
![download](https://github.com/user-attachments/assets/e361caa4-0956-4dee-8207-c079e3e251fa)
![download](https://github.com/user-attachments/assets/c4ebb622-8882-4e32-ba5c-3d4b60d7dda7)
![download](https://github.com/user-attachments/assets/5d50bde3-b2af-4c6f-8a90-991a5f887843)

## Week of 2/11/2025

- Understanding `hp.rot` Plots
  - Mollview maps for un-rotated and rotated combined feeds and plots of long and lat values
  - Compare rotated and un-rotated values and found they are the same
  - Mollview may be distorting maps visually, but not quantitatively
  
![Rotation_Plots](https://github.com/user-attachments/assets/a21a8573-21f2-43fa-a3ec-60083783b030)

![download](https://github.com/user-attachments/assets/4aab330b-bd52-453e-b9f3-d46a0d2be21f)
![download](https://github.com/user-attachments/assets/2937ed00-f029-4045-8317-fe037c0944b4)
![download](https://github.com/user-attachments/assets/afde2031-fd2c-4a43-a332-8a82e6aa0a1f)
![download](https://github.com/user-attachments/assets/a11367d9-2cee-4310-a9e5-be77caa9539e)

## Week of 1/28/2025 - 2/4/2025

- [January Update Slides](https://github.com/user-attachments/files/18648211/January_Update.pdf)

- Un-Rotated Plots (w/o phase shift)

![download](https://github.com/user-attachments/assets/4a56bc24-df7c-42ef-a3e7-92449c6cb74a)
![download](https://github.com/user-attachments/assets/0e67373b-b048-4d57-945d-d09e47c7a606)
![download](https://github.com/user-attachments/assets/f86d58bf-c185-49d1-9b26-e6fa2afce72a)

- Rotated Plots (w/o phase shift)

![download](https://github.com/user-attachments/assets/153c2868-34db-480e-9705-d3f1f9b901be)
![download](https://github.com/user-attachments/assets/e9d5e7e7-cbcc-4df6-8cec-c2f280639176)
![download](https://github.com/user-attachments/assets/ae34abff-bb3d-4feb-ba28-1baa223f494c)

<!--
- Un-Rotated Plots (w/ phase shift)

![download](https://github.com/user-attachments/assets/aa7d790e-785e-4da8-8a99-f013ea218017)
![download](https://github.com/user-attachments/assets/7b8c7356-6d30-4bc8-9b01-42428c93df6e)
![download](https://github.com/user-attachments/assets/e5c87fce-b348-484c-ba2a-e28ccde7ff22)

- Rotated Plots (w/ phase shift)

![download](https://github.com/user-attachments/assets/03432ddd-c72e-415a-b29a-c3b2bad23e27)
![download](https://github.com/user-attachments/assets/e022519e-200f-4640-bd79-69f6d5eb17da)
![download](https://github.com/user-attachments/assets/3e7a9982-532c-41e6-9ff4-8b06a891cad3)
-->
- Issues with Coordinate System (Again)
  - only use file coordinates (theta, phi) to set `pidx`, never reference after
  - use (long, lat) instead, references healpy coordinates (`long, lat = hp.pix2ang(nside, pidx)`)
 
![image](https://github.com/user-attachments/assets/5163021d-9ed6-4d04-b27c-67af5ccc2f6e)

## Week of 1/21/2025

<!--
- Correct(?) Plots

![download](https://github.com/user-attachments/assets/5b48d1e7-aa64-4e04-9f5e-3e03c4d5ed63)
![download](https://github.com/user-attachments/assets/2a2a0b2d-e842-40db-ad33-96472150b086)
![download](https://github.com/user-attachments/assets/ab854861-eb2e-4e5f-bb88-04bc76ff38d7)
-->

- Plotting Function (returns an `hpmap`)
```
import numpy as np
import healpy as hp
import pandas as pd

def plot_two_feeds(filename1, filename2, flip = False):
    '''
    inputs:
    ========
    filename1, filename 2: recursive strings of imported files of individual feeds 
    flip: set to False, True is used when plotting the flip of two feeds
    
    returns:
    ========
    rot_hpmap: hpmap of two feeds, to go into hp.mollview for a plot
    '''
    
    # importing files 
    
    data1 = pd.read_fwf(filename1, skiprows=2, colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135),
                                                  (135, 145)], 
                      names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data1['theta'] = np.radians(data1['theta'])
    data1['phi'] = np.radians(data1['phi'])
    data1['alpha'] = np.radians(data1['alpha'])
    data1['beta'] = np.radians(data1['beta'])

    data2 = pd.read_fwf(filename2, skiprows=2, colspecs=[(0, 10), (12, 22), (34, 46), (50, 66), (70, 86), (90, 110), (118, 135),
                                                  (135, 145)], 
                      names=['theta', 'phi', 'gain', 'abs(theta)', 'alpha', 'abs(phi)', 'beta', 'ratio'])
    data2['theta'] = np.radians(data2['theta'])
    data2['phi'] = np.radians(data2['phi'])
    data2['alpha'] = np.radians(data2['alpha'])
    data2['beta'] = np.radians(data2['beta'])
    
    # equations
    
    G_1 = 10**(data1['abs(theta)']/10)
    A_1 = np.sqrt(G_1)*np.exp(1j*data1['alpha'])
    
    G_2 = 10**(data2['abs(theta)']/10)
    A_2 = np.sqrt(G_2)*np.exp(1j*(data2['alpha'] + 2*np.pi*.325*np.sin(data2['phi'])))
    
    A_tot = A_1 + A_2
    D_tot = np.abs(A_tot)**2
    
    # plot
    
    nside=64
    npix = hp.nside2npix(nside)
    hpmap = np.zeros(npix)

    if flip == False:
        pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
        
    else: #flip == True
        pidx = hp.ang2pix(nside, data1['theta'], -data1['phi'])
        
    hpmap[pidx]=(D_tot)

    rot = hp.rotator.Rotator(rot=(0,0,90))
    orig_hpmap = hpmap
    rot_hpmap = rot.rotate_map_pixel(orig_hpmap)

    return rot_hpmap
```

- Meeting Notes

![20250121_105555](https://github.com/user-attachments/assets/dc611452-500c-467c-b485-bd5e37b86e93)

## Week of 1/14/2025

- Flipping Feeds
  - [1]' and [17]' plot should be the mirror of [1] and [17]
  - distance between [1] and [17]: .375 m
  - distance between [1] and [1]': 1.125 m (greater than wavelength)
  - instead of `np.pi-theta` use `-phi` (which is the same as `np.pi-theta` and `rot = (0,0,270)`)

- New Plots

![download](https://github.com/user-attachments/assets/5ed98000-8fd5-4d8f-a3df-a529fdb67e4a)
![download](https://github.com/user-attachments/assets/88b5e4cc-cbc0-4b83-9105-c30c9cc86eed)
![download](https://github.com/user-attachments/assets/3b095283-1083-4de9-800c-6394a67c89f3)

- Current Results Plots (incorrect)

![download](https://github.com/user-attachments/assets/0122d178-0300-4bdf-9429-0826e1831dc5)
![download](https://github.com/user-attachments/assets/7e0b6022-3acb-472d-84df-1a761a662ddb)
![download](https://github.com/user-attachments/assets/aab34f6f-3588-4bf3-b46b-17245e0e2783)

## Week of 1/7/2025

- "Mirroring" for flipping feeds
  - theta to -theta in ang2pix does not work (-theta out of bounds [0, $\pi$])
  - np.pi - theta instead

![image](https://github.com/user-attachments/assets/f3cd0187-a301-4e60-8c3b-2f7e15c05386)

![image](https://github.com/user-attachments/assets/84c048dd-adbc-4adc-aed0-cb26961b6e1a)

 <!--
![image](https://github.com/user-attachments/assets/2ae4df77-e025-4156-b61d-d4ff531faca9)

```
#original
G_1 = 10**(data['abs(theta)']/10)
A_1 = np.sqrt(G_1)*np.exp(1j*(data['alpha']))

#mirrored
G_1prime = 10**(data['abs(theta)']/10) #wouldn't change 
A_1prime = np.sqrt(G_1prime)*np.exp(1j*(-data['alpha'])) #negative alpha
...
A_tot = A_1 + A_1 prime + ...
```
  - sanity check: do [1] and [17] plot match [1]' and [17]'?: YES

![download](https://github.com/user-attachments/assets/8d6d0198-76e2-401a-9bcc-69fc9acc0e9c)
![download](https://github.com/user-attachments/assets/2615c03c-7021-447b-99b5-ede433b86ea1)

  - see peaks and nodes we would expect (all four feeds are larger than 1 m - the wavelength at .3 GHz)

![download](https://github.com/user-attachments/assets/2d239514-4067-4329-af7d-3f9ac5d315ed)
-->

- Meeting Notes
  - Renaming `Phase[theta]` to $\alpha$ and `Phase[phi]` to $\beta$
  - `flip='astro'` is fine (default) - "gods eye view"

- Rotator Code
  - Why are we rotating: easier to view plots with respect to feeds
  - rot = (a,b,c): euler angles
  - Third Euler angle is around the center of the map
  - takes `orig_hpmap` and outputs rotated version  `rot_hpmap`
```
import healpy as hp
rot = hp.rotator.Rotator(rot=(0,0,90))
rot_hpmap = rot.rotate_map_pixel(orig_hpmap)
hp.mollview(orig_hpmap)
hp.mollview(rot_hpmap)
```
![download](https://github.com/user-attachments/assets/c134005d-f864-418e-b373-9556d4e80503)
![download](https://github.com/user-attachments/assets/6319fbd6-ae6b-4d1a-ae20-54dfaa797d47)
![download](https://github.com/user-attachments/assets/874ce438-c54c-40f8-8b1a-4d8ec5f9ec4a)
![download](https://github.com/user-attachments/assets/167f0157-a2d8-48fb-a500-250c27611097)

- Updated Plot Code
```
#healpy map set up
nside=64
npix = hp.nside2npix(nside)
hpmap = np.zeros(npix)

#map with pixels matching theta and phi angles from data
pidx = hp.ang2pix(nside, data['theta'], data['phi'])

#linearizing gain - data is given in dBi
linear_gain = 10**(data['gain']/10)

#creating map with gain data
hpmap[pidx]=np.sqrt(linear_gain)

#rotating map around the center
rot = hp.rotator.Rotator(rot=(0,0,90))
orig_hpmap = hpmap
rot_hpmap = rot.rotate_map_pixel(orig_hpmap)

hp.mollview(rot_hpmap, unit =r'Amplitude', title="0.3 GHz: [1]")

```
![download](https://github.com/user-attachments/assets/a890d521-9167-4989-a236-ac3077f11ba6)
![download](https://github.com/user-attachments/assets/ee440f3b-ac5d-4cc3-ba88-2dd7d22ff43c)

- "Adding" Together [1] and [17] in phase
  - Phase[theta] used instead of Phase[phi] because Abs[theta] is greater than Abs[phi]
```
# equations
G_1 = 10**(data['abs(theta)']/10)
A_1 = np.sqrt(G_1)*np.exp(1j*(data['phase(theta)']))

G_17 = 10**(data1['abs(theta)']/10)
A_17 = np.sqrt(G_17)*np.exp(1j*(data1['phase(theta)']))

A_tot = A_1 + A_17
D_tot = np.abs(A_tot)**2

# plot
nside=64
npix = hp.nside2npix(nside)
hpmap = np.zeros(npix)

pidx = hp.ang2pix(nside, data['theta'], data['phi'])
hpmap[pidx]=(D_tot)

rot = hp.rotator.Rotator(rot=(0,0,90))
orig_hpmap = hpmap
rot_hpmap = rot.rotate_map_pixel(orig_hpmap)

hp.mollview(rot_hpmap, unit ="Amplitude", title="0.3 GHz: [1] & [17]")
```
![download](https://github.com/user-attachments/assets/6e2d21f5-e240-4ed5-b868-e15b9aac09e0)

- `flip` in `hp.mollview`
  - "Defines the convention of projection : ‘astro’ (default, east towards left, west towards right) or ‘geo’ (east towards right, west towards left)"
 
- Phase Plots

![download](https://github.com/user-attachments/assets/e54b2e6d-a1d1-402e-b248-f660b1664082)
![download](https://github.com/user-attachments/assets/bea0ee74-a6a1-4281-a6b9-b43a9bdeaaab)

## Week of 12/10/2024

- Worked on LitQual most of this week, not many updates
- Phase: Phi and Theta relative to polarization
  - One much bigger, means its alligned to the feed
- Coordinate System

![CoordinateSystems](https://github.com/user-attachments/assets/fc9a76d0-b9eb-45b6-8cc5-e1415ea9023c)
![image](https://github.com/user-attachments/assets/0f0b16f9-53f2-48d5-bcc5-96555dc9503a)

- Rotating Coordinates
  - [Rotating Tutorial](https://www.zonca.dev/posts/2021-03-11-rotate-maps-healpy)
  - "The definition of rotation in healpy is that the point provided in `rot` will be the center of the map."
  - `hp.Rotator`?
 
- Next Steps:
  - Figure out how to rotate coordinates
  - Look in Phase and Amplitude Space
  - Adding More Feeds
    - Mirror Flip: theta to -theta i.e., in ang2pix
    - Phi phase shift $dsin{\theta}$ don't care about x,y angle, only z angle $(cz/\nu)sin{\theta}$

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
