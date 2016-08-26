def now(array):

		#normalized median absolute deviation
		import numpy as np
		nmad_now  = np.median(np.abs(np.median(array)-array))/0.6745
		return nmad_now