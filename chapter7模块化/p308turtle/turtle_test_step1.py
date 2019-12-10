import turtle

slowpoke = turtle.Turtle()  #这个乌龟的名字叫slowpoke
slowpoke.shape('turtle')    #形状是乌龟,不加这句话就是一个箭头


slowpoke.forward(100)   #前进100个单位,一般就是像素点
slowpoke.right(90)
slowpoke.forward(100)
slowpoke.right(90)
slowpoke.forward(100)
slowpoke.right(90)
slowpoke.forward(100)
slowpoke.right(90)

turtle.mainloop()   #这行代码见识窗口所做的一切事务,包括点击关闭窗口的按钮,这行代码放在最后
