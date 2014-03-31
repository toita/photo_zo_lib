#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pz_operator
from pz_operator import *
import unittest


class TestFunctions(unittest.TestCase):

    def setUp(self):
        print 'setUp'

    def test1(self):
        print '#### User_ID test ####'
        pzo = PhotoZoOperator()
        assert pzo.get_user_id() == 12345, "error"

    def test2(self):
        print '#### Album_list test ####'
        pzo = PhotoZoOperator()
        res = [{'name': u'test', 'album_id': 1234567}]
        assert pzo.get_album_list() == res, "error"

    def test3(self):
        print '#### Album_ID test ####'
        pzo = PhotoZoOperator()
        assert pzo.get_album_id('citydiver_word') == 987655, "error"

    def test3(self):
        print '#### Add_photo test ####'
        pzo = PhotoZoOperator()
        assert pzo.add_photo('album_id', '/path/to/img', 'http://img/path') == 0, error


def main():
    unittest.main()


if __name__ == '__main__':
    main()
