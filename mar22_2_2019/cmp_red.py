import numpy as np
import extinction
import sys, os
sys.path.append('/Users/wenlong/Codes/libs/pylib')
import myfuncs as cf
from astropy.io import ascii
import matplotlib.pyplot as plt

figdir = 'figs/'
cf.mkdir(figdir)
log = cf.HtmlLog('./','Reddening.html')
log.add_line('Python version of integrated reddening', AppendLog=False)

log.add_line('<hr> HST filters:')

fv = 'F555W_UVIS_throughput.csv'
vdat = ascii.read(fv)
x = vdat['col2']
idx = (x > 4000) & (x < 10000)
vdat = vdat[idx]
fi = 'F814W_UVIS_throughput.csv'
idat = ascii.read(fi)
x = idat['col2']
idx = (x > 6000) & (x < 12000)
idat = idat[idx]
fh = 'F160W_IR_throughput.csv'
hdat = ascii.read(fh)
x = hdat['col2']
idx = (x > 13000) & (x < 24000)
hdat = hdat[idx]


rv = 3.1

fig, a = plt.subplots(1,1)
x = vdat['col2']
y = vdat['col3']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
av = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.5, 0.85, r'$A_{F555W} = $'+str(np.round(av, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.5, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('F555W throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'vthrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)
fig, a = plt.subplots(1,1)
x = idat['col2']
y = idat['col3']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.5, 0.85, r'$A_{F814W} = $'+str(np.round(ai, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.5, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('F814W throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'ithrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)
fig, a = plt.subplots(1,1)
x = hdat['col2']
y = hdat['col3']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.5, 0.85, r'$A_{F160W} = $'+str(np.round(ah, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.5, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('F160W throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'hthrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)

fmt = '%10s' + '%10.3f'*6 + '\n'
fout = 'table.dat'
hout = open(fout, 'w')
hout.write('#  Law   Rv   RIvi    RHvi   A_f555W   A_f814W   A_f160W\n')
for law in ['CCM89','F99']:
    if law == 'CCM89':
        myfunc = extinction.ccm89
    if law == 'F99':
        myfunc = extinction.fitzpatrick99
    for rv in [2.7, 2.9, 3.1, 3.3, 3.5]:
        x = vdat['col2']
        y = vdat['col3']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        av = -2.5*np.log10(np.sum(y2) / np.sum(y))
        x = idat['col2']
        y = idat['col3']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
        x = hdat['col2']
        y = hdat['col3']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
        rivi = ai / (av - ai)
        rhvi = ah / (av - ai)
        hout.write(fmt % (law, rv, rivi, rhvi, av, ai, ah))
law = 'FM07'
myfunc = extinction.fm07
rv = 3.1
x = vdat['col2']
y = vdat['col3']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
av = -2.5*np.log10(np.sum(y2) / np.sum(y))
x = idat['col2']
y = idat['col3']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
x = hdat['col2']
y = hdat['col3']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
rivi = ai / (av - ai)
rhvi = ah / (av - ai)
hout.write(fmt % (law, rv, rivi, rhvi, av, ai, ah))

hout.close()
dat = ascii.read(fout)
log.add_table(dat)

##################################

log.add_line('<hr> Ground filters:')

fv = 'bess-v.pass'
vdat = ascii.read(fv)
x = vdat['col1']
idx = (x > 4000) & (x < 10000)
vdat = vdat[idx]
fi = 'bess-i.pass'
idat = ascii.read(fi)
x = idat['col1']
idx = (x > 6000) & (x < 12000)
idat = idat[idx]
fh = '2mass-h.dat'
hdat = ascii.read(fh)
hdat['col1'] = hdat['col1'] * 1e4


rv = 3.1

fig, a = plt.subplots(1,1)
x = vdat['col1']
y = vdat['col2']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
av = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.5, 0.85, r'$A_{V} = $'+str(np.round(av, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.5, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('Ground V throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'gvthrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)
fig, a = plt.subplots(1,1)
x = idat['col1']
y = idat['col2']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.5, 0.85, r'$A_{I} = $'+str(np.round(ai, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.5, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('Ground I throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'githrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)
fig, a = plt.subplots(1,1)
x = hdat['col1']
y = hdat['col2']
a.plot(x, y, color='blue')
wave = np.array(x)
ccm89 = extinction.ccm89(wave, 1.0, rv)
y2 = y * 10**(-0.4 * ccm89)
a.plot(x, y2, color='red', alpha=0.8)
ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
plt.text(0.05, 0.85, r'$A_{H} = $'+str(np.round(ah, 3))+' mag', transform = a.transAxes, fontsize=20)
plt.text(0.05, 0.7, 'Rv = 3.1', transform = a.transAxes, fontsize=20)
a.set_xlabel('Wavelength [A]')
a.set_ylabel('Throughput')
a.set_title('Ground H throughput (blue), CCM89 extincted (red)')
fig.set_size_inches(7, 4)
plt.tight_layout()
f_fig = figdir + 'ghthrput.png'
fig.savefig(f_fig)
plt.close()
log.add_figure(f_fig, width='43%', linebreak=False)

fmt = '%10s' + '%10.3f'*6 + '\n'
fout = 'table.dat'
hout = open(fout, 'w')
hout.write('#  Law   Rv   RIvi    RHvi   A_V   A_I   A_H\n')
for law in ['CCM89','F99']:
    if law == 'CCM89':
        myfunc = extinction.ccm89
    if law == 'F99':
        myfunc = extinction.fitzpatrick99
    for rv in [2.7, 2.9, 3.1, 3.3, 3.5]:
        x = vdat['col1']
        y = vdat['col2']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        av = -2.5*np.log10(np.sum(y2) / np.sum(y))
        x = idat['col1']
        y = idat['col2']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
        x = hdat['col1']
        y = hdat['col2']
        wave = np.array(x)
        y2 = y * 10**(-0.4 * myfunc(wave, 1.0, rv))
        ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
        rivi = ai / (av - ai)
        rhvi = ah / (av - ai)
        hout.write(fmt % (law, rv, rivi, rhvi, av, ai, ah))
law = 'FM07'
myfunc = extinction.fm07
rv = 3.1
x = vdat['col1']
y = vdat['col2']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
av = -2.5*np.log10(np.sum(y2) / np.sum(y))
x = idat['col1']
y = idat['col2']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
ai = -2.5*np.log10(np.sum(y2) / np.sum(y))
x = hdat['col1']
y = hdat['col2']
wave = np.array(x)
y2 = y * 10**(-0.4 * myfunc(wave, 1.0, 'aa'))
ah = -2.5*np.log10(np.sum(y2) / np.sum(y))
rivi = ai / (av - ai)
rhvi = ah / (av - ai)
hout.write(fmt % (law, rv, rivi, rhvi, av, ai, ah))

hout.close()
dat = ascii.read(fout)
log.add_table(dat)

log.add_text('<br>'*20)
