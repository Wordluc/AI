import math
def arToDiz(b,a): #a -> b
    b['x']=a[0]
    b['y']=a[1]
    return b
def getArToDiz(a):

    return [a['x'],a['y']]

def centre(p,size):
    x=p['x']+size['x']/2
    y=p['y']+size['y']/2
    return {"x":x,"y":y}

def get_angle(p):
    if(p['x']==0):
        return 0
    angle = math.atan(p['y'] / p['x'])  # 0  180
    angle = angle * 180 / math.pi
    if p['x'] < 0 and p['y'] >= 0:
        angle += 180
    elif p['x'] < 0 and p['y'] <= 0:
        angle -= 180
    return angle


def norm_angle(angle):
    if(angle>180):
        angle=-360+angle
    elif (angle<-180):
        angle=360+angle
    return angle

print(norm_angle(-190))
