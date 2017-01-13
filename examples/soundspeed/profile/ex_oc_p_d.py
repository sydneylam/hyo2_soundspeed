from __future__ import absolute_import, division, print_function, unicode_literals

import os

from hydroffice.soundspeed.logging import test_logging

import logging
logger = logging.getLogger()

from hydroffice.soundspeed.profile.oceanography import Oceanography as Oc

# check values from Fofonoff and Millard(1983)
trusted_fof_d = 9712.653  # m
trusted_fof_p = 10000  # dBar
trusted_fof_lat = 30.0

calc_d = Oc.p2d_backup(p=trusted_fof_p, lat=trusted_fof_lat)
logger.info("Backup: Depth: %.3f <> %.3f" % (calc_d, trusted_fof_d))

calc_d = Oc.p2d_gsw(p=trusted_fof_p, lat=trusted_fof_lat, dyn_height=None)
logger.info("GSW: Depth: %.3f <> %.3f" % (calc_d, trusted_fof_d))

calc_p = Oc.d2p_backup(d=calc_d, lat=trusted_fof_lat)
logger.info("Backup: Pressure: %.3f <> %.3f" % (calc_p, trusted_fof_p))

calc_p = Oc.d2p_gsw(d=trusted_fof_d, lat=trusted_fof_lat, dyn_height=None)
logger.info("GSW: Pressure: %.3f <> %.3f" % (calc_p, trusted_fof_p))
