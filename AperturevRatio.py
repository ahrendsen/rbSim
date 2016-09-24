from BeerLambert.beerlambertmc import *


# Plot Radius of Aperture vs. -log(transmission) / (b.sigt * b.length * b.nden). Depicts deviation of from Beer-Lambert
# Law for larger apertures
def apervratio(fig, count=50000, isotrop=True, electr=0, magnet=0):
    # Array of aperture radii
    aper = linspace(0.05, 1.0, 10)
    ratio = empty([0])

    for i in aper:
        # Set conditions of attenuating chamber
        b = Box(10 ** 16, count, aperture=i, isotropic=isotrop, electrfield=electr, magnetfield=magnet)
        transm = b.transmissvalue()
        ratio = append(ratio, [-log(transm) / (b.sigt * b.length * b.nden)])
        print(str(i) + ", " + str(ratio[-1]))

    w = fig.add_subplot(111)
    w.set_xlabel("Aperture (cm)")
    w.set_ylabel(r"$-\ln (I/I_0)/\sigma n l$")

    ymin = min(ratio)
    ymax = max(ratio)
    ymarg = (ymax - ymin) * 0.05
    w.set_ylim([ymin - ymarg, 1])
    w.set_xlim(0, 1.1)

    if isotrop is False:
        print("ANISOTROPIC: Red")
        w.scatter(aper, ratio, c="red")
    else:
        print("ISOTROPIC: Black")
        w.scatter(aper, ratio, c="black")

fig = figure()
fig.canvas.set_window_title("Beer-Lambert Law Monte Carlo: Isotropic and Anisotropic Scattering")

apervratio(fig, count=300000)
apervratio(fig, count=300000, isotrop=False)

show()