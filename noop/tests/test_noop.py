#!/usr/bin/env python3

import logging                                                                                                       
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')                                         

@pytest.fixture(scope="module")
def run_and_verify():
    assert True


