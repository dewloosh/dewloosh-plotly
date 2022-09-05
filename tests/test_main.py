# -*- coding: utf-8 -*-
import unittest
import numpy as np
from polymesh.grid import grid
from polymesh.topo.tr import Q4_to_T3
from dewloosh.plotly import plot_triangles_2d
from dewloosh.plotly import scatter_lines_3d


class TestMain(unittest.TestCase):

    def test_1d(self):
        ...
        
    def test_2d(self):
        
        gridparams = {
            'size' : (1200, 600),
            'shape' : (30, 15),
            'eshape' : (2, 2),
            'origo' : (0, 0),
            'start' : 0
        }
        coordsQ4, topoQ4 = grid(**gridparams)
        points, triangles = Q4_to_T3(coordsQ4, topoQ4, path='grid')
        fig = plot_triangles_2d(points, np.random.rand(len(points)))
        
    def test_3d(self):
        ...
        
        
if __name__ == "__main__":
    unittest.main()
