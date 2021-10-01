# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SudutJarakDialog
                                 A QGIS plugin
 Penggambaran sudut dan jarak
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-09-30
        git sha              : $Format:%H$
        copyright            : (C) 2021 by SandySetyanagara
        email                : sandysetyanagara@mail.ugm.ac.id
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsVectorLayer, QgsProject, QgsFeature, QgsGeometry,QgsPointXY
from qgis.utils import iface


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'sudut_jarak_dialog_base.ui'))

class SudutJarakDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SudutJarakDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.iface = iface
        self.plot.clicked.connect(self.gambar_plot)

    def gambar_plot(self):
        """ Lakukan sesuatu ketika tombol ditekan """
        # memanggil isi dari Line Edit pada kolom X dan
        # menyimpannya pada variabel self.nilai_x
        # sekaligus mengkonversinya menjadi angka
        try:
            x = int(self.input_x.text())
            y = int(self.input_y.text())
            # cetak isi nilai X
            print(x,y)
            self.buat_titik(x,y)
        except Exception as e:
            print(e)
    
    def buat_titik(self, x, y):
        """ buat titik di koordinat masukan """
        # cek masukan
        print(x, y)
        # membuat layer pada memory
        # anggap bahwa pengguna hanya di sekitar yogya (zona EPSG:32749)
        layer = QgsVectorLayer(f"Point?crs=EPSG:32749", "Plot Titik", "memory")
        QgsProject.instance().addMapLayer(layer)
        # memberi geometri pada fitur baru
        feature = QgsFeature()
        feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
        # menambahkan fitur pada layer
        layer.dataProvider().addFeatures([feature])
        layer.updateExtents()
        
        # ini comment 2

        print("woy")

        self.iface.actionZoomToLayer().trigger()


