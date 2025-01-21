def read_response(response_file):
    """
    Reads and processes a FITS response file to extract and desparsify the response matrix
    along with energy bounds and channel information.

    Parameters:
        response_file (str): Path to the FITS response file.

    Returns:
        tuple: A tuple containing:
            - response_matrix (numpy.ndarray): The desparsified response matrix.
            - elow (numpy.ndarray): Array of lower energy bounds.
            - ehigh (numpy.ndarray): Array of higher energy bounds.
            - Emin (numpy.ndarray): Array of minimum energy bounds for channels.
            - Emax (numpy.ndarray): Array of maximum energy bounds for channels.
            - chan (numpy.ndarray): Array of channel numbers.
    """

  
    #Open fits file and read matrix as well as ebound extensions
    with fits.open(response_file) as f:
        elow = f['MATRIX'].data['ENERG_LO']
        ehigh = f['MATRIX'].data['ENERG_HI']
        f_chan = f['MATRIX'].data['F_CHAN']
        n_chan = f['MATRIX'].data['N_CHAN']
        matrix = f['MATRIX'].data['MATRIX']
        chan = f['EBOUNDS'].data['CHANNEL']
        Emin = f['EBOUNDS'].data['E_MIN']
        Emax = f['EBOUNDS'].data['E_MAX']
        n_grp = f['MATRIX'].data['N_GRP']
        
        # Initialize the desparsified matrix with zeros
        response_matrix = np.zeros((len(elow), len(chan)))

     # Populate the desparsified response matrix

        for i in range(len(elow)):
            start = 0 
            for j in range(n_grp[i]):
                response_matrix[i, f_chan[i][j]:f_chan[i][j]+n_chan[i][j]] = matrix[i][start:start + n_chan[i][j]]
                start += n_chan[i][j]
            
    return response_matrix,elow,ehigh,Emin,Emax,chan
