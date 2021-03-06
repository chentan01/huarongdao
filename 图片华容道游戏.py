# -*- coding: utf-8 -*-

"""
PyQt5 tutorial

In this example, we create three toggle buttons.
They will control the background color of a
QFrame.

author: py40.com
last edited: 2017年3月
"""
import sys
import sys
import random
from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class home(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background2.jpg')))
        self.setPalette(palette1)

    def initUI(self):

        self.col = QColor(0, 0, 0)

        startb = QPushButton('开始游戏', self)#开始游戏按钮
        startb.setGeometry(325,400,200,100)
        startb.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        startb.setCheckable(True)#通过setcheckable得到一个tagglebutton
        # startb.move(360, 400)
    #通过ckicked连接到用户自己定义的一个函数setm
        startb.clicked[bool].connect(self.setm1)

        greenb = QPushButton('排行榜', self)
        greenb.setGeometry(325, 550, 200, 100)
        greenb.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        greenb.setCheckable(True)
        # greenb.move(360, 460)

        greenb.clicked[bool].connect(self.setm2)

        blueb = QPushButton('退出游戏', self)
        blueb.setGeometry(325, 700, 200, 100)
        blueb.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        blueb.setCheckable(True)
        # blueb.move(360, 510)

        blueb.clicked[bool].connect(self.setm3)

        # self.square = QFrame(self)
        # self.square.setGeometry(450, 60, 300, 300)
        # self.square.setStyleSheet("QWidget { background-color: %s }" %
        #                           self.col.name())
        self.setGeometry(900, 900, 850, 900)
        self.center()
        self.setWindowTitle('走进柯学！')
        self.show()


    def setm1(self):#setm1就是打开游戏的关联
        self.close()
        self.start = NumberHuaRong()
        self.start.show

    def setm2(self):#历史得分
        self.close()
        self.score = grade()
        self.score.show

    def setm3(self):
        self.close()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #
    # def setm(self, pressed):
    #
    #     source = self.sender()
    #
    #     if pressed:
    #         val = 255
    #     else:
    #         val = 0
    #
    #     if source.text() == "开始游戏":
    #         self.col.setRed(val)
    #     elif source.text() == "排行榜":
    #         self.col.setGreen(val)
    #     else:
    #         self.col.setBlue(val)
    #
    #     self.square.setStyleSheet("QFrame { background-color: %s }" %
    #                               self.col.name())


class Direction(IntEnum):
    # 用枚举类表示方向

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class grade(QMainWindow):
    def __init__(self, parent=None):
        super(grade, self).__init__(parent)
        self.resize(600, 600)
        self.setWindowTitle('历史得分')

        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(192, 253, 123))
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background4.jpg')))
        self.setPalette(palette1)
        self.label = QLabel(self)

        self.label.setGeometry(200, 0, 400, 200)
        self.label.setText("历史得分")
        self.setStyleSheet("QLabel{color:rgb(0,205,205,255);font-size:50px;font-weight:bold;font-family:Arial;}")

        self.label = QLabel(self)
        self.label.setGeometry(270, 50, 300, 300)
        with open("score.txt", "r", encoding="utf-8") as fp:
            scores = fp.readlines()
            ls = []  # 只保留前15个记录
            for score in scores:
                ls.append(int(score.replace('\n', '')))
            ls = sorted(ls)
            finalstr = ' 步数\n'
            if len(ls) >= 15:
                for i in range(15):
                    if i < 9:
                        finalstr += (str(i + 1) + '.' + "  " + str(ls[i]) + '\n')
                    else:
                        finalstr += (str(i + 1) + '.' + " " + str(ls[i]) + '\n')
            else:
                for i in range(len(ls)):
                    if i < 9:
                        finalstr += (str(i + 1) + '.' + "  " + str(ls[i]) + '\n')
                    else:
                        finalstr += (str(i + 1) + '.' + " " + str(ls[i]) + '\n')
            self.label.setText(finalstr)
            self.label.setStyleSheet("QLabel{color:rgb(0,0,0,255);font-size:20px;font-weight:bold;font-family:楷体;}")

        self.button3 = QPushButton('返回home', self)
        self.button3.setGeometry(50, 450, 150, 100)
        self.button3.setStyleSheet("QPushButton{color:black}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:rgb(78,255,255)}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:10px}"
                                   "QPushButton{padding:2px 4px}")
        self.button3.clicked.connect(self.comeback)

        self.button5 = QPushButton('再试一次', self)
        self.button5.setGeometry(405, 450, 150, 100)
        self.button5.setStyleSheet("QPushButton{color:black}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:rgb(78,255,255)}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:10px}"
                                   "QPushButton{padding:2px 4px}")
        self.button5.clicked.connect(self.playagain)

    def comeback(self):
        self.hide()
        self.f = home()
        self.f.show()

    def playagain(self):
        self.close()
        self.s = NumberHuaRong()
        self.s.show()






class NumberHuaRong(QWidget):
    """ 华容道主体 """
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.zero_row = 0
        self.zero_column = 0
        self.gltMain = QGridLayout()
        self.initUI()

    def initUI(self):
        # 设置方块间隔
        self.onInit()
        self.gltMain.setSpacing(4)
        self.gltMain.setContentsMargins(0,0,0,0)
        # 设置布局
        self.setLayout(self.gltMain)
        # 设置宽和高
        self.setFixedSize(700, 700)
        # 设置标题
        self.setWindowTitle('图片华容道')
        # 设置背景颜色
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255,132,139))
        # palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background4.jpg')))
        self.setPalette(palette1)
        self.show()

    # 初始化布局
    def onInit(self):
        # 产生顺序数组
        self.point = 0
        # arr = range(1,10)
        # self.numbers = random.sample(arr, 8)
        # self.numbers.append(0)
        # print(self.numbers)
        self.numbers =[5, 8, 3, 4, 9, 2, 0, 7, 1]
        #self.numbers = list(range(1,9))
        # self.numbers = list()
        # self.numbers.append(4)
        # self.numbers.append(9)
        # self.numbers.append(6)
        # self.numbers.append(8)
        # self.numbers.append(1)
        # self.numbers.append(7)
        # self.numbers.append(0)
        # self.numbers.append(5)
        # self.numbers.append(3)

        # 将数字添加到二维数组
        for row in range(3):
            self.blocks.append([])
            for column in range(3):
                temp = self.numbers[row * 3 + column]

                if temp == 0:
                    self.zero_row = row
                    self.zero_column = column
                self.blocks[row].append(temp)

        # # 打乱数组
        # for i in range(500):
        #     random_num = random.randint(0, 3)
        #     self.move(Direction(random_num))

        self.updatePanel()

    # 检测按键
    def keyPressEvent(self, event):
        key = event.key()
        if(key == Qt.Key_Up or key == Qt.Key_W):
            self.move(Direction.UP)
        if(key == Qt.Key_Down or key == Qt.Key_S):
            self.move(Direction.DOWN)
        if(key == Qt.Key_Left or key == Qt.Key_A):
            self.move(Direction.LEFT)
        if(key == Qt.Key_Right or key == Qt.Key_D):
            self.move(Direction.RIGHT)
        self.updatePanel()
        if self.checkResult():
            if QMessageBox.Ok == QMessageBox.information(self, '挑战结果', '恭喜您完成挑战！'):
                self.onInit()

    # 方块移动算法
    def move(self, direction):
        if(direction == Direction.DOWN): # 上
            if self.zero_row != 2:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row + 1][self.zero_column]
                self.blocks[self.zero_row + 1][self.zero_column] = 0
                self.zero_row += 1
        if(direction == Direction.UP): # 下
            if self.zero_row != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row - 1][self.zero_column]
                self.blocks[self.zero_row - 1][self.zero_column] = 0
                self.zero_row -= 1
        if(direction == Direction.RIGHT): # 左
            if self.zero_column != 2:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column + 1]
                self.blocks[self.zero_row][self.zero_column + 1] = 0
                self.zero_column += 1
        if(direction == Direction.LEFT):   # 右
            if self.zero_column != 0:
                self.blocks[self.zero_row][self.zero_column] = self.blocks[self.zero_row][self.zero_column - 1]
                self.blocks[self.zero_row][self.zero_column - 1] = 0
                self.zero_column -= 1

    def updatePanel(self):
        for row in range(3):
            for column in range(3):
                self.gltMain.addWidget(Block(self.blocks[row][column]), row, column)

        self.setLayout(self.gltMain)

    # 检测是否完成
    def checkResult(self):
        # 先检测最右下角是否为0
        if self.blocks[2][2] != 0:
            return False

        for row in range(3):
            for column in range(3):
                # 运行到此处说名最右下角已经为0，pass即可
                if row == 2 and column == 2:
                    pass
                # 值是否对应
                elif self.blocks[row][column] != row * 3 + column + 1:
                    return False

        return True


class Block(QLabel):

    """ 数字方块 """

    def __init__(self, number):
        super().__init__()

        self.number = number
        self.setFixedSize(200, 200)

        # 设置字体
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.setFont(font)

        # 设置字体颜色
        pa = QPalette()
        pa.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pa)
        # 设置文字位置
        self.setAlignment(Qt.AlignCenter)
        # 设置背景颜色\圆角和文本内容
        if self.number == 0:
            self.setStyleSheet("background-color:white") # border-image:url(./bc.gif);
        # if self.number == 2:
        #     self.setStyleSheet("border - image: url(./2.png);background-color:white")
        # if self.number == 3:
        #     self.setStyleSheet("border - image: url(./3.png);background-color:white")
        # if self.number == 4:
        #     self.setStyleSheet("border - image: url(./4.png);background-color:white")
        # if self.number == 5:
        #     self.setStyleSheet("border - image: url(./5.png);background-color:white")
        # if self.number == 6:
        #     self.setStyleSheet("border - image: url(./6.png);background-color:white")
        # if self.number == 7:
        #     self.setStyleSheet("border - image: url(./7.png);background-color:white")
        # if self.number == 8:
        #     self.setStyleSheet("border - image: url(./8.png);background-color:white")
        # if self.number == 9:
        #     self.setStyleSheet("border - image: url(./9.png);background-color:white")
        else:
            # self.setStyleSheet("background-color:red")
            # self.setText(str(self.number))
            if self.number == 1:
                self.setStyleSheet("border-image:url(./1.jpg);background-color:white")
            if self.number == 2:
                self.setStyleSheet("border-image:url(./2.jpg);background-color:white")
            if self.number == 3:
                self.setStyleSheet("border-image:url(./3.jpg);background-color:white")
            if self.number == 4:
                self.setStyleSheet("border-image:url(./4.jpg);background-color:white")
            if self.number == 5:
                self.setStyleSheet("border-image:url(./5.jpg);background-color:white")
            if self.number == 6:
                self.setStyleSheet("border-image:url(./6.jpg);background-color:white")
            if self.number == 7:
                self.setStyleSheet("border-image:url(./7.jpg);background-color:white")
            if self.number == 8:
                self.setStyleSheet("border-image:url(./8.jpg);background-color:white")
            if self.number == 9:
                self.setStyleSheet("border-image:url(./9.jpg);background-color:white")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hom= home()
    hom.show()
    sys.exit(app.exec_())
