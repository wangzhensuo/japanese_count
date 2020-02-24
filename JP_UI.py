# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JP_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import xlwt
from PyQt5.QtWidgets import QWidget,QHeaderView
from PyQt5.QtGui import QMouseEvent,QPixmap
from PyQt5.QtCore import QCoreApplication,QPoint,Qt
import os,sys
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.pushButton_clear = QtWidgets.QPushButton(self.tab)
        # self.pushButton_clear.setObjectName("pushButton_clear")
        # self.horizontalLayout_4.addWidget(self.pushButton_clear)
        self.btn_wordcount = QtWidgets.QPushButton(self.tab)
        self.btn_wordcount.setObjectName("btn_wordcount")
        self.horizontalLayout_4.addWidget(self.btn_wordcount)
        self.pushButton_exfile = QtWidgets.QPushButton(self.tab)
        self.pushButton_exfile.setObjectName("pushButton_exfile")
        self.horizontalLayout_4.addWidget(self.pushButton_exfile)
        self.pushButton_close = QtWidgets.QPushButton(self.tab)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_4.addWidget(self.pushButton_close)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.textEdit = QtWidgets.QTextEdit(self.tab)
        # self.textEdit.setObjectName("textEdit")
        # self.textEdit.setText("\n使用方法：\
        # \n 1.点击“打开”加载需要统计单词的日文文档（支持txt、docx、pdf）；\
        # \n 2.稍候片刻，建议喝杯咖啡，看看窗外的风景放松一下；")
        # self.horizontalLayout_3.addWidget(self.textEdit)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 2, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.pushButton_duibi = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_duibi.setGeometry(QtCore.QRect(10, 10, 181, 31))
        self.pushButton_duibi.setObjectName("pushButton_duibi")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 50, 181, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.layoutWidget = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 60, 100, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.doc_in_action = QtWidgets.QAction(MainWindow)
        self.doc_in_action.setCheckable(True)
        self.doc_in_action.setChecked(False)
        self.doc_in_action.setObjectName("doc_in_action")
        self.cp_in_action = QtWidgets.QAction(MainWindow)
        self.cp_in_action.setCheckable(True)
        self.cp_in_action.setObjectName("cp_in_action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addSeparator()
        self.menu.addAction(self.doc_in_action)
        self.menu.addAction(self.cp_in_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.doc_in_action.triggered['bool'].connect(self.doc_in_action.setChecked)
        self.cp_in_action.triggered['bool'].connect(self.cp_in_action.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # def doc_in_action_checked(self):
    #     self.in_mode_action = 0
    #     self.cp_in_action.setChecked(False)
    #     self.doc_in_action.setChecked(True)
    #     self.menu.setTitle("【文档导入】模式")
    #     self.btn_wordcount.setText("导入文档")
    #     self.textEdit.setText("当前操作模式已切换为【文档导入】模式，\n请点击【导入文档】进行文档导入。\n点击左上角菜单栏进行切换")

    def cp_in_action_checked(self):
        self.in_mode_action = 1
        self.doc_in_action.setChecked(False)
        self.cp_in_action.setChecked(True)
        self.menu.setTitle("【文本复制粘贴】模式")
        self.btn_wordcount.setText("开始统计")
        self.textEdit.setText("当前操作模式已切换为【文本复制粘贴】模式，\n请将需要统计的文本复制粘贴到这里，\n点击【开始统计】即可。\n中文不会被统计。")
 
    def quit_APP(self):
        # if os.path.exists(resource_path('./data/englishwords.db')):
        #     os.rename(resource_path('./data/englishwords.db'),resource_path('./data/tmp.dll'))
        # if os.path.exists(resource_path('./data/englishwords.db')):
        #     os.rename(resource_path('./data/lemma.db'),resource_path('./data/temp.dll'))
        # if os.path.exists(resource_path('./data/blue.qss')):
        #     os.rename(resource_path('./data/blue.qss'),resource_path('./data/blue.dll')) 

        # os.rename(resource_path('./data/englishwords.db'),resource_path('./data/tmp.dll'))
        # os.rename(resource_path('./data/lemma.db'),resource_path('./data/temp.dll'))
        # os.remove(resource_path('./data/englishwords.db'))
        QCoreApplication.quit()
    def show_zhifu(self):
        pix = QPixmap(resource_path('.//data//zf.png'))
        width = self.label_4.width()
        height = self.label_4.height()
        pix2 = pix.scaled(width,height,Qt.IgnoreAspectRatio,Qt.SmoothTransformation)
        # self.label_4.setGeometry(0,300,581*3/4,367*3/4)
        # self.label_4.setStyleSheet("border: 2px solid")
        self.label_4.setPixmap(pix2)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "词频助手日语版1.8"))
        # self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.btn_wordcount.setText(_translate("MainWindow", "添加"))
        self.pushButton_exfile.setText(_translate("MainWindow", "保存"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        header = self.tableWidget.horizontalHeader() 
        header.setStretchLastSection(True) 
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "語数"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "表層形"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "品詞"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "活用型"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "活用形"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "基本形"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "読み"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "発音"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "词频统计"))
        self.pushButton_duibi.setToolTip(_translate("MainWindow", "<html><head/><body><p>使用方法：直接单击对比，在弹出的对话框中选择需要对比的两个xls文件即可。</p></body></html>"))
        self.pushButton_duibi.setText(_translate("MainWindow", "对比"))
        self.tableWidget_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>显示的是AB对比文件单词的并集。</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "词列对比"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>您好，朋友，欢迎使用词频助手。</p><p>它是我业余时间开发的一个小工具。</p><p>从控件布局到处理逻辑，从素材积累到界面美化，从错误排查到打包发布，</p><p>花费了大量的时间和精力。</p><p>曾经，在地铁上，在午休中，在睡觉前，无时无刻不在构思各个功能的组成。</p><p>体会了一种前所未有的专注感觉，所有的精力好像透过放大镜的太阳光一样，</p><p>聚焦到一个光点上。随着慢慢的完善，这个光点在变亮，变热，冒烟。</p><p>最后有了一点点星火。</p><p>《男儿当自强》有句歌词“用我百点热，耀出千分光”，百点热不敢遑论，</p><p>只是希望这个小工具能散发一点点热，</p><p>统计出高频的常考词汇，批量翻译出陌生的未知词汇，</p><p>合理的分配学习的精力，科学的提高学习的效率。</p><p>如果您觉得词频助手确实还行，并希望能持续更新完善，</p><p>您的捐助将是作者持续更新的无尽动力！</p><p>当前软件版本：20200209</p><p><span style=\" font-weight:600;\">词频助手最新版发布QQ群：587129532</span></p><p><span style=\" font-weight:600;\">微信：milestoners</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "随缘打赏"))
        self.label_4.resize(581*3/4,367*3/4)
        self.show_zhifu()
        self.pushButton_close.clicked.connect(self.quit_APP)

    def openfile(self, MainWindow):
        fileName1 = 'None'
        fileName1, filetype = QFileDialog.getOpenFileNames(self,"选取文件（支持txt docx pdf）","./","All Files (*);;Text Files (*.txt);;docx Files (*.docx);;pdf Files (*.pdf)")
        print(fileName1,filetype)
        return fileName1
    def open_some_files(self,MainWindow):
        fileName = 'None'
        ok = 'None'
        fileName, ok = QFileDialog.getOpenFileNames(self,"只能选择两个文件对比","./","All Files (*);;Text Files (*.xls)")
        print(fileName)
        return fileName
    def savefile(self):
        # fileName2, ok2 = QFileDialog.getSaveFileName(self,"文件保存","./","All Files (*);;Text Files (*.txt)")
        filename, filetype = QFileDialog.getSaveFileName(self, '文件保存', '', ".xls(*.xls)")
        if filename:
            wbk = xlwt.Workbook()
            sheet = wbk.add_sheet("词频统计", cell_overwrite_ok=True)
            self.add2(sheet)
            wbk.save(filename)

    def add2(self, sheet):
        for currentColumn in range(self.tableWidget.columnCount()):
            for currentRow in range(self.tableWidget.rowCount()):
                try:
                    teext = str(self.tableWidget.item(currentRow, currentColumn).text())
                    sheet.write(currentRow, currentColumn, teext)
                except AttributeError:
                    pass
    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)
 
    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())
 
    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
class MoneyBox(QWidget):
    def __init__(self, parent=None):
        super(MoneyBox, self).__init__(parent)
        self.resize(500, 500)
        # palette	= QPalette()
        # palette.setBrush(QPalette.Background,QBrush(QPixmap("aa.PNG")))
        
        # self.setPalette(palette)
        self.setWindowTitle("QMainWindow Background Image")
        png=QtGui.QPixmap('./data/wx.png')
        layout = QHBoxLayout()
        l1=QtWidgets.QLabel(self)
        l2=QtWidgets.QLabel(self)
        # l1.setPixmap(png)
        l1.resize(828/4,1136/4)
        l2.resize(720/4,1120/4)
        l1.setStyleSheet('QLabel{border-image:url(data/wx.png)}')
        l2.setStyleSheet('QLabel{border-image:url(data/zfb.png)}')
        layout.addWidget(l1)
        layout.addWidget(l2)
        # self.setLayout(layout)

        l3=QtWidgets.QLabel(self)
        l3.setText('如果您觉得软件很好用的话,\n能请程序员小哥哥一杯熬夜写代码的咖啡吗')

        layout2 = QVBoxLayout()
        layout2.addLayout(layout)
        layout2.addWidget(l3)

        self.setLayout(layout2)

    def handle_close(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    # s = MoneyBox()
    # s.show()
    sys.exit(app.exec_())
