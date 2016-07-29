# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                ARK Grid
                    A QGIS plugin for Archaeological Recording.
        Part of the Archaeological Recording Kit by L-P : Archaeology
                        http://ark.lparchaeology.com
                              -------------------
        begin                : 2016-07-29
        git sha              : $Format:%H$
        copyright            : 2016 by L-P : Heritage LLP
        email                : ark@lparchaeology.com
        copyright            : 2016 by John Layt
        email                : john@layt.net
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

import os.path

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ArkSpatial class from file arkspatial.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .arkgrid import ArkGrid
    return ArkGrid(iface, os.path.dirname(__file__))
