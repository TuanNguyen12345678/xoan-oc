import turtle
    
t = turtle.Turtle()
t.speed(10)
# bán kính ban đầu
r = 10  
# Vòng lặp để in hình tròn xoắn ốc
for i in range(100):
    t.circle(r + i, 20)
turtle.done()