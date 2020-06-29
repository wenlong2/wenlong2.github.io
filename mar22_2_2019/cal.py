import numpy as np
import extinction
import sys, os
sys.path.append('/Users/wenlong/Codes/libs/pylib')
import myfuncs as cf
from astropy.io import ascii

f5 = 5410.
f8 = 8353.
f1 = 15450.
wave = np.array([f5, f8, f1])
av = 1.0
rv = 3.1

log = cf.HtmlLog('./','Reddening.html')
log.add_line('Python version of simple reddening', AppendLog=False)


ccm89 = extinction.ccm89(wave, av, rv)
f99 = extinction.fitzpatrick99(wave, av, rv)
fm07 = extinction.fm07(wave, av, 'aa')

rv = 3.1
fout = 'table.dat'
hout = open(fout, 'w')
hout.write('#  Law   Rv   A555   A814   A160   RIvi    RHvi\n')
law = 'CCM89'
av, ai, ah = extinction.ccm89(wave, av, rv)
rivi = ai / (av - ai)
rhvi = ah / (av - ai)
fmt = '%10s' + '%10.3f'*6 + '\n'
hout.write(fmt % (law, rv, av, ai, ah, rivi, rhvi))

law = 'F99'
av, ai, ah = extinction.fitzpatrick99(wave, av, rv)
rivi = ai / (av - ai)
rhvi = ah / (av - ai)
hout.write(fmt % (law, rv, av, ai, ah, rivi, rhvi))

law = 'FM07'
av, ai, ah = extinction.fm07(wave, av, 'aa')
rivi = ai / (av - ai)
rhvi = ah / (av - ai)
hout.write(fmt % (law, rv, av, ai, ah, rivi, rhvi))

for rv in [2.9, 3.3, 3.5, 3.7]:
    law = 'CCM89'
    av, ai, ah = extinction.ccm89(wave, av, rv)
    rivi = ai / (av - ai)
    rhvi = ah / (av - ai)
    hout.write(fmt % (law, rv, av, ai, ah, rivi, rhvi))

    law = 'F99'
    av, ai, ah = extinction.fitzpatrick99(wave, av, rv)
    rivi = ai / (av - ai)
    rhvi = ah / (av - ai)
    hout.write(fmt % (law, rv, av, ai, ah, rivi, rhvi))
hout.close()

dat = ascii.read(fout)
log.add_table(dat)
