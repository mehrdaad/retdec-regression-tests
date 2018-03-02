from regression_tests import *


class TestStringTableSegfault(Test):

    settings = TestSettings(
        tool='fileinfo',
        input='79e34ba714e38c7e72f30b5dcb54ba4e4e05915dbaece7fdf4271b1410306e04'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded


class TestDynamicSegfault(Test):

    settings = TestSettings(
        tool='fileinfo',
        input='4dfc8ebfa6d90d2fbacf56c035b04aa38a3c595f462904f4a038d45dcb9d3a7b'
    )

    def test_no_segfault(self):
        assert self.fileinfo.succeeded
