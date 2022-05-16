import shutil

def check_pkg_exists(pkg: str):
    """Check whether a system package exists

    Checks whether a given executable is found on PATH, providing
    cross-platform functionality

    Parameters
    ----------
    pkg : str
        Name of the package to check

    Returns
    -------
    bool
        Whether ``pkg`` is found on PATH
    """
    return shutil.which(pkg) is not None
