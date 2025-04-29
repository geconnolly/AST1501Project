def plot_one_feed(filename1, filename2, flip = False, nside_value=64):
    '''
    Parameters:
    ===========
    filename1, filename 2: string
        recursive strings of imported files of individual feeds 
    flip: boolean, default False
        set to False, True is used when plotting the flip or mirror of two feeds
    nside_value: int, optional
        HealPy resolution value, set to 64
    
    Returns:
    ========
    rot_hpmap1, rot_hpmap2: array of floats
        array of power values at HealPy pixel values for two individual feeds
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
    A_2 = np.sqrt(G_2)*np.exp(1j*data2['alpha'])
    
    # plotting info
    
    nside=nside_value
    npix = hp.nside2npix(nside)
    
    # flip
    
    if flip == False:
        pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
        
    else: #flip == True
        pidx = hp.ang2pix(nside, data1['theta'], -data1['phi'])
    
    # generating healpy maps
    
    i=0
    j=0
    
    sub_hpmap1 = np.zeros(npix, dtype=complex)
    sub_bin1 = np.zeros(npix)
    sub_hpmap2 = np.zeros(npix, dtype=complex)
    sub_bin2 = np.zeros(npix)

    for pixel in pidx:
        sub_hpmap1[pixel] += A_1[i]
        sub_bin1[pixel] += 1
        sub_hpmap2[pixel] += A_2[i]
        sub_bin2[pixel] += 1
        i += 1    

    hpmap1=np.abs(sub_hpmap1/sub_bin1)**2
    hpmap2=np.abs(sub_hpmap2/sub_bin2)**2

    # rotation
    
    rot = hp.rotator.Rotator(rot=(0,0,90))
    rot_hpmap1 = rot.rotate_map_pixel(hpmap1)
    rot_hpmap2 = rot.rotate_map_pixel(hpmap2)

    return rot_hpmap1, rot_hpmap2

def plot_two_feeds(filename1, filename2, flip = False, nside_value=64):
    '''
    Parameters:
    ===========
    filename1, filename 2: string
        recursive strings of imported files of individual feeds 
    flip: boolean, default False
        set to False, True is used when plotting the flip or mirror of two feeds
    nside_value: int, optional
        HealPy resolution value, set to 64
    
    Returns:
    ========
    rot_hpmap: array of floats
        array of power values for selected stacks at HealPy pixel values for combined feeds
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
    A_2 = np.sqrt(G_2)*np.exp(1j*data2['alpha'])
    
    # plotting info
    
    nside=nside_value
    npix = hp.nside2npix(nside)

    if flip == False:
        pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
        
    else: #flip == True
        pidx_flip = hp.ang2pix(nside, data1['theta'], -data1['phi'])
       
    # generating healpy maps
    
    i=0
    j=0
    
    sub_hpmap_A1 = np.zeros(npix, dtype=complex)
    sub_hpmap_A2 = np.zeros(npix, dtype=complex)
    
    sub_bin_A1 = np.zeros(npix)
    sub_bin_A2 = np.zeros(npix)
    
    if flip == False:
        for pixel in pidx:
            sub_hpmap_A1[pixel] += A_1[i]
            sub_hpmap_A2[pixel] += A_2[i]
            sub_bin_A1[pixel] += 1
            sub_bin_A2[pixel] += 1
            i += 1 
            
    else: # flip == True
        for pixel_flip in pidx_flip:
            sub_hpmap_A1[pixel_flip] += A_1[j]
            sub_hpmap_A2[pixel_flip] += A_2[j]
            sub_bin_A1[pixel_flip] += 1
            sub_bin_A2[pixel_flip] += 1
            j+=1
    
    hpmap = (np.abs(sub_hpmap_A1/sub_bin_A1 + sub_hpmap_A2/sub_bin_A2)**2)
    
    # rotation

    rot = hp.rotator.Rotator(rot=(0,0,90))
    orig_hpmap = hpmap
    rot_hpmap = rot.rotate_map_pixel(orig_hpmap)

    return rot_hpmap

def plot_rotated_stacks(filename1, filename2, stacks, SNR=False, nside_value=64):
    '''
    Parameters:
    ==========
    filename1, filename 2: strings
        recursive strings of imported files of individual feeds 
    stacks: list of ints
        stack numbers 1 - 16 (# of bottom most feed of stack)
    SNR: boolean, default False
        set to False, when True, uses inverse variance to weight signals given the power at the bore sight
    nside_value: int, optional
        HealPy resolution value, set to 64
    
    Returns:
    =======
    return_value: array of floats
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
    
    # plotting info
    
    nside=nside_value
    npix = hp.nside2npix(nside)

    pidx = hp.ang2pix(nside, data1['theta'], data1['phi'])
    
    pidx_flip = hp.ang2pix(nside, data1['theta'], -data1['phi'])
        
    # equations
        
    G_1 = 10**(data1['abs(theta)']/10)
    A_1 = np.sqrt(G_1)*np.exp(1j*(data1['alpha']))

    G_2 = 10**(data2['abs(theta)']/10)
    A_2 = np.sqrt(G_2)*np.exp(1j*(data2['alpha']))
    
    D_tot = np.abs(A_1+A_2)**2
    
    # center point in pixel values
    
    theta = np.radians(90)
    phi = np.radians(0)
    center = hp.ang2pix(nside, theta, phi)
    
    # generating healpy maps
    
    i=0
    j=0
    
    sub_hpmap_A1 = np.zeros(npix, dtype=complex)
    sub_hpmap_A2 = np.zeros(npix, dtype=complex)
    sub_hpmap_A3 = np.zeros(npix, dtype=complex)
    sub_hpmap_A4 = np.zeros(npix, dtype=complex)
    
    sub_bin_A1 = np.zeros(npix)
    sub_bin_A2 = np.zeros(npix)
    sub_bin_A3 = np.zeros(npix)
    sub_bin_A4 = np.zeros(npix)
    
    for pixel in pidx:
        sub_hpmap_A1[pixel] += A_1[i]
        sub_hpmap_A2[pixel] += A_2[i]
        sub_bin_A1[pixel] += 1
        sub_bin_A2[pixel] += 1
        i += 1 
    for pixel_flip in pidx_flip:
        sub_hpmap_A3[pixel_flip] += A_2[j]
        sub_hpmap_A4[pixel_flip] += A_1[j]
        sub_bin_A3[pixel_flip] += 1
        sub_bin_A4[pixel_flip] += 1
        j+=1
       
    hpmap_A_1 = sub_hpmap_A1/sub_bin_A1
    hpmap_A_2 = sub_hpmap_A2/sub_bin_A2
    hpmap_A_3 = sub_hpmap_A3/sub_bin_A3
    hpmap_A_4 = sub_hpmap_A4/sub_bin_A4
    
    # rotation 
    
    stack_rotations = np.arange(0, 360, 22.5)
    
    sum_A = 0
    weighting_all_stacks = 0 
    
    for stack in stacks:
        
        rot = hp.rotator.Rotator(rot=(0, stack_rotations[stack-1], 90))
        
        rot_A_1 = rot.rotate_map_pixel(hpmap_A_1)
        rot_A_2 = rot.rotate_map_pixel(hpmap_A_2)
        rot_A_3 = rot.rotate_map_pixel(hpmap_A_3)
        rot_A_4 = rot.rotate_map_pixel(hpmap_A_4)
        
        # weight values: magnitude of amplitude at center
        
        weight_1 = (np.abs(rot_A_1))[center]
        weight_2 = (np.abs(rot_A_2))[center]
        weight_3 = (np.abs(rot_A_3))[center]
        weight_4 = (np.abs(rot_A_4))[center]
        
        if SNR == True:
            sub_tot = (rot_A_1*weight_1 + rot_A_2*weight_2 + rot_A_3*weight_3 + rot_A_4*weight_4)
            D = np.abs(sub_tot)**2
            
        else: # SNR == False
            
            sub_tot = (rot_A_1 + rot_A_2 + rot_A_3 + rot_A_4)
            D = np.abs(sub_tot)**2
        
        # phase corrections
        
        tot_phase = np.unwrap(np.arctan2(np.imag(sub_tot), np.real(sub_tot)))

        phase = tot_phase[center]
        
        if SNR == True:
            
        # weighting based power at the center
            
            A_weighted_stack = sub_tot/(weight_1+weight_2+weight_3+weight_4)
        
            D_stack = np.abs(A_weighted_stack)**2
            
            weight_stack = (np.abs(A_weighted_stack))[center]

            sum_A += np.exp(-1j*phase)*(A_weighted_stack)*weight_stack
                
            weighting_all_stacks += weight_stack**2

        else: # SNR == False
                
            sum_A += np.exp(-1j*phase) * (rot_A_1 + rot_A_2 + rot_A_3 + rot_A_4)
    
    # Normalizing for total number of stacks
    
    if SNR == True:
        
        return_value = (np.abs(sum_A))**2/weighting_all_stacks
            
    else: # SNR == False
        return_value = (np.abs(sum_A))**2/len(stacks)
    
    return return_value
