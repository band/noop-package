#!/usr/bin/env python3
import pytest
import subprocess

def test_main_output():
    result = subprocess.run(['python', 'src/noop_BAND/noop.py'], capture_output=True, text=True)
    assert "nothing going on here" in result.stderr

