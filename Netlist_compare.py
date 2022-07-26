# main file
from tkinter import *

import time

Netlist_Type = [('REL share NET',1),
        ('Allegro Export (.txt)',2)]

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("Netlist Compare Check Tool")           #窗口名
        self.init_window_name.geometry('640x320+200+200')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        #self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_Open_Netlist_1_button = Button(self.init_window_name, text="Netlist 1", bg="lightblue", width=12,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_Open_Netlist_1_button.grid(row=1, column=0)
        self.str_Open_Netlist_2_button = Button(self.init_window_name, text="Netlist 2", bg="lightblue", width=12,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_Open_Netlist_2_button.grid(row=2, column=0,)
        self.str_Do_Check_button = Button(self.init_window_name, text="Check", bg="lightblue", width=24,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_Do_Check_button.grid(row=3, column=0)
        #单选框
        # IntVar() 用于处理整数类型的变量
        v1 = IntVar()
        v2 = IntVar()
        # 根据单选按钮的 value 值来选择相应的选项
        v1.set(0)
        v1.set(0)
        # 使用 variable 参数来关联 IntVar() 的变量 v
        num = 0
        for name, num in Netlist_Type:
            radio_button = Radiobutton (self.init_window_name,text = name, variable = v1,value =num).grid(row=1, column=num+1)
            num = num + 1
        num = 0
        for name, num in Netlist_Type:
            radio_button = Radiobutton (self.init_window_name,text = name, variable = v2,value =num).grid(row=2, column=num+1)
            num = num + 1
    #功能函数
    def str_trans_to_md5(self):
        return 0


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()