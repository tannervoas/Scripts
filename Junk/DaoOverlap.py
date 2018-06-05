import turtle
t = turtle.Turtle()
s = turtle.Turtle()
f = turtle.Turtle()
daos = [i for i in range(1,1001)]
daos.sort()
daos.reverse()
step = 5
power = []
maxi = max(daos)*step
pi = 3.141519
sum = 0

vals = []
max_v = 0
for i in range(1,maxi+1):
    i = i / step
    t_value = 0
    ddao = 0
    for dao in daos:
        if i <= dao:
            ddao += dao
            t_value += (3*pi/4)*((i**3) - (i-1/step)**3)
        elif i <= daos[0]:
            diff = daos[0] - dao
            loc = (i - dao) / diff
            dao_ = dao * (1 - loc)
            ddao += dao_
            t_value += (3*pi/4)*((i**3) - (i-1/step)**3) * (dao_ / dao)
    sum += ddao*t_value
    vals += [[i,t_value,sum]]
    if t_value > max_v:
        max_v = t_value
    print('{0:>10.4f}: {1:20.6f} * {2:20.6f} = {3:20.6f}'.format(i,t_value/ddao,ddao, t_value))
print('       SUM: {0:20.6f}'.format(sum))
scale = sum / max_v
turtle.setworldcoordinates(0, 0, maxi/step,max_v*1.1)
turtle.speed(0)
turtle.delay(0)
t.speed(0)
s.speed(0)
f.speed(0)
t.up()
t.goto(0,0)
t.down()
t.hideturtle()
t.color('green')
t.width(5)
s.up()
s.goto(0,0)
s.down()
s.hideturtle()
s.color('red')
s.width(5)
f.up()
f.goto(0,0)
f.down()
f.hideturtle()
f.width(1)
for pair in vals:
    #if pair[1] >= pair[2]/scale:
    #    f.color('green')
    #else:
    #    f.color('red')
    #f.up()
    #f.goto(pair[0],pair[1])
    #f.down()
    #f.goto(pair[0],pair[2]/scale)
    t.goto(pair[0],pair[1])
    s.goto(pair[0],pair[2]/scale)
turtle.mainloop()
