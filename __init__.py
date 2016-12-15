from eqnet import *
import glob
sampdirs = glob.glob("../..//*.mat")
buildNetFile(sampdirs, netfile, cutoff, auxDir, writecomponents=False)