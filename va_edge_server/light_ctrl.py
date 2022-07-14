from yeelight import discover_bulbs,Bulb

def getBulb():
    #bulbAddr=None
    #for device in discover_bulbs():
    #    if device['capabilities']['model'] == 'color8':
    #        bulbAddr=device['ip']
    #        print(device['capabilities']['model'],device['ip'])
#
    #bulb = Bulb(bulbAddr)
    bulb = Bulb('your_bulb_addr')
    return bulb