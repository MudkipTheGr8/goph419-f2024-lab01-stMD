def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Function that takes as input the ratio of escape velocity to terminal velocity ve_v0, the desired maximum altitude as a fraction of Earth's radius alpha and the tolerance for maximum altitude tol_alpha.
    Parameters
    ----------
    ve_v0 :
    alpha :
    tol_alpha :
    Returns
    -------
    """
    import numpy as np

    min = float((1+tol_alpha)*alpha)
    max = float((1-tol_alpha)*alpha)
    # x = (1+aplha)*(numpy.sqrt(1-(alpha/(1+alpha))*(ve_v0)**2))
    # inverse = (x*(sin)**(-1))**2
    min_x = (1 + min) * np.sqrt((1 - (min / (1 + min)) * ((float(ve_v0)) ** 2)))
    max_x = (1 + max) * np.sqrt((1 - (max / (1 + max)) * ((float(ve_v0)) ** 2)))
    #
    min_inverse = round((np.arcsin(min_x)) ** 2, 5)
    max_inverse = round((np.arcsin(max_x)) ** 2, 5)
    # ...
    # implementation of Equations (17) and (18)
    # ...
    phi_range = np.array([min_inverse, max_inverse])
    return phi_range