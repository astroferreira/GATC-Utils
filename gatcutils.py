import os
import pyfits as pf
import numpy as np
import gc
import time

def normalizePSFs(path):
	psfsNames = sorted(os.listdir(path))

	#psfsNames = psfsNames[1999:]
	for name in psfsNames:
		print name
		try:
			psf, hdr = pf.getdata(path + name, header=1)
			psf = psf / psf.sum()
			pf.writeto(path + name, psf, hdr, clobber=1)
		except:
			print "Unexpected error:", sys.exc_info()[0]																																																																																																																																																																																																																																																																																																																																																																																																																																																											
			continue
	
