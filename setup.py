from distutils.core import setup, Extension

setup(name = 'pyephem',
      version = '3.5.2b1',
      description = 'Python interface to the XEphem libastro library',
      author = 'Brandon Craig Rhodes',
      author_email = 'brandon@rhodesmill.org',
      url = 'http://www.rhodesmill.org/brandon/projects/pyephem.html',
      ext_modules = [Extension('ephem',
                               ['src/ephem.c',
                                'libastro/aa_hadec.c',
                                'libastro/aberration.c',
                                'libastro/actan.c',
                                'libastro/anomaly.c',
                                'libastro/ap_as.c',
                                'libastro/auxil.c',
                                'libastro/chap95.c',
                                'libastro/chap95_data.c',
                                'libastro/circum.c',
                                'libastro/constel.c',
                                'libastro/comet.c',
                                'libastro/dbfmt.c',
                                'libastro/deep.c',
                                'libastro/deltat.c',
                                'libastro/earthsat.c',
                                'libastro/eq_ecl.c',
                                'libastro/eq_gal.c',
                                'libastro/formats.c',
                                'libastro/helio.c',
                                'libastro/libration.c',
                                'libastro/misc.c',
                                'libastro/mjd.c',
                                'libastro/moon.c',
                                'libastro/mooncolong.c',
                                'libastro/nutation.c',
                                'libastro/obliq.c',
                                'libastro/parallax.c',
                                'libastro/plans.c',
                                'libastro/precess.c',
                                'libastro/reduce.c',
                                'libastro/refract.c',
                                'libastro/rings.c',
                                'libastro/riset.c',
                                'libastro/riset_cir.c',
                                'libastro/sdp4.c',
                                'libastro/sgp4.c',
                                'libastro/sphcart.c',
                                'libastro/sun.c',
                                'libastro/thetag.c',
                                'libastro/twobody.c',
                                'libastro/utc_gst.c',
                                'libastro/vsop87.c',
                                'libastro/vsop87_data.c'],
                               #extra_compile_args = ["-O2", "-ffast-math"],
                               include_dirs=['libastro'])])
