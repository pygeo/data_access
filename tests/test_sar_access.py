"""
Test for SAR data access provider
"""

import unittest

from multiply_dummy.configuration import Configuration
from multiply_dummy.state import TargetState

from multiply_data_access.sar_data_access import SARDataAccessProvider
import datetime

import os
import tempfile

class TestSAR(unittest.TestCase):
    
    def setUp(self):
        self.odir = tempfile.mkdtemp() + os.sep
        t1 = datetime.datetime(2000,1,1)
        t2 = datetime.datetime(2002,12,31)
        tstate = TargetState(state={'lai':True, 'sm':False})
        r = {}
        r.update({'lr' : {'lat': 45., 'lon' : 11.2}})
        r.update({'ul' : {'lat': 47., 'lon' : 10.2}})
        self.c = Configuration(region=r, time_start=t1, time_stop=t2, tstate=tstate)

    def test_init(self):
        odir = self.odir + 'xyz'
        S = SARDataAccessProvider(config=self.c, output_dir=odir)
        self.assertTrue(os.path.exists(S.output_dir))
        self.assertTrue(S.output_dir[-1] == os.sep)

    def test_get_data(self):
        S = SARDataAccessProvider(config=self.c, output_dir=self.odir)
        r = S.get_data()
        self.assertTrue(isinstance(r, str))
