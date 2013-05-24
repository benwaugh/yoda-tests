from nose.tools import *
import math

from yoda.core import *

def test_HistoBin1D_fill_default():
    bin = HistoBin1D(0.0, 1.0)
    bin.fill()
    assert_almost_equal(1.0, bin.area)
    assert_almost_equal(1.0, bin.areaErr)
    assert_almost_equal(1.0, bin.height)
    assert_almost_equal(1.0, bin.heightErr)

def test_HistoBin1D_fill_weights_cancel():
    bin = HistoBin1D(0.0, 1.0)
    bin.fill(None, 1.0)
    bin.fill(None, -1.0)
    sqrt2 = math.sqrt(2.0)
    assert_almost_equal(0.0, bin.area)
    assert_almost_equal(sqrt2, bin.areaErr)
    assert_almost_equal(0, bin.height)
    assert_almost_equal(sqrt2, bin.heightErr)

# Not sure how to test for yoda.LogicError since can't import it.
@raises(Exception)
def test_add_incompatible_bins():
    bin1 = HistoBin1D(0.0, 0.5)
    bin2 = HistoBin1D(0.5, 1.0)
    bin_add = bin1 + bin2
    