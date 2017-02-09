from PyQt5 import QtGui, QtWidgets

from config import *

splash_image = options['ida_user_dir'] + os.sep + "rsrc" + os.sep + "splash.png"
pixmap = QtGui.QPixmap(splash_image)
splash = QtWidgets.QSplashScreen(pixmap)
splash.show()