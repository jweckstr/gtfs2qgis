# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GTFS2QGIS
                                 A QGIS plugin
 This plugin enables loading GTFS data into QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-06-28
        copyright            : (C) 2019 by Christoffer Weckström
        email                : j.c.weckstrom@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GTFS2QGIS class from file GTFS2QGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gtfs2_qgis import GTFS2QGIS
    return GTFS2QGIS(iface)
