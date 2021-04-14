import MySQLdb
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

# 连接数据库
class MysqlSearch(object):
	def __init__(self):
		self.get_conn()
	# 获取连接
	def get_conn(self):
		try:
			self.conn = MySQLdb.connect(
				host='123',
				user='root',
				passwd='',
				db='personnelmanagement',
				charset='utf8'
				)
		except MySQLdb.Error as e:
			print('Error: %s' % e)
	# 关闭连接
	def close_conn(self):
		try:
			if self.conn:
				self.conn.close()
		except MySQLdb.Error as e:
			print('Error: %s' % e)
	def get_userinfo(self):
		sql = 'SELECT * FROM 登陆账户'
        
        # 使用cursor()方法获取操作游标
		cursor = self.conn.cursor()
 
        # 使用execute()方法执行SQL语句
		cursor.execute(sql)
 
        # 使用fetchall()方法获取全部数据
		result = cursor.fetchall()
        
        # 将数据用字典形式存储于result
		result = [dict(zip([k[0] for k in cursor.description],row)) for row in result]
 
		cursor.close()
	
class zhuce(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1, columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        self.label03 = Label(self, text='确认密码')
        self.label03.grid(row=2, column=0)

        v2 = StringVar()  # 确认密码输入
        self.entry03 = Entry(self, textvariable=v2, show='*')
        self.entry03.grid(row=2, column=1, columnspan=2)

        Button(self, text='确定', command=self.login1) \
            .grid(row=3, column=1, padx=10, sticky=NSEW)
        Button(self, text='取消', command=self.cancel) \
            .grid(row=3, column=2, sticky=NSEW)

    def login1(self):
        pass

    def cancel(self):
        pass

class login1(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='数据集')
        self.label01.grid(row=1, column=0)

        v1 = StringVar()  # 数据集名字输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=1, column=1, columnspan=2)

        self.label02 = Label(self, text='算法')
        self.label02.grid(row=2, column=0)

        v2 = StringVar()  # 算法输入
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.grid(row=2, column=1, columnspan=2)

        Button(self, text='开始执行', command=self.login1) \
            .grid(row=4, column=1, padx=10, sticky=NSEW)
        Button(self, text='取消', command=self.cancel) \
            .grid(row=4, column=2, sticky=NSEW)


    def login1(self):
        pass

    def cancel(self):
        pass
        
class Applicantion(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.label01 = Label(self, text='用户名')
        self.label01.grid(row=0, column=0)

        v1 = StringVar()  # 用户名输入
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1,columnspan=2)

        self.label02 = Label(self, text='密码')
        self.label02.grid(row=1, column=0)

        v2 = StringVar()  # 密码输入
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1, columnspan=2)

        # 登录 注册 按钮事件绑定
        Button(self, text='登录', command=self.login)\
            .grid(row=2, column=1, padx=10, sticky=NSEW)
        Button(self, text='注册', command=self.set)\
            .grid(row=2, column=2, sticky=NSEW)

    def login(self):  # 登录事件
        username = self.entry01.get()
        pwd = self.entry02.get()

        if username == '123' and pwd == '123456':
            messagebox.showinfo('登录系统', '登录成功')
            root1 = Tk()
            root1.geometry('400x200+300+400')
            root1.title('实验测试')
            table = login1(master=root1)
            root1.mainloop()
        else:
            messagebox.showinfo('登录系统', '登录失败，用户名或密码错误')

    def set(self):  # 注册事件
        root1 = Tk()
        root1.geometry('400x200+300+400')
        root1.title('注册系统')
        table = zhuce(master=root1)
        root1.mainloop()




if __name__ == '__main__':
    root = Tk()
    
    root.geometry('400x200+300+400')
   
    root.title('D{0-1}KP 实例数据集算法实验平台')
    app = Applicantion(master=root)
    
    root.mainloop()
    
