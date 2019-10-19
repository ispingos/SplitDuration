SplitDuration
=============

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3510113.svg)](https://doi.org/10.5281/zenodo.3510113)

Calculate the length of expected time periods of time-delays (acquired from shear-wave splitting) increase and decrease according to the empirical relations of Crampin et al. (2013).

For any issues, comments or suggestions please contact me at ispingos@geol.uoa.gr or through GitHub at https://www.github.com/ispingos/SplitDuration

You can find more information about stress cycles and shear-wave splitting in:
Crampin, S., Gao, Y. & De Santis, A. (2013) A few earthquake conundrums resolved. J Asian Earth Sci 62, 501-509. doi: 10.1016/j.jseaes.2012.10.036


Compatibility
-------------

* This program was developed and tested in a Windows 10 64 bit with Python 3.7. It should work with Python 2 as well (assuming ``PyQt5`` is installed), but it **has not been tested for this release**.
* The current released binary file is for Windows 10 64 bit. A future Linux binary may be added at at some time.

Prerequisites
-------------
If you want to run the source code, you will need to install the latest Python 3 and ``PyQt5``. After installing Python 3, you can install the latter through a command prompt / terminal, using the command: 

``pip install PyQt5``

How to run
-------------

With GUI:
- Simply run the script or the exe file. Insert the required earthquake magnitude in the respective field and press "Calculate".

Without GUI:
- From a console, run any of the two following commands in a command prompt / terminal (make sure you are in the source directory):
  
``python SplitDuration.py --console=True``

``SplitDuration.exe --console=True``

The program will prompt you to provide the required earthquake magnitude and will show the theoretical values for the accumulation and relaxation periods.

### Related Software ###

If you are interested in shear-wave splitting, take a look at our analysis software **Pytheas** @ https://www.github.com/ispingos/pytheas-splitting
