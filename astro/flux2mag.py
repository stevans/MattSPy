
def now(flux_arr, units = 'nJy'):
	#convert flux to mag

	import numpy as np


	if units == 'nJy':
		zeropoint = 31.4

	mag_arr = -2.5*np.log10(flux_arr]) + zeropoint

	return mag_arr