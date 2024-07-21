#  -*- coding: utf-8 -*-
"""
.. _tutorial-operating:

=============================
Math Operations
=============================

It is often the case where measurements of an experiment are collected ...
"""
# %%
# First steps with the samples
# ----------------------------
#
# Initially, imagine that you have been given this
# :download:`csv file <../../__data/antenna_samples_freq_17.00GHz.csv>`
# containing the field samples of the antenna collected at 17.00 GHz.
# The table in the file has the following six columns:
#
# - ``theta_deg`` : denotes the polar angle :math:`\theta` (in degrees) of the direction at
#   which the sample has been measured.
#
# - ``phi_deg`` : denotes the azimuthal angle :math:`\phi` (in degrees) of the direction at
#   which the sample has been measured.
#
# - ``E_theta_real_mV`` : denotes the real part of vertical component :math:`\MEN_\theta` (in mV)
#   of the normalised electric phasor field measured at the direction :math:`\pare{\theta, \phi}`.
#
# - ``E_theta_imag_mV`` : denotes the imaginary part of vertical component :math:`\MEN_\theta` (in mV)
#   of the normalised electric phasor field measured at the direction :math:`\pare{\theta, \phi}`.
#
# - ``E_phi_real_mV`` : denotes the real part of horizontal component :math:`\MEN_\phi` (in mV)
#   of the normalised electric phasor field measured at the direction :math:`\pare{\theta, \phi}`.
#
# - ``E_phi_imag_mV`` : denotes the imaginary part of horizontal component :math:`\MEN_\phi` (in mV)
#   of the normalised electric phasor field measured at the direction :math:`\pare{\theta, \phi}`.
#
# You should be able to create a simple function to read such file and return the data as
# `quantities <https://docs.astropy.org/en/stable/units/>`_ as follows:


import numpy


print(numpy.random.randn(3, 3))


# %%
# Plotting something cool
# -----------------------
#
# The measurements package provides the :func:`plot_samples_2D <aftk.measurements.plot_samples_2D>`
# function, which plots the magnitude of total field and its components in a heatmap alongside the
# distribution of the sampling directions.

from matplotlib import pyplot

# %%

figure, axes = pyplot.subplots()

x = numpy.random.randn(1000)
y = numpy.random.randn(1000)

a = numpy.cumsum(x)
b = numpy.cumsum(y)

axes.plot(a, b, '.')

