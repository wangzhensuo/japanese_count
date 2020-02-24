import os
import random
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import QThread, pyqtSignal,Qt
from PyQt5.QtGui import QTextCharFormat, QTextDocument, QTextCursor,QColor,QFont,QBrush
from PyQt5.QtWidgets import QMessageBox,QColorDialog,QTableWidgetItem
from pydub import AudioSegment
import sys
from JP_UI import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore,QtWidgets,QtGui
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *
import re
import chardet
import xlrd
import xlwt
import time
import docx
kana = {
    'ア':'あ', 'ァ':'あ', '々':'々', 
    'イ':'い', 
    'ウ':'う', 
    'エ':'え', 
    'オ':'お', 'ォ':'お', 
    'カ':'か', 
    'キ':'き', 
    'ク':'く', 
    'ケ':'け', 
    'コ':'こ', 
    'サ':'さ', 
    'シ':'し', 
    'ス':'す', 
    'セ':'せ', 
    'ソ':'そ', 
    'タ':'た', 
    'チ':'ち', 
    'ツ':'つ', 
    'テ':'て', 
    'ト':'と', 
    'ナ':'な', 
    'ニ':'に', 
    'ヌ':'ぬ', 
    'ネ':'ね', 
    'ノ':'の', 
    'ハ':'は', 
    'ヒ':'ひ', 
    'フ':'ふ', 
    'ヘ':'へ', 
    'ホ':'ほ', 
    'マ':'ま', 
    'ミ':'み', 
    'ム':'む', 
    'メ':'め', 
    'モ':'も', 
    'ヤ':'や', 
    'ユ':'ゆ', 
    'ヨ':'よ', 
    'ラ':'ら', 
    'リ':'り', 
    'ル':'る', 
    'レ':'れ', 
    'ロ':'ろ', 
    'ワ':'わ', 
    'ヲ':'を', 
    'ン':'ん', 
    'ガ':'が', 
    'ギ':'ぎ', 
    'グ':'ぐ', 
    'ゲ':'げ', 
    'ゴ':'ご', 
    'ザ':'ざ', 
    'ジ':'じ', 
    'ズ':'ず', 
    'ゼ':'ぜ', 
    'ゾ':'ぞ', 
    'ダ':'だ', 
    'ヂ':'ぢ', 
    'ヅ':'づ', 
    'デ':'で', 
    'ド':'ど', 
    'バ':'ば', 
    'ビ':'び', 
    'ブ':'ぶ', 
    'ベ':'べ', 
    'ボ':'ぼ', 
    'パ':'ぱ', 
    'ピ':'ぴ', 
    'プ':'ぷ', 
    'ペ':'ぺ', 
    'ポ':'ぽ', 
    'ャ':'ゃ', 
    'ュ':'ゅ', 
    'ョ':'ょ', 
    'ー':'い', 
    '*':'*',
    'ッ':'っ',
    'ィ':'い',
    'ェ':'え',
}
class CommonHelper:
    def __init__(self):
        pass
 
    @staticmethod
    def readQss(style):
        with open(style, 'r') as f:
            return f.read()
def trans(words):
    trans_words = ''
    print(words)
    trans_words = ''.join([kana[x] for x in list(words)])
    print(trans_words)
    return trans_words
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    # print(os.path.join(base_path, relative_path))
    return os.path.join(base_path, relative_path)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_wordcount.clicked.connect(self.btn_wordcount_clicked)
        self.pushButton_exfile.clicked.connect(self.pushButton_exfile_clicked)
        self.pushButton_duibi.clicked.connect(self.pushButton_duibi_clicked)

    def pushButton_duibi_clicked(self):
        file_path = self.open_some_files(MainWindow)
        if len(file_path) ==2:
            self.thread = RunThread(file_path,2)
            self.thread.save_compare_file_signal.connect(self.save_compare_file)
            self.thread.start()
    def save_compare_file(self,str):
        if str=='1':
            QMessageBox.information(self, "温馨提示", "保存成功，快去软件所在目录看看吧！")
    def btn_wordcount_clicked(self):
        file_path = self.openfile(MainWindow)
        self.tableWidget.clear()
        self.tableWidget.setRowCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['語数','表層形','発音','基本形','品詞','活用型','活用形','読み'])
        # self.tableWidget.setHorizontalHeaderLabels(['語数','表層形','品詞','活用型','活用形','基本形','読み','発音'])
        self.thread = RunThread(file_path,1)
        self.thread.words_signal.connect(self.add_words_to_table)
        self.thread.start()
        self.thread.proessbar_signal.connect(self.set_progressbar_value)
    def set_progressbar_value(self, value, max,level,text):
        self.progressBar.setFormat(text)
        self.progressBar.setValue(value)
        self.progressBar.setMaximum(max)
        if value == max:
            self.progressBar.setFormat('处理完成。您的捐助将是作者不断更新的无尽动力！')
            self.progressBar.setValue(0)
        return
    def add_words_to_table(self,line,num,l1,l2,l3,l4,l5,l6,l7):
        # print('add:',line,num,l1,l2,l3,l4,l5,l6,l7)
        self.tableWidget.setItem(line , 0, QtWidgets.QTableWidgetItem(num))
        self.tableWidget.setItem(line , 1, QtWidgets.QTableWidgetItem(l1))
        self.tableWidget.setItem(line , 2, QtWidgets.QTableWidgetItem(l2))
        self.tableWidget.setItem(line , 3, QtWidgets.QTableWidgetItem(l3))
        self.tableWidget.setItem(line , 4, QtWidgets.QTableWidgetItem(l4))
        self.tableWidget.setItem(line , 5, QtWidgets.QTableWidgetItem(l5))
        self.tableWidget.setItem(line , 6, QtWidgets.QTableWidgetItem(l6))
        self.tableWidget.setItem(line , 7, QtWidgets.QTableWidgetItem(l7))
        rowPosition = self.tableWidget.rowCount()
        # print(rowPosition)
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.scrollToBottom()
        # self.tableWidget.setColumnWidth(0,50)
        # self.tableWidget.setColumnWidth(1,50)
        # self.tableWidget.setColumnWidth(2,50)
        # self.tableWidget.setColumnWidth(3,50)
    def pushButton_exfile_clicked(self):
        self.savefile()
class RunThread(QThread):
    words_signal = pyqtSignal(int,str,str,str,str,str,str,str,str)
    proessbar_signal = pyqtSignal(int,int,int,str)
    save_compare_file_signal = pyqtSignal(str)
    def __init__(self,file_path,thread_id):
        super(RunThread, self).__init__()
        self.file_path = file_path
        self.thread_id = thread_id
        
    def __del__(self):
        self.wait() 

    def run(self):
        if self.thread_id == 1:    #词频统计（词形还原）
            some_files = ''
            for files in self.file_path:
                file_str = self.read_file(files)
                print(file_str)
                some_files=some_files+file_str
            print(some_files)
            file_str=some_files
            if file_str != None:
                self.text2wordinfolist(file_str)
        elif self.thread_id ==2:#Excel对比
            self.compare_excel(self.file_path[0],self.file_path[1])

    def read_file(self,file_path):
        words=[]
        raw_words=''
        if '.txt' in file_path:
            with open(file_path,'rb')as f:
                raw_words = f.read() 
                # raw_words = raw_words.encode('utf-8').decode('gbk','replace').encode('gbk','ignore')
                print(raw_words)
                print(raw_words.decode("utf8","ignore"))
                try:
                    result = chardet.detect(raw_words)
                    print(result['encoding'])
                    if result['encoding']=='GB2312':
                        
                        
                        raw_words=raw_words.decode('utf-8')
                        print(raw_words)
                        words = raw_words
                    else:
                        raw_words = raw_words.decode(encoding=result['encoding'])
                        words = raw_words
                    # self.set_text_show_signal.emit(raw_words)    
                    # low_words = raw_words.lower()
                    # words = re.findall('[a-z]+',low_words) #正则re找到所有单词
                except:
                    # QMessageBox.information(self, "警告", "文件编码有问题！请转换为utf8")
                    return ''
        elif '.docx' in file_path:
            file=docx.Document(file_path)
            docx_txt = ''
            for para in file.paragraphs:
                docx_txt=docx_txt+para.text
            raw_words = docx_txt
            try:
                words = raw_words
                # self.set_text_show_signal.emit(raw_words)    
                # low_words = raw_words.lower()
                # words = re.findall('[a-z]+',low_words) #正则re找到所有单词
            except:
                QMessageBox.information(self, "警告", "文件编码有问题！请转换为utf8")
                return ''
        elif '.pdf' in file_path:
            # resource manager
            rsrcmgr = PDFResourceManager()
            retstr = StringIO()
            laparams = LAParams()
            # device
            device = TextConverter(rsrcmgr, retstr, laparams=laparams)
            with open(file_path, "rb") as my_pdf:
                process_pdf(rsrcmgr, device, my_pdf)
                device.close()
                content = retstr.getvalue()
                retstr.close()
                raw_words = str(content)
                try:
                    words = raw_words
                except:
                    QMessageBox.information(self, "警告", "文件编码有问题！请转换为utf8")
                    return ''
        return words
    def text2wordinfolist(self,text):
        stopwords = '。'
        # text = u'の12時から朝6時まで。朝6時でも、お給料はいいんですよ。'
        # char_filters = [UnicodeNormalizeCharFilter()]
        # print(text)
        self.proessbar_signal.emit(20,100,1,'正在加载自然语言分析库') 
        text =  re.sub('\W+', '。', text)
        tokenizer = Tokenizer()
        self.proessbar_signal.emit(40,100,1,'正在加载自然语言分析库')
        token_filters = [CompoundNounFilter(),LowerCaseFilter()]
        self.proessbar_signal.emit(80,100,1,'正在加载自然语言分析库')
        analyzer = Analyzer([], tokenizer, token_filters)
        self.proessbar_signal.emit(99,100,1,'正在加载自然语言分析库')
        word_list =[]
        all_word_lists =[]
        progress=0
        for token in analyzer.analyze(text):
            # self.proessbar_signal.emit(64,100,1,token.surface) 
            word_list.append(token.surface)
            word_list.append(token.part_of_speech)
            word_list.append(token.infl_type)
            word_list.append(token.infl_form)
            word_list.append(token.base_form)
            word_list.append(token.reading)
            word_list.append(token.phonetic)
            all_word_lists.append(word_list)
            print(word_list)
            word_list =[]
            progress=progress+1
            self.proessbar_signal.emit(random.randint(61,80),100,1,'正在处理词语 [ '+token.surface+' ]  ') 
        d={}
        word_list=[]
        for key in all_word_lists: 
            d[key[0]] = d.get(key[0], 0) + 1
        l1=(sorted(d.items(), key = lambda x: x[1], reverse = True))
        l2=[w for w in l1 if w[0] not in stopwords]
        line = 0
        for l in l2:
            for wordinfo in all_word_lists:
                # print(wordinfo)
                # print(len(wordinfo))
                if l[0] == wordinfo[0]:
                    # print(line,wordinfo[0],str(l[1]),wordinfo[1],wordinfo[2],wordinfo[3],wordinfo[4],wordinfo[5],wordinfo[6])
                    # self.words_signal.emit(line,wordinfo[0],str(l[1]),wordinfo[1],wordinfo[2],wordinfo[3],wordinfo[4],wordinfo[5],trans(wordinfo[6]))
                    print(wordinfo)
                    self.words_signal.emit(line,str(l[1]),wordinfo[0],trans(wordinfo[5]),wordinfo[4],wordinfo[1],wordinfo[2],wordinfo[3],wordinfo[5])
                    line = line + 1
                    break
            self.proessbar_signal.emit(line,len(l2),2,'词频信息整理中') 
        self.proessbar_signal.emit(len(l2),len(l2),2,'词频信息整理中') 
    def compare_excel(self,file1,file2):
        data = xlrd.open_workbook(file1)  #读取数据
        table = data.sheets()[0]                                #打开第一张表
        nrows = table.nrows                                     #获取总行数
        ncols = table.ncols                                       #获取总列数
    # file2 
        data1 = xlrd.open_workbook(file2)  #读取数据
        table1 = data1.sheets()[0]                                #打开第一张表
        nrows1 = table1.nrows                                     #获取总行数
        ncols1 = table1.ncols                                       #获取总列数
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('word')
        word_list_A=[]
        word_list_B=[]

        word_list_A =table.col_values(0)
        word_list_B =table1.col_values(0)

        inBnotA = sorted([i for i in word_list_B if i not in word_list_A], key=str.lower)
        inAnotB = sorted([i for i in word_list_A if i not in word_list_B], key=str.lower)
        inAinB = sorted([i for i in word_list_A if i in word_list_B], key=str.lower)
        ABbingji = []
        ABbingji = inAnotB + inBnotA + inAinB
        ABbingji = sorted(ABbingji, key=str.lower)
        print(inBnotA)
        print(inAnotB)
        print(inAinB)
        indexx = 0
        #表格宽度
        worksheet.col(0).width = 5120
        worksheet.col(1).width = 5120
        worksheet.col(2).width = 5120
        font = xlwt.Font()
        font.bold = True
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        pattern.pattern_fore_colour = 3  #背景颜色

        style4 = xlwt.XFStyle()
        style4.font = font
        style4.pattern = pattern

        worksheet.write(indexx,0,file1+'专有单词',style=style4)
        for aa in inAnotB:
            indexx=indexx+1
            worksheet.write(indexx,0,aa)
        indexx1 = 0
        worksheet.write(indexx1,1,file2+'专有单词',style=style4)
        for bb in inBnotA:
            indexx1=indexx1+1
            worksheet.write(indexx1,1,bb)
        indexx3 = 0
        worksheet.write(indexx3,2,'两文件交集',style=style4)
        for cc in inAinB:
            indexx3=indexx3+1
            worksheet.write(indexx3,2,cc)
        indexx4 = 0
        worksheet.write(indexx4,3,'两文件并集',style=style4)
        all_wd = inAnotB+inBnotA+inAinB
        for dd in all_wd:
            indexx4=indexx4+1
            worksheet.write(indexx4,3,dd)
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
        workbook.save('单词文件对比结果{}.xls'.format(now))
        self.save_compare_file_signal.emit('1') 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    styleFile = './data/blue.dll'
    qssStyle = CommonHelper.readQss(resource_path(styleFile))
    MainWindow.setStyleSheet(qssStyle)
    sys.exit(app.exec_())
    # print(trans('ニ'))