import tkinter as tk
import clueai
from clueai.classify import Example
def predict(txt):#换成咱的函数
    response = cl.classify(
        model_name='clueai-large',
        task_name='情感分析',
        inputs=[txt],
        examples=[Example('''比之前买不到强太多了，之前还有点贵，现在还不错，整体下来性价比还是很不错的，棒棒哒''', '''正向'''),
                  Example('''原装充电器，正品，包装很好，物流非常快，前天晚上订购，今天中午到货。很满意.''', '''正向'''), Example(
                '''第二次买这个牌子了 其他没的说 就一点 手机下面早就没有耳机孔了 手机壳还留着那个位置感觉很不精致 没诚意 也愧对这个价格''',
                '''负向'''), Example('''自己贴的、效果不错、很喜欢、虽然贵、但是还是蛮不错''', '''正向'''),
                  Example('''商城的速度真是好快啊，昨天下午下单，今天早上就送到了，包装手感都不错，应该是正品。''', '''正向'''),
                  Example('''话筒声小 插上耳机手机还能外放破耳机别买''', '''负向'''),
                  Example('''在这里买的一套，没用几天都用不了了，商城越来越差了''', '''负向'''),
                  Example('''与宣传不符，没信用！''', '''负向'''),
                  Example('''不好，！得快那插头的铜片就掉了?很容易黑，铜的质量差''', '''负向'''),
                  Example('''一般般，做工普通，充电慢，容量小''', '''负向'''),
                  Example('''连猪都会的东西你不会''', '''负向''')],
        labels=["正向", "负向"])

    # print('prediction: {}'.format(
    #     response.classifications))
    return response.classifications
cl = clueai.Client('K3Io6qzMNDreOFr1X2bzG1101110010')
class GUI:
    def __init__(self):
        root = tk.Tk()
        self.txt = ''
        root.title('演示窗口')
        root.geometry("800x400+300+100")
        label_0 = tk.Label(root,
                           text="Welcome to our program!Please enter the sentence you want us to process！")  # 设置标题0
        label_0.pack()

        self.Entry()
        root.mainloop()#防止窗体退出

    def Entry(self):
        def event():
            """按钮事件,获取文本信息"""
            txt = entry00.get()#获取用户的输入
            # print(txt)
            res = predict(txt)#换成咱的函数
            # print(res)
            text.insert("insert",res)#将结果输出给用户
            text.pack()
        def clear():
            text.delete(1.0,"end")
        text = tk.Text()
        entry00 = tk.StringVar()#用于获取用户输入
        entry00.set("请输入您的句子（输入后删除提示信息）：")
        entry0 = tk.Entry( textvariable=entry00,width=80)
        Button0 = tk.Button( text="run program", command=event)#第一个按钮，点击运行情感分析模块
        Button1 = tk.Button(text='clear the textbox below ',command =clear)#第二个按钮，点击清空输出文本框内容
        entry0.pack()
        Button0.pack()
        Button1.pack()

if __name__ == '__main__':
    GUI()

