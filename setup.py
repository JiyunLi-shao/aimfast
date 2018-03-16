from setuptools import setup, find_packages

setup(name="aimfast",
      version="0.0.1",
      description="An Astronomical Image Fidelity Assessment Tool.",
      author="Athanaseus Ramaila",
      author_email="aramaila@ska.ac.za",
      packages=find_packages(),
      url="https://github.com/Athanaseus/aimfast",
      license="GNU GPL 3",
      classifiers=["Intended Audience :: Developers",
                   "Programming Language :: Python :: 3",
                   "Topic :: Software Development :: Libraries :: Python Modules"],
      platforms=["OS Independent"],
      install_requires=["astLib",
                        "astropy",
                        "astro-tigger",
                        "numpy",
                        "plotly",
                        "scikit-learn",
                        "scipy"],
      extras_require={'docs': ["sphinx-pypi-upload",
                               "numpydoc",
                               "Sphinx"]},
      scripts=['aimfast/bin/aimfast'])
