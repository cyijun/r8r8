from light_ctrl import getBulb
from yeelight import Bulb
import re

colors = {
    '红': (255, 0, 0),
    '橙红': (255, 69, 0),
    '橙': (255, 97, 0),
    '橙黄': (255, 128, 0),
    '黄': (255, 255, 0),
    '黄绿': (127, 255, 0),
    '绿': (0, 255, 0),
    '青': (0, 255, 255),
    '蓝': (0, 0, 255),
    '蓝紫': (106, 90, 205),
    '紫': (160, 32, 240),
    '紫红': (255, 0, 255),
    '暖白':(255,248,220),
    '白':(255,255,255),
}

bulb=getBulb()

def dealWithCommand(cmd):
    numList=re.findall(r"\d+\.?\d*",cmd)
    if len(numList)!=0:
        target=int(numList[0])
        if target>=0 and target<=100:
            bulb.set_brightness(target)
    else:
        if cmd.find('开')!=-1:
            bulb.turn_on()
        elif cmd.find('关')!=-1 or cmd.find('零')!=-1:
            bulb.turn_off()
        else:
            matched=[]
            for (key,value) in colors.items():
                if cmd.find(key) !=-1:
                    matched.append(key)
                    
            if len(matched)>0:
                maxindex=0
                maxlen=0
                for index,mkey in enumerate(matched):
                    if len(mkey)>maxlen:
                        maxindex=index
                        maxlen=len(mkey)
                
                r,g,b=colors[matched[maxindex]]
                bulb.turn_on()
                bulb.set_rgb(r, g, b)
                    
