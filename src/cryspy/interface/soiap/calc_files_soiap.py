'''
Calculation files in soiap
'''

from logging import getLogger
import os

from ...IO import read_input as rin


logger = getLogger('cryspy')

def check_input_soiap():
    # ---------- prepare rin.jobfile, rin.soiap_infile
    calc_inputs = [rin.jobfile, rin.soiap_infile]

    # ----- check required files
    for f in calc_inputs:
        if f == rin.soiap_infile:
            finfiles = [rin.soiap_infile + '_{}'.format(i)
                        for i in range(1, rin.nstage+1)]
            for ff in finfiles:
                if not os.path.isfile('./calc_in/'+ff):
                    logger.error('Could not find ./calc_in/'+ff)
                    raise SystemExit(1)
        else:
            if not os.path.isfile('./calc_in/'+f):
                logger.error('Could not find ./calc_in/'+f)
                raise SystemExit(1)
