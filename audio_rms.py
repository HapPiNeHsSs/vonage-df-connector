import struct, math


SHORT_NORMALIZE = (1.0/32768.0)
swidth = 2

def rms(frame): #Root mean Square: a function to check if the audio is silent. Commonly used in Audio stuff
    count = len(frame) / swidth
    format = "%dh" % (count) 
    shorts = struct.unpack(format, frame) #unpack a frame into individual Decimal Value
    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE #get the level of a sample and normalize it a bit (increase levels)
        sum_squares += n * n #get square of level
    rms = math.pow(sum_squares / count, 0.5) #summ all levels and get mean
    return rms * 1000 #raise value a bit so it's easy to read 

def ding(): #a binary representation of a Ding sound. so we are self contained. 
    # Technically we can just load a file and return the bytes via wave
    # wv = wave.open("ding.wav", mode="rb")
    # return wv.readframes(100000)
    
    return b'\xab\x0b\xcf\x06\x9b\x04T\x02]\x02\xaa\x00\xf8\xfe\xce\xfe\x87\xfe\xf1\xfd\xa6\xfd\xb0\xfe\xfe\xfe\xb1\xff\xeb\xff\xd0\x00\xfa\x00\xac\x01\x9d\x01\x8a\x01\xc1\x00b\x00@\x00\xe8\xfe\xff\xfd\x07\xfd\xdb\xfc?\xfd\xa0\xfc\x83\xfc\x1f\xfdq\xfd7\xfd\xb4\xfe\xea' + \
        b'\x00\xfd\x01\x95\x026\x03\x1b\x02T\x02c\x02T\x02e\x01J\x01\xa0\xff\x1d\xfd\x1f\xfcf\xfa\r\xfb1\xfbJ\xfb\xaa\xfa\x9d\xfb_\xfc+\xfe\xeb\xfd\x81\xff\xd3\x00\xd7\x03\xcd\x03\xd3\x04u\x04]\x03C\x03\xa8\x01r\x02\x16\x00d\x01\x0c\xfe\xf4\xfe"\xfa\xb6\xfc\x9f\xf8H' + \
        b'\xfdE\xfb\xad\xf7!\x10\x01!02\xf4,@\x1fz\x10\x0e\x11/\xfd\xe7\x03W\xf1\x15\xf3\x84\xe2\xc0\xeb\x98\xed\x86\xf0\x7f\xe5r\xea\xda\xfe\xeb\xff?\xfcZ\xfa\x1c\x06\x81\x05\x80\xfc\xf9\xfbD\x04\xd1\x08q\x0b`\x0b\x81\r\x13\x0e9\r$\rH\x02\x1b\x08\xed\n\x95\x0e\x9c\x06' + \
        b'\xb2\xfdB\xfc\x01\xfcm\xf1\xc7\xf3\x9e\xf8\xf3\xfe\x9a\xf7\x0e\xf8`\xfc\x9a\xff\x81\xf6,\xf7*\xf9\xea\xfd\xc3\xfb\xd0\xff\x82\xfe\x0b\xfc\xa1\xfa\n\xf9\x18\xfd\xbe\xf7\xc3\x00\xb9\x02\x89\x06g\x02\x7f\x03\xcb\x06\x11\x06\x81\x01y\x05\xbd\x07=\x08y\x06\xfb\x04\xae' + \
        b'\x07\x89\xfeV\x01"\xffQ\x01A\xfc.\xfd\xa3\xfe\xba\xfb\xe8\xf6\xea\xf9\xef\xfb\x15\xf8\xfa\xf7\n\xf9$\xfdG\xf5\xd4\xf7y\xf9\xbc\xfd\x91\xf8>\xfc\x8c\x01\x9e\x00\xc3\xfe\xd5\xffC\x05\x82\x02G\x03V\x04\xf9\t\xaa\x03#\x06y\x05\xd5\x07\xbd\x03\xce\x04?\x07-\x05\xca\x02'+ \
        b'\xee\x022\x048\x00\xd3\xff\xc1\xff\xa0\x01V\xfd\x8d\xfe~\xfeA\xfd\xe2\xf9j\xfa\xbf\xfa4\xf8\x0f\xf7\x0f\xf8\xc9\xf90\xf7\xc6\xf8\xab\xfb\xcc\xfd\x12\xfd\\\xff\x9a\x02v\x02\x87\x01\xb2\x04\x8c\x07\x9e\x04\x12\x04\x89\x05t\x08>\x03\xf7\x02\xbf\x04q\x05\xf6\x02Y\x03\xb0'+ \
        b'\x04\xee\x02\x0b\xff\xd8\x00\x1f\x03\xb8\xff\x99\x00\x0c\x01\xd2\x01|\xfb\xc3\xf9\xdb\xfcO\xfb\xfb\xf5\x0e\xf6\xbc\xf8K\xf8\x89\xf6R\xf7J\xfc\xb1\xf8P\xfb\x9f\xfer\x02K\xff\xd5\x00X\x04a\x05\x15\x02\xc3\x04w\x07,\x06\xa9\x02\xda\x04\xdc\x06S\x05\xee\x04]\x07\xdf\x06\x88' + \
        b'\x03?\x02(\x05\x88\x02{\xff\xb5\x00l\x02\x88\x00\xad\xfb\t\xfc.\xfd\xc8\xf8k\xf7\xf4\xf7\xf4\xf7\xe7\xf5\xed\xf4\xec\xf7\x07\xf7\x14\xf5\xf1\xf9\xba\xfc\xfb\xfc\xde\xfb\x82\xffR\x02\xad\xff\xbb\xff}\x05w\x06\xc6\x04\x98\x04\xd8\x07!\x08\x93\x04\xab\x06\xa2\x08%\x07\x7f' + \
        b'\x04J\x06\xe5\x06\xae\x034\x01\xe3\x02\x83\x02O\xfe\x9d\xfde\xff\xd4\xfd>\xf9D\xfa\x08\xfb\xc8\xf9\xc5\xf4]\xf7G\xf8\xdc\xf5a\xf5>\xf9\xf5\xfbJ\xfa@\xfb\x8f\xfe[\xff\xe6\xfbH\x00\xe4\x02\x86\x04\x98\x02\xa0\x05\x8b\x07\xdc\x05V\x04\xe3\x07\x1a\x07\xb5\x06\x1e\x06\xbe\t\xd6' + \
        b'\x06v\x04\x1f\x03\xa0\x05\xbf\x006\xffk\x00\xec\x01\x00\xfe\x86\xfa\xfe\xfbb\xfb\x9d\xf8\xa8\xf6\xc4\xf9\x07\xf7\xbf\xf6_\xf6S\xf9\x17\xf7\xd6\xf6g\xfbs\xfd_\xfcw\xfc$\x02\x80\x01\xa8\x01L\x00\xf8\x07\x83\x05r\x06\xd2\x06D\n\xde\x06\xc5\x05\x17\x07\x1c\t%\x05W\x04r\x06\xe4' + \
        b'\x04@\x00r\xff\xa2\x01\xbd\x00\xc4\xfcx\xfd\x95\xfe\xdd\xfbj\xf8H\xfa\xdd\xf8\x93\xf6x\xf4\x8d\xf9W\xf8\x14\xf6\xfb\xf4\xea\xfa\xce\xf9\r\xfa\x1b\xfc\x01\x01\xb1\x00&\xff\'\x03\x95\x05+\x05\x8f\x04\xf6\x07\x02\x08y\x06,\x06\xa8\t\xec\x07\x13\x05E\x06\xba\x07f\x06_\x02u\x03' + \
        b'\x9d\x02\xdb\xff\xf2\xfc\xfb\xff\xdd\xfd\x87\xfbu\xf9~\xfcl\xfb\xeb\xf8S\xf9\x86\xfb\xf2\xf8\xce\xf6\xae\xf7;\xf9k\xf7\xa4\xf7\xd3\xfa\xb1\xfd\x86\xfc\x16\xff\xe0\x02P\x03\xd8\x02\x12\x05\xaf\x08\xf4\x06\t\x05e\x06j\x08w\x05,\x05N\x07\x03\x08\x9c\x04Q\x03\xa6\x04>\x03\x8c' + \
        b'\xff\xb7\xff\xae\x00\xac\xfe\xdd\xfb\xcc\xfc!\xfd\x98\xf9\x98\xf7\x9d\xf9C\xfa\xe2\xf7L\xf7\xe1\xf9\x9a\xf9n\xf7\xf7\xf8\xab\xfc\x07\xfd\xa9\xfc\x7f\xff\x94\x02\xca\x01\xc6\x00\xbc\x03u\x05\x10\x041\x04t\x07x\x07\x10\x06\xd4\x05\xec\x08\x0f\x07!\x05\x8b\x05{\x075\x04n\x01p' + \
        b'\x02x\x01\xd3\xff\x97\xfb\x81\xff\xae\xfb\x90\xfb\x8d\xf77\xfcm\xf7#\xf8\x12\xf7\x18\xfbN\xf8\xfe\xf6\x85\xf9\n\xfbK\xfc\x08\xfb\xfd\x00w\xff[\x01\xa1\xffv\x057\x03\xa3\x03\x86\x03,\x06\xd7\x04\x8d\x02\x98\x05!\x05\xa5\x06w\x03\xe0\x08*\x06 \x07>\x03\x17\x06e\x02\xe6\x01\x89' + \
        b'\x00#\x01\xd3\xfd\xbf\xfb\x81\xfc\xd7\xfb"\xf9\x8f\xf7\x82\xf9>\xf9\xce\xf70\xf8\xa0\xfa\x96\xfar\xf9\x80\xfb\xc8\xfd\x1b\xfe\xb2\xfdq\x00q\x01\xb0\x01\xa0\x01\x95\x04F\x04a\x03\x07\x04h\x06P\x05k\x04\x82\x05\x04\x08\xe2\x06\xff\x057\x06q\x06I\x03\x84\x02\x08\x021\x01a\xfe#' + \
        b'\xfe\xcb\xfe\xab\xfch\xfa\xae\xf9{\xfa\x0f\xf8\xb1\xf8_\xf9\xd1\xfa\xc3\xf7\xcd\xf8\x96\xfa]\xfb3\xfa\xd6\xfb+\x00\xc8\xffs\x00_\x00\x1d\x05R\x02A\x04p\x03\x11\x07\xc9\x03:\x05\x99\x05G\x07@\x05\xfd\x05W\x07\xe2\x06\xe9\x05\x8d\x05\x9e\x05\xad\x02\x81\x00\xb1\x00\x1d\x00' + \
        b'\x8c\xfdg\xfc\x06\xfd\x18\xfc\xeb\xf9\x8e\xf9\x1b\xfb\x1e\xf9\x02\xf7\x8e\xf7\xfd\xf9\xcf\xf8\'\xf8\x9d\xf9\xb6\xfc{\xfc\xd3\xfc\xe1\xff\x1a\x01\xab\x01\x9a\x01\x8e\x05e\x05\xbb\x05\xda\x04\x82\x07\x91\x05\x86\x05\xef\x05\x08\x08\xf7\x060\x06\x0f\x07\xea\x06\xbd\x04\xa2\x02' + \
        b'\xaf\x02\xe7\x00t\xffN\xfe\xcc\xfe\x87\xfc\xa9\xfa\xbb\xfa\xbe\xfa\x0c\xf93\xf8(\xfa\x87\xfa/\xf9\r\xf8\xeb\xfaW\xfb8\xfb\xeb\xfb\xf3\xfe\xc1\xff\x8c\xff\xd0\x00\x17\x03\x82\x02s\x01\xdc\x02c\x04,\x04\x8a\x03$\x05\xa5\x06\x92\x06\x9c\x06\x8d\x076\x07\x91\x06+\x06j\x05\xff' + \
        b'\x02\x84\x019\x01{\x00S\xfd\x02\xfdz\xfd\xad\xfc\xb4\xf9}\xf9!\xfb~\xfa\x93\xf8\x85\xf8~\xfa\xa7\xf9\xc6\xf9\x82\xfaV\xfd\xe8\xfcT\xfeV\x00\xf0\x01\x15\x01R\x02\x08\x04\xff\x04$\x03\xf2\x03\x12\x05o\x05\t\x04\x81\x05\x00\x06z\x06\x8c\x05{\x06\xbf\x05*\x04\xff\x02\xfa\x02N' + \
        b'\x01\x8e\xff \xffD\xffV\xfd\x9a\xfb]\xfc\x80\xfcp\xfa\x88\xf9(\xfa\x8e\xfa@\xf9\x06\xf9/\xfb\xc2\xfb\xb7\xfa\xc0\xfc\xe4\xfeH\xff\x87\xfe\xae\xff\xd3\x01\x96\x02\xe8\x01\xbb\x03\xa0\x04\xbb\x04r\x04f\x06\x17\x06\xbc\x06\xa7\x06G\x08\xc6\x06\x88\x06}\x05\x8d\x05\x90\x02\xe6' + \
        b'\x00\xc4\x00\x0e\x00\xee\xfcM\xfcT\xfcZ\xfb\x84\xf9\x11\xf9\x1c\xfa.\xfa\x9e\xf8\xe1\xf9\x17\xfb-\xfa\xe1\xf9~\xfc\xb7\xfdt\xfe\x0e\xfeI\x00f\x01B\x01U\x01\x8c\x03\x08\x04\x8c\x03\xc2\x04u\x05\x92\x05\r\x057\x06\xf2\x05\xe7\x06\x8f\x05\x19\x07P\x05\xd4\x03\x89\x02\xab\x03' + \
        b'\xdb\x00\xcf\xff\x17\xff;\xff\xcb\xfd\\\xfc\x8a\xfb\x15\xfc\xe3\xf9\xae\xf8\xa0\xf9\xb4\xf9\xf7\xf8\xf7\xf9\xa1\xfak\xfb\xba\xfb\xfd\xfc\xaa\xfe\x93\xff\xea\xfe\x10\x01r\x024\x02\xd5\x02N\x04\x1f\x05E\x05t\x05\xd1\x05\x8b\x06\xe2\x05\xee\x05v\x06\xe0\x05\xca\x04L\x05\xbf' + \
        b'\x03Q\x02\x85\x01I\x01\xdb\xff\xda\xfeF\xfdY\xfdg\xfc1\xfaO\xfa\xc9\xfan\xf9\x95\xf9\x02\xfa\x15\xfal\xfa#\xfaE\xfb\xff\xfcO\xfd\xe4\xfd;\x00[\x00\xaa\x017\x02s\x03\x0b\x03\xbe\x04\xd5\x043\x06\xc9\x05\xc5\x05B\x06\x1c\x07\x96\x05\t\x06\xee\x05\x95\x040\x04[\x03\xcb\x01\xcb' + \
        b'\x00H\xff\xbf\xfe\x13\xff\xc6\xfc\xda\xfb\x07\xfc\xf1\xfa4\xfac\xfa\x9b\xf9\x15\xfa\xb2\xf9E\xfa\xec\xfa\xb5\xfb\x9e\xfb\x07\xfev\xfe\x03\xff\xc1\xff\xc4\x01\x8e\x01\xef\x02\xdc\x02\xcc\x04\xd9\x04&\x05%\x04\xee\x05\xb1\x04\xb0\x05*\x06O\x06\x1c\x05\x95\x05\xf5\x03>\x04\x17' + \
        b'\x02a\x01\xcb\x00.\x00\xc2\xfd\x02\xfe\xe6\xfc\xf4\xfb\xd3\xfa`\xfa%\xfah\xfa\xe2\xf9"\xfa\x98\xfan\xfaN\xfb\xba\xfcp\xfd\xb3\xfdz\xff\xdf\xff\x06\x01\xa7\x01h\x02o\x03\xee\x03\x98\x03\n\x05_\x05\x00\x05\x8f\x05\x8d\x05O\x05\xaf\x05g\x05\xfa\x043\x04d\x02\x18\x02\xc1\x01s' + \
        b'\x00\x83\xffb\xff\xed\xfdE\xfd\x14\xfc\xc2\xfb\x19\xfb\xba\xfa\xbd\xf9;\xfa\xd8\xf9\x1c\xfa\xf9\xfa\xce\xfb\x9f\xfb\xf1\xfc\xfa\xfdA\xffa\x00\xcd\x00\x91\x01i\x02^\x02^\x03,\x04\\\x04\x81\x04k\x05\xf2\x04}\x05\xff\x04I\x05\x0e\x05\xc9\x04I\x04c\x04\x06\x03\xa5\x01\xee\x00C' + \
        b'\x00<\xff\x03\xfe]\xfd\xa4\xfc:\xfc{\xfb%\xfb\xfa\xfa\x7f\xfah\xfa\x06\xfb\xe4\xfa{\xfb^\xfc\xf3\xfcU\xfd\xfe\xfd\x95\xfe\xff\xff=\x00\xdd\x00\xaa\x01\xb8\x02F\x03[\x04\xdb\x04\xd3\x04\x08\x05\n\x05i\x05F\x054\x05\xa0\x04d\x04\x1b\x03\xd4\x02c\x02\x8b\x01X\x00\xca\xff*\xffg' + \
        b'\xfee\xfd\xa7\xfch\xfc\xe0\xfb\x18\xfb\xe9\xfa\xb0\xfav\xfa\x83\xfa\xb7\xfa\xf3\xfa\xb2\xfb\xac\xfc\xfd\xfd\xc6\xfe\xaa\xffS\x00\x02\x01\x8a\x01\'\x02s\x03\x04\x04O\x04\xe8\x04 \x05\t\x05\x05\x05\xee\x04>\x05\xd8\x04T\x04+\x04\xc1\x03\x83\x02\xb9\x01\xe2\x00\x1e\x00\x18' + \
        b'\xff"\xfem\xfd\x05\xfdh\xfc\x1f\xfc\x9b\xfb\xe2\xfa\xc5\xfa\xd9\xfa\xd9\xfa\x99\xfa\xed\xfa\xd2\xfbl\xfc\xd7\xfc\xc2\xfd\xd8\xfe\xc6\xffW\x00+\x01*\x02\xa6\x02\x8b\x03t\x04*\x05\'\x05T\x05\x9e\x05\xb5\x05Y\x05,\x05\xbc\x04\x12\x04\x08\x03\xac\x02\xf1\x01\xf5\x00\xd6\xffN' + \
        b'\xff\x98\xfe\xbf\xfd\x16\xfd\xbd\xfc\x1f\xfcw\xfb\x12\xfb$\xfb\x17\xfb\xc4\xfa\x13\xfbV\xfbg\xfb\x13\xfc\xff\xfc\xf8\xfd\xb4\xfe~\xff\x81\x00m\x01\xa3\x01\x81\x02l\x03\x12\x04d\x04\xff\x04\xfd\x04\xf7\x04\xc2\x04\xf0\x04%\x05\xaf\x04.\x04\xe5\x03\x05\x03\x15\x02b\x01\xb8' + \
        b'\x00\xb8\xff\x9d\xfe\xcc\xfdP\xfd\x93\xfc\xff\xfb\xdb\xfb\xc8\xfb7\xfb\r\xfb\xf4\xfa\xf0\xfa\x05\xfb{\xfb,\xfc\xf9\xfcZ\xfdj\xfeF\xff\xca\xff^\x007\x01\xf8\x01\xc0\x02N\x03)\x04\x87\x04\x8b\x04\xa9\x04\x0c\x05\xec\x04\xef\x04\xde\x04\xaa\x04\xf9\x03\x13\x03e\x02\xed\x01' + \
        b'\xd5\x00\x08\x00M\xff\x87\xfe\xc0\xfd4\xfd\xbf\xfcA\xfc\xc0\xfb\xb7\xfb\x92\xfbR\xfb\xed\xfa:\xfb\x9c\xfb\xe7\xfbj\xfc[\xfd\xe6\xfd\xb3\xfeC\xff\x15\x00\xdb\x00P\x01"\x02\xe1\x028\x03\xba\x03=\x04`\x04~\x04{\x04\xcf\x04\xf0\x04\x95\x04L\x04\xe5\x03"\x03^\x02\xd1\x01\x1a' + \
        b'\x01;\x00\x12\xff]\xfe\x86\xfd\xc7\xfc@\xfc\xee\xfb\x85\xfb\x1a\xfb\xfe\xfaI\xfbO\xfb\\\xfb\xee\xfbt\xfc/\xfd\xb1\xfdv\xfe(\xff\xa4\xffM\x00 \x01\x8b\x01\'\x02\xbe\x02c\x03\xae\x03\xab\x03\x11\x04v\x04f\x04\x87\x04\x88\x04O\x04\xdf\x03>\x03\xd3\x02I\x02P\x01\x8a\x00\xc0' + \
        b'\xff\xb4\xfe\x15\xfe\x94\xfd\x04\xfd\x8c\xfc\x01\xfc\xd6\xfb\x92\xfb\x19\xfb\x0f\xfb[\xfb_\xfb\xb1\xfbQ\xfcS\xfd\xf9\xfd\xa5\xfeJ\xff4\x00\xda\x00\x99\x01[\x02\x18\x03O\x03\xdb\x03+\x046\x04F\x04\x82\x04\xa1\x04\xab\x04V\x041\x04\xcf\x03\xdf\x02(\x02\x98\x01\xbb\x00\xbb' + \
        b'\xff\xe3\xfe:\xfe\x95\xfd\xcf\xfcU\xfc\xfc\xfb\x8a\xfb0\xfb!\xfb\x10\xfb\xfe\xfa+\xfb\xde\xfbe\xfc\xdc\xfc\x95\xfdT\xfe\x01\xff\x9b\xffk\x00i\x01\x16\x02\x99\x02e\x03\xea\x03?\x04~\x04\xb5\x04\xa8\x04\x9b\x04\x92\x04\xb3\x046\x04|\x03\xf4\x02k\x02\xa6\x01\xe2\x00@\x00' + \
        b'\x98\xff\xb7\xfe\xe4\xfd]\xfd\xb3\xfc\x17\xfc\xaf\xfbz\xfb2\xfb\xf3\xfa\xf4\xfa1\xfbY\xfb\xec\xfb\xc5\xfc\x86\xfd\x1f\xfe\xdd\xfe\xd1\xff\xa0\x002\x01\xc1\x01\x7f\x02\xda\x02:\x03\xad\x03\x0c\x04\x07\x04\x10\x04D\x04z\x04[\x043\x04\x02\x04\x9f\x03\xe6\x02N\x02\xbb\x01' + \
        b'\xe2\x00\xf2\xff1\xffX\xfel\xfd\xab\xfcF\xfc\xe5\xfbT\xfb\x03\xfb\x1f\xfb\x13\xfb\x0c\xfb[\xfb\x13\xfc\x91\xfc\x07\xfd\xbb\xfd\x97\xfe;\xff\xbd\xffn\x00/\x01\xce\x01u\x021\x03\x91\x03\xc0\x03\x11\x04W\x04Y\x04L\x04n\x04\x83\x04\x1a\x04h\x03\x07\x03\x9a\x02\xe5\x01=\x01' + \
        b'\xb9\x00\x02\x00.\xfff\xfe\xec\xfdM\xfd\x92\xfc1\xfc\xf2\xfb\x8f\xfbA\xfb-\xfbD\xfbD\xfb{\xfb"\xfc\xbd\xfcI\xfd\x0f\xfe\x0c\xff\xda\xfft\x00X\x019\x02\xb5\x02\x0c\x03\x89\x03\xe8\x03\x17\x04\x19\x04C\x04\x81\x04Y\x04>\x042\x04\xa4\x03\xe6\x02d\x02\xdd\x01X\x01~\x00\xc1' + \
        b'\xff\t\xff2\xfev\xfd\x0e\xfd\x8b\xfc\x03\xfc\x92\xfby\xfbP\xfb4\xfbf\xfb\xd8\xfb/\xfc\x98\xfc2\xfd\xce\xfdK\xfe\xd9\xfe\xa1\xff\x85\x00\'\x01\xc3\x01\xa5\x02P\x03\x8d\x03\n\x04v\x04\xc6\x04\xc7\x04\xce\x04\x9f\x04W\x04\xdc\x03B\x03\x89\x02\xa9\x01\xf3\x00\x8a\x00\xe2\xff' + \
        b'\xdd\xfe,\xfe\xa9\xfd$\xfd\x95\xfc7\xfc\x02\xfc\xc2\xfbm\xfbQ\xfbg\xfb\x84\xfb\xbf\xfb^\xfc\xd8\xfcr\xfd$\xfe\x0c\xff\xb4\xfft\x00=\x01\x0f\x02\x98\x02\x1c\x03\x90\x03\x01\x04=\x04%\x04Y\x04z\x04X\x04\r\x04\xe0\x03r\x03\xed\x02h\x02\xb0\x01\xf8\x00G\x00\xa1\xff\xdf\xfe' + \
        b'\'\xfe>\xfd\xd5\xfce\xfc\xdb\xfbj\xfb2\xfb\x17\xfb8\xfb\x8a\xfb\xe8\xfb]\xfc\xd1\xfcp\xfd\x18\xfe\xb3\xfe;\xff\xf2\xff\xae\x00X\x01\x04\x02\xae\x02$\x03\x8b\x03\n\x04\\\x04}\x04\x9b\x04\xaf\x04\x86\x04K\x04\xbb\x03&\x03\x82\x02\xda\x01\x11\x01v\x00\xc3\xff\xf8\xfe^\xfe' + \
        b'\xcd\xfd1\xfd\xce\xfcq\xfc\x00\xfc\xcc\xfb\x85\xfba\xfbh\xfbz\xfb\xd3\xfbh\xfc\xe1\xfcz\xfdB\xfe\xff\xfe\xbe\xff\x84\x00,\x01\xdb\x01b\x02\xdf\x02H\x03\xa6\x03\xdd\x03\t\x04<\x04<\x04.\x04\x1e\x04\xf8\x03\x81\x03\r\x03o\x02\xe8\x01\x1a\x01\x88\x00\xb9\xff\xcf\xfe!\xfe' + \
        b'\x86\xfd\xff\xfc\x8e\xfc\xf0\xfb\xb1\xfb\x97\xfb^\xfb{\xfb\xcc\xfb\x1c\xfc\x9f\xfc\x11\xfd\xb5\xfd9\xfe\xd2\xfeO\xff\xfa\xffr\x00\x13\x01\xac\x01]\x02\xbd\x02L\x03\xb7\x03\xf4\x03\x08\x04>\x04B\x04A\x04\xdb\x03|\x03\xf3\x02i\x02\xaf\x01+\x01}\x00\xda\xff\x1a\xff\x92' + \
        b'\xfe\r\xfe\x9b\xfdB\xfd\xee\xfct\xfc(\xfc\xe2\xfb\xb9\xfb\x9d\xfb\xba\xfb%\xfc\x94\xfc\xfd\xfc\x94\xfd5\xfe\xeb\xfe\x86\xff>\x00\x00\x01\xa6\x01\x1e\x02\xb1\x02\x1b\x03\x85\x03\xc5\x03\xe8\x03\xf4\x03\xf6\x03\xea\x03\xe4\x03\x97\x03;\x03\xd9\x02z\x02\xd1\x01?\x01\xa5' + \
        b'\x00\x11\x00D\xffz\xfe\xd8\xfde\xfd\xcf\xfc=\xfc\xdf\xfb\xb2\xfb\x88\xfb\x99\xfb\xc0\xfb\x0b\xfcm\xfc\xdb\xfcl\xfd\x01\xfe\x92\xfeC\xff\xe4\xff`\x00\xf9\x00\x95\x010\x02\x9e\x02 \x03\x95\x03\xeb\x03\xf7\x03\xfd\x03\x16\x04\x14\x04\xd3\x03\x92\x03\x1b\x03\x8d\x02\xf3' + \
        b'\x01Q\x01\xb4\x00\xf4\xff)\xff\x92\xfe\x10\xfe\x9d\xfdE\xfd\xf4\xfc\x9c\xfcO\xfc\x1d\xfc\xfe\xfb\xeb\xfb\xf1\xfb&\xfc\x8a\xfc\xee\xfct\xfd\x13\xfe\xbb\xfen\xff8\x00\x02\x01\x8b\x01\x10\x02\x82\x02\x06\x03`\x03\x94\x03\xa7\x03\xb8\x03\x98\x03\xb6\x03\x9f\x03|\x03A\x03' + \
        b'\xe1\x02k\x02\xe1\x01D\x01\xd2\x00#\x00d\xff\xb0\xfe\x16\xfe|\xfd\xe2\xfcj\xfc \xfc\xd4\xfb\xad\xfb\xae\xfb\xc4\xfb\x17\xfcm\xfc\x05\xfd\x89\xfd\x04\xfe\x91\xfe4\xff\xb0\xffL\x00\xd6\x00t\x01\xfc\x01q\x02\xff\x02\x80\x03\xb2\x03\xec\x03\x0b\x04\x18\x04\x02\x04\xc6\x03' + \
        b'\x84\x03\t\x03m\x02\xe4\x01V\x01\xc9\x00&\x00\x82\xff\xe3\xfeF\xfe\xd0\xfd\x81\xfd\x0b\xfd\xa9\xfcR\xfc\x1e\xfc\xfb\xfb\xd6\xfb\xf3\xfb9\xfc}\xfc\xeb\xfcf\xfd\xfc\xfd\x9d\xfeK\xff\x0c\x00\xc9\x00c\x01\t\x02}\x02\xeb\x026\x03\x80\x03\xa1\x03\xa7\x03\x97\x03\xb2\x03\x9e' + \
        b'\x03{\x03;\x03\xee\x02y\x02\xf0\x01d\x01\xe9\x00N\x00\x92\xff\xe9\xfe2\xfe\xa2\xfd\x16\xfd\xad\xfc:\xfc\xe9\xfb\xbd\xfb\xd3\xfb\xe5\xfb/\xfc\x86\xfc\x01\xfdq\xfd\xec\xfd\x8b\xfe\x1b\xff\x8e\xff\x11\x00\xa3\x00;\x01\xcd\x01B\x02\xc0\x02\'\x03\x85\x03\xd5\x03\xf9\x03\xf8' + \
        b'\x03\xef\x03\xd7\x03\x96\x03&\x03\xa4\x02\n\x02}\x01\xcf\x009\x00\x9a\xff\xe6\xfeI\xfe\xde\xfd|\xfd*\xfd\xd3\xfc\x8a\xfcY\xfc\x1f\xfc\xfa\xfb\x01\xfc"\xfci\xfc\xe7\xfcf\xfd\xfb\xfd\x92\xfeN\xff\xef\xff\x9f\x00(\x01\xe1\x01Z\x02\xc6\x02"\x03x\x03\x98\x03\x96\x03\x89\x03' + \
        b'\x94\x03\x86\x03a\x03&\x03\xd7\x02i\x02\xea\x01n\x01\xe1\x00:\x00\xa9\xff\xfd\xfeW\xfe\xb5\xfd-\xfd\xcd\xfc_\xfc\x0b\xfc\xfa\xfb\xf6\xfb\x0c\xfcO\xfc\xad\xfc"\xfd\x83\xfd\xfb\xfd\x91\xfe\x12\xff\x80\xff\x02\x00\x92\x00\x14\x01\xa2\x01\x1c\x02\xa5\x02\x0e\x03f\x03\xb6' + \
        b'\x03\xdf\x03\xde\x03\xdb\x03\xbb\x03g\x03\xfa\x02r\x02\xed\x01S\x01\xc8\x002\x00\xae\xff\x0b\xff\x88\xfe&\xfe\xbb\xfd_\xfd\x14\xfd\xd8\xfc\x98\xfcj\xfc-\xfcE\xfcB\xfc\x8d\xfc\xde\xfcm\xfd\xe9\xfd\x96\xfe&\xff\xca\xffr\x00\x12\x01\xb8\x018\x02\x93\x02\xef\x02/\x03Z\x03_' + \
        b'\x03h\x03h\x03h\x03S\x034\x03\xd3\x02|\x02\xf7\x01\x7f\x01\xed\x00X\x00\xc5\xff&\xfff\xfe\xe1\xfd]\xfd\xf6\xfc\x9a\xfcF\xfc.\xfc0\xfc:\xfc{\xfc\xc4\xfc\'\xfd\x8d\xfd\x07\xfex\xfe\xeb\xfet\xff\xf2\xffe\x00\xec\x00{\x01\t\x02u\x02\xd6\x02E\x03\x9f\x03\xb9\x03\xbb\x03\xc2' + \
        b'\x03\xa0\x03d\x03\x08\x03\x8f\x02\r\x02o\x01\xe2\x00^\x00\xc0\xff-\xff\xa7\xfe\x1b\xfe\xbf\xfdd\xfd(\xfd\xd4\xfc\x89\xfc`\xfcL\xfc/\xfc?\xfc{\xfc\xef\xfca\xfd\xe3\xfd\x82\xfe+\xff\xd4\xff|\x00\x1e\x01\xc2\x01S\x02\xb7\x02\n\x03O\x03\x7f\x03\x9a\x03\x9a\x03\x8d\x03\x83' + \
        b'\x03o\x03\'\x03\xcb\x02j\x02\x05\x02\x81\x01\xf3\x00`\x00\xc9\xff&\xff\x7f\xfe\xdc\xfd_\xfd\xe6\xfc\x93\xfcD\xfc\x1f\xfc,\xfc=\xfco\xfc\xb3\xfc\x1e\xfd\x98\xfd\x11\xfe\x90\xfe\x01\xff~\xff\xfd\xffc\x00\xf2\x00\x82\x01\xf1\x01a\x02\xc5\x02&\x03\x87\x03\xa7\x03\xb1\x03' + \
        b'\xad\x03\x97\x03^\x03\t\x03\xa2\x02\x1e\x02\x96\x01\x11\x01\x84\x00\xf4\xffa\xff\xdd\xfeT\xfe\xee\xfd\x94\xfdH\xfd\x06\xfd\xbc\xfc\x85\xfcn\xfc`\xfce\xfc\x9d\xfc\xfc\xfcj\xfd\xdf\xfdh\xfe\xec\xfe\x8b\xff4\x00\xcb\x00u\x01\x07\x02o\x02\xd0\x02\x10\x03J\x03{\x03\x85\x03' + \
        b'\x80\x03s\x03X\x03%\x03\xe2\x02\x81\x02\x10\x02\x8e\x01\x1d\x01\x9b\x00\x01\x00d\xff\xc3\xfe!\xfe\x8b\xfd\x18\xfd\xcc\xfcr\xfc@\xfcH\xfcO\xfct\xfc\xba\xfc\x04\xfd\x83\xfd\xf8\xfdh\xfe\xe2\xfeU\xff\xd3\xffb\x00\xdd\x00j\x01\xe3\x01_\x02\xc6\x02\x0c\x03P\x03\x8b\x03\xa6' + \
        b'\x03\xa8\x03\x8a\x03[\x03 \x03\xba\x02E\x02\xa7\x01\x1b\x01\x98\x00\x11\x00\x7f\xff\xed\xfe_\xfe\xee\xfd\x91\xfdC\xfd\xfa\xfc\xb7\xfc\x88\xfcu\xfcp\xfc\x85\xfc\xa9\xfc\xfa\xfcb\xfd\xd0\xfdV\xfe\xf1\xfe}\xff\x1c\x00\xb7\x00Y\x01\xf1\x01f\x02\xc0\x02\x0c\x039\x03d\x03h' + \
        b'\x03[\x03K\x030\x03\t\x03\xc3\x02c\x02\xfd\x01\x8d\x01\x17\x01\x91\x00\x16\x00\x83\xff\xe3\xfeP\xfe\xc6\xfdT\xfd\xf5\xfc\x99\xfcm\xfc`\xfcl\xfc\x96\xfc\xe4\xfc1\xfd\x8d\xfd\xf6\xfdh\xfe\xce\xfe5\xff\xa9\xff\'\x00\x9b\x00\x18\x01\xa1\x01\x17\x02z\x02\xd3\x02\x1d\x03f' + \
        b'\x03\x8b\x03\x90\x03\x89\x03`\x03\x1a\x03\xc2\x02G\x02\xbc\x018\x01\xb8\x00,\x00\xab\xff \xff\xa1\xfe\'\xfe\xc4\xfd\x80\xfdP\xfd\x0b\xfd\xd3\xfc\xae\xfc\xae\xfc\xb4\xfc\xd1\xfc\x05\xfd_\xfd\xc9\xfdQ\xfe\xdd\xfea\xff\xe9\xff\x84\x00\x1d\x01\xa3\x01\x17\x02o\x02\xb4\x02' + \
        b'\xe2\x02\xf9\x02\x15\x03 \x03\x15\x03\x03\x03\xe8\x02\xbc\x02x\x02\x1b\x02\xae\x010\x01\xb8\x00O\x00\xc8\xff\'\xff\x8a\xfe\r\xfe\x9f\xfd2\xfd\xcd\xfc\x99\xfc\x8b\xfc\x91\xfc\xa5\xfc\xe9\xfc<\xfd\x91\xfd\xf0\xfdh\xfe\xd8\xfe:\xff\xa5\xff\x1a\x00\x8b\x00\x0e\x01\x8e\x01' + \
        b'\xff\x01Z\x02\xaf\x02\x07\x03I\x03l\x03z\x03z\x03T\x03\x0c\x03\xbb\x02R\x02\xc6\x016\x01\xb0\x00<\x00\xc0\xff:\xff\xbe\xfeI\xfe\xee\xfd\xa6\xfd\\\xfd\x1a\xfd\xe6\xfc\xcb\xfc\xc4\xfc\xb9\xfc\xc8\xfc\x01\xfdT\xfd\xb9\xfd\'\xfe\xb6\xfe;\xff\xce\xffk\x00\x07\x01\x94\x01' + \
        b'\x11\x02r\x02\xbe\x02\xf3\x02\x07\x03\x1f\x03\x1d\x03\x11\x03\xf3\x02\xd9\x02\xa6\x02f\x02\x17\x02\xbd\x01O\x01\xd5\x00`\x00\xe3\xffY\xff\xc2\xfe1\xfe\xbc\xfdH\xfd\xef\xfc\xb3\xfc\x8e\xfc\x8e\xfc\xaa\xfc\xe0\xfc0\xfd{\xfd\xe0\xfdN\xfe\xb4\xfe\x1e\xff\x89\xff\xfb\xfft\x00' + \
        b'\xe1\x00\\\x01\xcf\x014\x02\x86\x02\xd4\x02\x05\x03>\x03O\x03M\x032\x03\x00\x03\xac\x02S\x02\xd0\x01L\x01\xcf\x00R\x00\xd9\xffY\xff\xe1\xfel\xfe\x02\xfe\xae\xfdp\xfd8\xfd\n\xfd\xe7\xfc\xe0\xfc\xdb\xfc\xeb\xfc\x1d\xfd]\xfd\xb8\xfd\x1f\xfe\xa1\xfe/\xff\xb4\xff@\x00\xd4' + \
        b'\x00\\\x01\xd0\x019\x02\x8a\x02\xbd\x02\xdd\x02\xfc\x02\x08\x03\xf1\x02\xcf\x02\xbd\x02\x95\x02O\x02\x04\x02\xa8\x01C\x01\xcb\x00W\x00\xec\xffj\xff\xdc\xfe`\xfe\xe9\xfd\x81\xfd+\xfd\xe8\xfc\xc0\xfc\xa8\xfc\xbb\xfc\xef\xfc/\xfdw\xfd\xcf\xfd8\xfe\xa0\xfe\x07\xffs\xff\xdc' + \
        b'\xffD\x00\xad\x00)\x01\x9f\x01\x03\x02Q\x02\xa5\x02\xe6\x02\x18\x036\x03>\x03(\x03\xf7\x02\xb5\x02`\x02\xef\x01h\x01\xe8\x00m\x00\xef\xffw\xff\x03\xff\x90\xfe*\xfe\xd2\xfd\x9c\xfdg\xfd6\xfd\x17\xfd\x0b\xfd\x08\xfd\r\xfd.\xfdg\xfd\xb3\xfd\x18\xfe\x8e\xfe\x0b\xff\x8c\xff' + \
        b'\x19\x00\xaf\x005\x01\xa8\x01\x1b\x02n\x02\xa8\x02\xcd\x02\xef\x02\x07\x03\xfe\x02\xed\x02\xd0\x02\xaa\x02y\x02/\x02\xd9\x01u\x01\x01\x01\x94\x00\x17\x00\x8b\xff\x05\xff\x80\xfe\x08\xfe\x9d\xfdK\xfd\x11\xfd\xe6\xfc\xcf\xfc\xd8\xfc\x01\xfd4\xfd\x80\xfd\xd4\xfd3\xfe\x95' + \
        b'\xfe\xf6\xfeZ\xff\xbd\xff!\x00\x99\x00\x0f\x01u\x01\xda\x010\x02}\x02\xba\x02\xef\x02\x13\x03\x19\x03\x11\x03\xf0\x02\xb8\x02d\x02\xf5\x01\x81\x01\x0b\x01\x90\x00\x1b\x00\xa8\xff1\xff\xbe\xfe[\xfe\x07\xfe\xc0\xfd\x81\xfdR\xfd,\xfd\x0e\xfd\xf8\xfc\x01\xfd\x14\xfd<\xfd\x83' + \
        b'\xfd\xe6\xfd_\xfe\xdf\xfef\xff\xf7\xff\x8a\x00\x13\x01\x9c\x01\x17\x02p\x02\xad\x02\xd9\x02\xf5\x02\x04\x03\xff\x02\xec\x02\xd2\x02\xac\x02t\x023\x02\xde\x01~\x01\x16\x01\xa7\x000\x00\xb0\xff)\xff\x9d\xfe\x1c\xfe\xa9\xfdM\xfd\n\xfd\xdc\xfc\xc1\xfc\xc5\xfc\xe2\xfc\x1c\xfdi' + \
        b'\xfd\xc3\xfd\x1d\xfe\x81\xfe\xea\xfeS\xff\xb9\xff\x1a\x00\x81\x00\xf1\x00X\x01\xc0\x01\x1a\x02h\x02\xad\x02\xea\x02\x17\x03$\x03\x1e\x03\t\x03\xd8\x02\x87\x02!\x02\xb3\x01B\x01\xc3\x00=\x00\xc0\xffG\xff\xd9\xfen\xfe\x0e\xfe\xc5\xfd\x8e\xfd]\xfd6\xfd\x14\xfd\x05\xfd\x0b\xfd' + \
        b'\x1a\xfd=\xfd\x81\xfd\xe0\xfdK\xfe\xbb\xfe=\xff\xc9\xffW\x00\xdd\x00b\x01\xd5\x016\x02v\x02\xa4\x02\xc6\x02\xd9\x02\xdd\x02\xd4\x02\xbf\x02\xa2\x02v\x026\x02\xeb\x01\x9b\x01B\x01\xd7\x00h\x00\xf1\xffl\xff\xe2\xfeQ\xfe\xda\xfd|\xfd-\xfd\xf4\xfc\xd2\xfc\xc2\xfc\xd9\xfc\x05\xfdL' + \
        b'\xfd\x9f\xfd\xf7\xfde\xfe\xd8\xfe?\xff\xa2\xff\n\x00u\x00\xdf\x00B\x01\xae\x01\x15\x02h\x02\xaf\x02\xea\x02\x13\x03(\x03!\x03\x08\x03\xd1\x02\x84\x02*\x02\xc3\x01D\x01\xc1\x00D\x00\xce\xffZ\xff\xe6\xfe\x81\xfe/\xfe\xe9\xfd\xb5\xfd\x8a\xfdb\xfd>\xfd,\xfd+\xfd5\xfdP\xfd\x8c\xfd' + \
        b'\xd8\xfd7\xfe\xa4\xfe"\xff\xae\xff2\x00\xbc\x00B\x01\xb1\x01\x0b\x02L\x02~\x02\x9a\x02\xa5\x02\xab\x02\xa2\x02\x94\x02y\x02V\x02"\x02\xe0\x01\x97\x01F\x01\xe5\x00\x7f\x00\x15\x00\xa2\xff\x1d\xff\x97\xfe"\xfe\xbb\xfdi\xfd0\xfd\x0c\xfd\xf7\xfc\xfd\xfc&\xfde\xfd\xac\xfd\xff\xfda' + \
        b'\xfe\xc9\xfe#\xff\x7f\xff\xe4\xffE\x00\xa2\x00\x05\x01l\x01\xce\x01\x1c\x02i\x02\xb1\x02\xe3\x02\x01\x03\x06\x03\xf8\x02\xcf\x02\x91\x02G\x02\xe2\x01p\x01\xf9\x00\x85\x00\x0b\x00\x8c\xff\x1e\xff\xc1\xfeb\xfe\x15\xfe\xda\xfd\xb1\xfd\x85\xfd\\\xfdF\xfd<\xfd?\xfd[\xfd\x8c\xfd\xd3' + \
        b'\xfd&\xfe\x8e\xfe\x04\xff}\xff\xfd\xff\x84\x00\x08\x01}\x01\xdd\x014\x02s\x02\x9b\x02\xb2\x02\xbe\x02\xbb\x02\xaa\x02\x98\x02z\x02K\x02\x07\x02\xbd\x01e\x01\x02\x01\x9a\x003\x00\xb6\xff.\xff\xb3\xfeB\xfe\xd9\xfd\x80\xfdC\xfd"\xfd\x06\xfd\x04\xfd\x1e\xfdT\xfd\x8f\xfd\xdb\xfdF' + \
        b'\xfe\xa8\xfe\x08\xffi\xff\xcb\xff,\x00\x85\x00\xe9\x00W\x01\xb2\x01\x02\x02P\x02\x94\x02\xc5\x02\xe4\x02\xf2\x02\xe8\x02\xc6\x02\x90\x02R\x02\xfc\x01\x8a\x01\x15\x01\xa6\x00+\x00\xb9\xffH\xff\xda\xfe{\xfe$\xfe\xed\xfd\xc1\xfd\x8f\xfdh\xfdR\xfdB\xfd@\xfdR\xfd{\xfd\xbb\xfd\t\xfei' + \
        b'\xfe\xda\xfeL\xff\xc9\xffM\x00\xcb\x00>\x01\xaa\x01\x05\x02B\x02j\x02\x8b\x02\xa1\x02\x9f\x02\x91\x02~\x02h\x02:\x02\xfe\x01\xbf\x01o\x01\x15\x01\xb5\x00P\x00\xde\xff`\xff\xe3\xfeo\xfe\x02\xfe\xad\xfds\xfdK\xfd\'\xfd \xfd9\xfdf\xfd\xa0\xfd\xe1\xfd;\xfe\x98\xfe\xeb\xfeE\xff\xa0' + \
        b'\xff\xfb\xffP\x00\xae\x00\x11\x01m\x01\xc2\x01\x13\x02X\x02\x8f\x02\xb5\x02\xce\x02\xcb\x02\xa9\x02\x80\x02F\x02\xf4\x01\x8e\x01#\x01\xbb\x00N\x00\xdc\xffp\xff\x0f\xff\xaa\xfe^\xfe"\xfe\xed\xfd\xbd\xfd\x93\xfdm\xfdZ\xfdM\xfd[\xfd\x7f\xfd\xac\xfd\xf3\xfdQ\xfe\xb7\xfe\'\xff\x9c' + \
        b'\xff"\x00\xa7\x00\x1d\x01\x8d\x01\xe9\x01-\x02Z\x02}\x02\x90\x02\x94\x02\x87\x02w\x02`\x02:\x02\x06\x02\xcc\x01~\x01&\x01\xd2\x00t\x00\r\x00\x95\xff\x1f\xff\xaa\xfe<\xfe\xdc\xfd\x9a\xfdi\xfdC\xfd1\xfd:\xfdX\xfd\x8a\xfd\xcd\xfd\x1f\xfez\xfe\xd3\xfe/\xff\x88\xff\xd8\xff4\x00\x8e' + \
        b'\x00\xf0\x00I\x01\xa1\x01\xf6\x01<\x02q\x02\xa2\x02\xbe\x02\xc4\x02\xae\x02\x88\x02T\x02\x04\x02\xa5\x01?\x01\xd2\x00c\x00\xf1\xff\x89\xff&\xff\xca\xfe}\xfe>\xfe\x07\xfe\xd9\xfd\xb7\xfd\x9b\xfd\x81\xfdr\xfd|\xfd\x9b\xfd\xc6\xfd\x05\xfe[\xfe\xbd\xfe#\xff\x92\xff\x0c\x00\x84\x00' + \
        b'\xf0\x00a\x01\xbc\x01\x04\x023\x02U\x02r\x02w\x02k\x02a\x02M\x02-\x02\x01\x02\xc9\x01\x86\x016\x01\xe1\x00\x87\x00\x1e\x00\xad\xff8\xff\xc5\xfeQ\xfe\xee\xfd\xa5\xfdp\xfdL\xfd8\xfd=\xfdZ\xfd\x88\xfd\xcf\xfd"\xfey\xfe\xd3\xfe*\xff\x84\xff\xd4\xff%\x00\x7f\x00\xd4\x00.\x01\x85\x01' + \
        b'\xda\x01\x1c\x02V\x02\x88\x02\xa8\x02\xb0\x02\xa1\x02\x83\x02U\x02\t\x02\xae\x01L\x01\xe0\x00u\x00\x04\x00\x9c\xff=\xff\xdd\xfe\x8c\xfeG\xfe\x0f\xfe\xe8\xfd\xc3\xfd\xa0\xfd\x86\xfd\x80\xfd\x89\xfd\x9a\xfd\xbe\xfd\xfd\xfdS\xfe\xad\xfe\x0e\xff|\xff\xf0\xffa\x00\xcf\x007\x01\x95' + \
        b'\x01\xd6\x01\x08\x022\x02M\x02\\\x02[\x02S\x02?\x02"\x02\x04\x02\xd5\x01\x96\x01L\x01\xfc\x00\xa8\x00A\x00\xd4\xffi\xff\xf4\xfe\x83\xfe\x1d\xfe\xd0\xfd\x94\xfdk\xfdV\xfdT\xfdb\xfd\x89\xfd\xc6\xfd\x0c\xfeY\xfe\xaf\xfe\x07\xffZ\xff\xa8\xff\xfa\xffW\x00\xaa\x00\xfd\x00Y\x01\xad' + \
        b'\x01\xf5\x01/\x02h\x02\x93\x02\xa3\x02\x99\x02\x83\x02V\x02\x14\x02\xc1\x01d\x01\x00\x01\x99\x006\x00\xd2\xffo\xff\x13\xff\xc1\xfeu\xfe3\xfe\x02\xfe\xdc\xfd\xb7\xfd\x95\xfd\x85\xfd\x87\xfd\x92\xfd\xae\xfd\xe5\xfd1\xfe\x88\xfe\xe9\xfeV\xff\xca\xff:\x00\xaf\x00\x1d\x01x\x01\xc4' + \
        b'\x01\xff\x01*\x02F\x02Q\x02U\x02H\x027\x02\x1c\x02\xff\x01\xd5\x01\x97\x01U\x01\x0c\x01\xb7\x00\\\x00\xfa\xff\x91\xff&\xff\xb4\xfeR\xfe\xfc\xfd\xba\xfd\x91\xfd|\xfdn\xfdu\xfd\x96\xfd\xcc\xfd\x0f\xfeV\xfe\xab\xfe\x02\xffN\xff\x98\xff\xed\xffC\x00\x91\x00\xe4\x00=\x01\x8e\x01' + \
        b'\xd5\x01\x17\x02P\x02y\x02\x8d\x02\x90\x02\x83\x02[\x02"\x02\xdc\x01\x81\x01\x17\x01\xb1\x00M\x00\xe7\xff\x81\xff\'\xff\xd7\xfe\x8a\xfeI\xfe\x17\xfe\xf6\xfd\xd4\xfd\xb5\xfd\xa6\xfd\xa5\xfd\xab\xfd\xc3\xfd\xf3\xfd6\xfe\x86\xfe\xe3\xfeN\xff\xb9\xff+\x00\x9f\x00\r\x01o\x01\xc2' + \
        b'\x01\x01\x02.\x02J\x02\\\x02d\x02\\\x02F\x02)\x02\x06\x02\xda\x01\xa4\x01e\x01\x1c\x01\xc7\x00r\x00\x16\x00\xad\xffB\xff\xd4\xfen\xfe\x11\xfe\xc8\xfd\x9a\xfd}\xfdj\xfdi\xfd\x81\xfd\xb2\xfd\xf2\xfd:\xfe\x8f\xfe\xe6\xfe6\xff\x88\xff\xd9\xff+\x00z\x00\xd1\x00-\x01\x80\x01\xcb\x01' + \
        b'\x12\x02K\x02v\x02\x94\x02\xa0\x02\x96\x02u\x02B\x02\x00\x02\xaa\x01G\x01\xe4\x00\x80\x00\x19\x00\xb6\xffY\xff\x02\xff\xaf\xfei\xfe2\xfe\x06\xfe\xe2\xfd\xc4\xfd\xb1\xfd\xa6\xfd\xa5\xfd\xb8\xfd\xdd\xfd\x14\xfe]\xfe\xb4\xfe\x1b\xff\x83\xff\xf2\xffg\x00\xd2\x005\x01\x90\x01\xd5' + \
        b'\x01\x08\x020\x02L\x02Z\x02Z\x02J\x028\x02!\x02\xf3\x01\xbe\x01\x81\x018\x01\xe4\x00\x8e\x003\x00\xcc\xffd\xff\xfc\xfe\x94\xfe2\xfe\xe6\xfd\xb2\xfd\x8e\xfdv\xfdq\xfd\x81\xfd\xa7\xfd\xde\xfd\x1f\xfem\xfe\xbd\xfe\t\xff[\xff\xae\xff\x01\x00W\x00\xaf\x00\x06\x01Z\x01\xab\x01\xf1' + \
        b'\x01-\x02]\x02\x7f\x02\x92\x02\x8e\x02s\x02E\x02\t\x02\xba\x01[\x01\xfa\x00\x98\x003\x00\xd0\xffs\xff\x19\xff\xc8\xfe|\xfe@\xfe\x11\xfe\xe9\xfd\xcd\xfd\xb3\xfd\x9f\xfd\x9c\xfd\xac\xfd\xcb\xfd\xfc\xfd?\xfe\x98\xfe\xf8\xfe]\xff\xcb\xff=\x00\xac\x00\x15\x01t\x01\xc3\x01\xfe\x01)' + \
        b'\x02I\x02^\x02a\x02V\x02D\x02+\x02\x06\x02\xd6\x01\x98\x01P\x01\x03\x01\xb0\x00S\x00\xf0\xff\x89\xff \xff\xb7\xfeS\xfe\x00\xfe\xc4\xfd\x9a\xfd\x81\xfd|\xfd\x85\xfd\xa4\xfd\xd4\xfd\x16\xfe_\xfe\xab\xfe\xfa\xfeN\xff\x9d\xff\xed\xff?\x00\x95\x00\xea\x009\x01\x8a\x01\xd1\x01\x10' + \
        b'\x02B\x02j\x02\x80\x02\x83\x02r\x02M\x02\x14\x02\xc8\x01r\x01\x11\x01\xae\x00K\x00\xeb\xff\x91\xff6\xff\xe3\xfe\x9b\xfeZ\xfe&\xfe\xff\xfd\xe0\xfd\xc7\xfd\xb3\xfd\xae\xfd\xb7\xfd\xcd\xfd\xf7\xfd6\xfe\x87\xfe\xe3\xfeH\xff\xb3\xff&\x00\x92\x00\xfb\x00Y\x01\xa7\x01\xe1\x01\r\x02,' + \
        b'\x02=\x02D\x02>\x02-\x02\x18\x02\xf7\x01\xd1\x01\x9c\x01]\x01\x16\x01\xc7\x00p\x00\x12\x00\xad\xffH\xff\xe0\xfe|\xfe!\xfe\xe0\xfd\xb4\xfd\x97\xfd\x8d\xfd\x91\xfd\xaa\xfd\xda\xfd\x16\xfeZ\xfe\xa3\xfe\xf1\xfe=\xff\x89\xff\xd3\xff"\x00s\x00\xc6\x00\x18\x01h\x01\xb0\x01\xf0\x01&' + \
        b'\x02P\x02l\x02u\x02l\x02K\x02\x13\x02\xce\x01|\x01\x1c\x01\xba\x00Y\x00\xfa\xff\xa0\xffG\xff\xfa\xfe\xb2\xfes\xfe>\xfe\x17\xfe\xf8\xfd\xdd\xfd\xc8\xfd\xbe\xfd\xc0\xfd\xd3\xfd\xf8\xfd/\xfew\xfe\xcd\xfe/\xff\x93\xff\xfe\xffi\x00\xd4\x003\x01\x84\x01\xc1\x01\xf1\x01\x12\x02\'\x02.' + \
        b'\x02)\x02\x1d\x02\x0c\x02\xee\x01\xc5\x01\x94\x01\\\x01\x19\x01\xd0\x00|\x00%\x00\xc8\xffg\xff\x02\xff\x9e\xfeC\xfe\xfa\xfd\xc3\xfd\xa2\xfd\x93\xfd\x96\xfd\xa8\xfd\xce\xfd\x04\xfeF\xfe\x90\xfe\xdc\xfe(\xffu\xff\xc0\xff\r\x00\\\x00\xac\x00\xfe\x00I\x01\x92\x01\xd2\x01\r\x02;\x02X' + \
        b'\x02e\x02a\x02J\x02\x1d\x02\xdd\x01\x8d\x014\x01\xd7\x00v\x00\x18\x00\xb9\xffd\xff\x13\xff\xc9\xfe\x88\xfeP\xfe&\xfe\x06\xfe\xe8\xfd\xd2\xfd\xc5\xfd\xc3\xfd\xd2\xfd\xef\xfd \xfea\xfe\xaf\xfe\n\xffn\xff\xd5\xff@\x00\xa9\x00\t\x01b\x01\xa7\x01\xdc\x01\x03\x02\x19\x02\'\x02&\x02' + \
        b'\x1d\x02\x0f\x02\xf1\x01\xcd\x01\x9e\x01i\x01)\x01\xde\x00\x8f\x00;\x00\xdf\xff\x81\xff \xff\xbd\xfe_\xfe\x10\xfe\xd7\xfd\xb0\xfd\x9f\xfd\x99\xfd\xa9\xfd\xc8\xfd\xfc\xfd<\xfe\x82\xfe\xcc\xfe\x16\xffb\xff\xb0\xff\xfa\xffF\x00\x93\x00\xe1\x00,\x01s\x01\xb5\x01\xeb\x01\x1b\x02?' + \
        b'\x02Q\x02U\x02E\x02 \x02\xe8\x01\x9e\x01K\x01\xf1\x00\x90\x003\x00\xd8\xff\x82\xff3\xff\xe9\xfe\xa8\xfen\xfeB\xfe \xfe\x05\xfe\xec\xfd\xdd\xfd\xd9\xfd\xe2\xfd\xf7\xfd#\xfe^\xfe\xaa\xfe\x00\xffb\xff\xca\xff4\x00\x9c\x00\xfe\x00T\x01\x9b\x01\xcf\x01\xf3\x01\t\x02\x13\x02\x16\x02' + \
        b'\x0e\x02\xff\x01\xe6\x01\xc6\x01\x9d\x01j\x01/\x01\xed\x00\xa3\x00S\x00\xfc\xff\xa1\xffB\xff\xe3\xfe\x86\xfe4\xfe\xf4\xfd\xcb\xfd\xb5\xfd\xaf\xfd\xba\xfd\xd8\xfd\x06\xfeB\xfe\x84\xfe\xcb\xfe\x16\xff_\xff\xa3\xff\xec\xff5\x00~\x00\xcb\x00\x14\x01^\x01\x9d\x01\xd9\x01\n\x021\x02G' + \
        b'\x02N\x02D\x02%\x02\xf1\x01\xb0\x01`\x01\x07\x01\xaa\x00N\x00\xf4\xff\x9f\xffP\xff\n\xff\xc8\xfe\x8e\xfe_\xfe<\xfe\x1e\xfe\x06\xfe\xf6\xfd\xed\xfd\xee\xfd\x00\xfe$\xfeW\xfe\x97\xfe\xe4\xfe>\xff\x9d\xff\x00\x00f\x00\xca\x00#\x01p\x01\xab\x01\xd7\x01\xf4\x01\x05\x02\x0c\x02\x0b' + \
        b'\x02\xfe\x01\xea\x01\xd2\x01\xac\x01\x7f\x01J\x01\x0e\x01\xc8\x00z\x00(\x00\xd0\xffr\xff\x14\xff\xb5\xfe^\xfe\x17\xfe\xe4\xfd\xc5\xfd\xb5\xfd\xb7\xfd\xcb\xfd\xef\xfd!\xfe`\xfe\xa6\xfe\xef\xfe5\xff{\xff\xc5\xff\x0c\x00T\x00\x9f\x00\xec\x004\x01x\x01\xb5\x01\xea\x01\x17\x025' + \
        b'\x02F\x02E\x02-\x02\x04\x02\xc7\x01|\x01%\x01\xc8\x00i\x00\x0c\x00\xb2\xffa\xff\x16\xff\xd0\xfe\x94\xfec\xfe;\xfe\x1e\xfe\x06\xfe\xf9\xfd\xef\xfd\xef\xfd\xfb\xfd\x19\xfeC\xfe\x7f\xfe\xc9\xfe\x1d\xff|\xff\xe0\xffH\x00\xab\x00\x07\x01[\x01\x9e\x01\xcd\x01\xee\x01\x05\x02\x10\x02' + \
        b'\x0b\x02\x01\x02\xf1\x01\xd6\x01\xb4\x01\x8c\x01]\x01#\x01\xe1\x00\x97\x00H\x00\xf2\xff\x94\xff6\xff\xda\xfe~\xfe1\xfe\xf7\xfd\xd0\xfd\xbc\xfd\xb9\xfd\xca\xfd\xeb\xfd\x1c\xfeY\xfe\x9f\xfe\xe7\xfe-\xfft\xff\xba\xff\xff\xffB\x00\x8b\x00\xd1\x00\x18\x01[\x01\x9d\x01\xd4\x01\x03' + \
        b'\x02(\x02@\x02C\x024\x02\x13\x02\xdd\x01\x96\x01E\x01\xea\x00\x8e\x004\x00\xdb\xff\x8b\xff>\xff\xf7\xfe\xba\xfe\x87\xfe[\xfe5\xfe\x1b\xfe\x06\xfe\xf5\xfd\xeb\xfd\xf2\xfd\t\xfe.\xfef\xfe\xad\xfe\x00\xff[\xff\xbf\xff\'\x00\x8c\x00\xec\x00B\x01\x87\x01\xbb\x01\xe1\x01\xf9\x01' + \
        b'\x08\x02\x08\x02\x00\x02\xf2\x01\xdb\x01\xba\x01\x96\x01f\x01.\x01\xed\x00\xa6\x00Y\x00\x06\x00\xac\xffO\xff\xf0\xfe\x95\xfeE\xfe\x08\xfe\xdc\xfd\xc6\xfd\xc1\xfd\xcf\xfd\xea\xfd\x15\xfeP\xfe\x93\xfe\xd8\xfe"\xffh\xff\xb0\xff\xf6\xff9\x00\x81\x00\xc4\x00\t\x01K\x01\x8a\x01\xc2' + \
        b'\x01\xf1\x01\x15\x02-\x023\x02)\x02\r\x02\xde\x01\x9d\x01O\x01\xfb\x00\xa1\x00F\x00\xef\xff\x9d\xffN\xff\x08\xff\xcb\xfe\x94\xfeh\xfeD\xfe\'\xfe\x13\xfe\x02\xfe\xf9\xfd\xfc\xfd\x0c\xfe+\xfe]\xfe\x9d\xfe\xeb\xfeB\xff\xa2\xff\x06\x00k\x00\xc8\x00 \x01g\x01\xa0\x01\xc8\x01\xe3' + \
        b'\x01\xef\x01\xf3\x01\xed\x01\xe0\x01\xca\x01\xae\x01\x8c\x01g\x012\x01\xf6\x00\xb5\x00k\x00\x1d\x00\xc7\xffo\xff\x12\xff\xb8\xfeg\xfe"\xfe\xf3\xfd\xd7\xfd\xcd\xfd\xd5\xfd\xec\xfd\x11\xfeE\xfe\x83\xfe\xc3\xfe\t\xffP\xff\x94\xff\xd7\xff\x1c\x00b\x00\xa9\x00\xec\x002\x01s\x01\xac' + \
        b'\x01\xdd\x01\x02\x02\x1d\x02)\x02"\x02\x0c\x02\xde\x01\xa4\x01Z\x01\x08\x01\xb1\x00U\x00\x00\x00\xb1\xffc\xff\x1e\xff\xe1\xfe\xab\xfe~\xfeY\xfe>\xfe*\xfe\x19\xfe\x0e\xfe\x0e\xfe\x1a\xfe4\xfe^\xfe\x98\xfe\xdf\xfe0\xff\x8b\xff\xe8\xffF\x00\xa2\x00\xf7\x00@\x01{\x01\xa6\x01\xc8' + \
        b'\x01\xd9\x01\xe0\x01\xe0\x01\xd4\x01\xc2\x01\xa9\x01\x88\x01d\x014\x01\xfc\x00\xbd\x00w\x00-\x00\xdb\xff\x89\xff4\xff\xdd\xfe\x8c\xfeI\xfe\x15\xfe\xf3\xfd\xe5\xfd\xe7\xfd\xf7\xfd\x15\xfeC\xfey\xfe\xb7\xfe\xf8\xfe=\xff~\xff\xbf\xff\xff\xffB\x00\x82\x00\xc5\x00\x06\x01F\x01' + \
        b'\x7f\x01\xb3\x01\xdb\x01\xf9\x01\x08\x02\x06\x02\xf6\x01\xd2\x01\x9d\x01]\x01\x13\x01\xbe\x00h\x00\x15\x00\xc5\xffz\xff7\xff\xfb\xfe\xc6\xfe\x97\xfes\xfeW\xfeA\xfe0\xfe$\xfe \xfe&\xfe9\xfe\\\xfe\x91\xfe\xd0\xfe\x18\xffk\xff\xc5\xff \x00z\x00\xcf\x00\x1c\x01Z\x01\x8b\x01\xb0' + \
        b'\x01\xc3\x01\xca\x01\xcc\x01\xc1\x01\xb2\x01\x9d\x01\x82\x01`\x017\x01\x05\x01\xcd\x00\x8e\x00H\x00\xff\xff\xb2\xff`\xff\x0f\xff\xbe\xfew\xfe?\xfe\x1a\xfe\x08\xfe\x03\xfe\x0f\xfe)\xfeP\xfe\x83\xfe\xbc\xfe\xfc\xfe:\xffx\xff\xb5\xff\xf1\xff-\x00g\x00\xa4\x00\xe2\x00\x1e\x01W' + \
        b'\x01\x8a\x01\xb5\x01\xd4\x01\xe6\x01\xeb\x01\xe3\x01\xc5\x01\x99\x01a\x01\x1e\x01\xcf\x00\x80\x001\x00\xe4\xff\xa0\xff`\xff%\xff\xf3\xfe\xc7\xfe\xa5\xfe\x8b\xfet\xfec\xfe[\xfeT\xfeU\xfe`\xfez\xfe\xa4\xfe\xd9\xfe\x1a\xffd\xff\xb4\xff\x06\x00Y\x00\xa7\x00\xef\x00,\x01]\x01' + \
        b'\x80\x01\x95\x01\x9f\x01\xa1\x01\x9b\x01\x8c\x01z\x01c\x01F\x01!\x01\xf6\x00\xc6\x00\x8d\x00O\x00\x0e\x00\xca\xff\x81\xff7\xff\xee\xfe\xab\xfet\xfeN\xfe8\xfe0\xfe7\xfeJ\xfel\xfe\x96\xfe\xc9\xfe\x02\xff=\xffx\xff\xb1\xff\xe8\xff\x1e\x00S\x00\x88\x00\xbe\x00\xf2\x00#\x01N' + \
        b'\x01s\x01\x90\x01\xa3\x01\xab\x01\xa4\x01\x93\x01q\x01E\x01\x0c\x01\xca\x00\x85\x00@\x00\xfd\xff\xbb\xff\x81\xffJ\xff\x1b\xff\xf0\xfe\xcf\xfe\xb2\xfe\x9d\xfe\x8e\xfe\x81\xfez\xfex\xfe\x81\xfe\x94\xfe\xb4\xfe\xe1\xfe\x17\xffX\xff\x9e\xff\xe6\xff/\x00w\x00\xb7\x00\xf1\x00 \x01A' + \
        b'\x01W\x01e\x01h\x01d\x01W\x01J\x018\x01\x1f\x01\x02\x01\xe1\x00\xb9\x00\x8b\x00W\x00"\x00\xe9\xff\xac\xffm\xff.\xff\xf3\xfe\xc0\xfe\x9a\xfe\x81\xfet\xfeu\xfe\x81\xfe\x98\xfe\xb9\xfe\xe1\xfe\x11\xffB\xfft\xff\xa4\xff\xd5\xff\x03\x001\x00^\x00\x8d\x00\xba\x00\xe5\x00\r\x010' + \
        b'\x01L\x01`\x01k\x01l\x01`\x01J\x01&\x01\xfa\x00\xc5\x00\x8e\x00S\x00\x19\x00\xe2\xff\xae\xff\x7f\xffS\xff,\xff\r\xff\xef\xfe\xda\xfe\xc9\xfe\xbd\xfe\xb5\xfe\xb3\xfe\xb7\xfe\xc4\xfe\xdc\xfe\xfe\xfe+\xff`\xff\x9a\xff\xd6\xff\x16\x00T\x00\x8e\x00\xc2\x00\xec\x00\x0c\x01"' + \
        b'\x01/\x014\x01/\x01\'\x01\x1c\x01\x0c\x01\xf9\x00\xe1\x00\xc7\x00\xa6\x00\x81\x00Z\x00.\x00\xfe\xff\xcc\xff\x99\xffd\xff1\xff\x04\xff\xe0\xfe\xc9\xfe\xbb\xfe\xb9\xfe\xc2\xfe\xd1\xfe\xea\xfe\x0c\xff0\xffY\xff\x81\xff\xa9\xff\xd0\xff\xf5\xff\x1b\x00A\x00g\x00\x8b\x00\xb0' + \
        b'\x00\xd3\x00\xf0\x00\t\x01\x1c\x01*\x01+\x01$\x01\x14\x01\xfa\x00\xd6\x00\xab\x00}\x00L\x00\x1c\x00\xed\xff\xc2\xff\x9c\xffz\xff[\xffA\xff,\xff\x1c\xff\x10\xff\t\xff\x01\xff\x00\xff\x00\xff\t\xff\x19\xff1\xffQ\xffw\xff\xa1\xff\xd1\xff\x02\x002\x00a\x00\x8a\x00\xae\x00' + \
        b'\xc9\x00\xdd\x00\xea\x00\xef\x00\xef\x00\xea\x00\xe2\x00\xd5\x00\xc8\x00\xb7\x00\xa1\x00\x88\x00k\x00M\x00,\x00\x06\x00\xe1\xff\xb9\xff\x91\xffi\xffE\xff&\xff\x10\xff\x05\xff\x00\xff\x03\xff\x0f\xff\x1f\xff8\xffT\xfft\xff\x94\xff\xb4\xff\xd4\xff\xf1\xff\x0f\x00,\x00J' + \
        b'\x00g\x00\x83\x00\x9e\x00\xb5\x00\xc7\x00\xd7\x00\xe1\x00\xe3\x00\xe1\x00\xd7\x00\xc3\x00\xab\x00\x8b\x00j\x00E\x00\x1f\x00\xfc\xff\xda\xff\xbc\xff\xa0\xff\x89\xfft\xffb\xffU\xffK\xffE\xff@\xff>\xff=\xffA\xffL\xff\\\xffs\xff\x8d\xff\xac\xff\xcf\xff\xf2\xff\x16\x00:\x00[' + \
        b'\x00w\x00\x8d\x00\x9e\x00\xa9\x00\xae\x00\xaf\x00\xac\x00\xa7\x00\x9e\x00\x93\x00\x87\x00w\x00f\x00Q\x00<\x00#\x00\t\x00\xef\xff\xd3\xff\xb5\xff\x98\xff}\xfff\xffS\xffI\xffC\xffE\xffL\xffW\xffg\xff|\xff\x91\xff\xa8\xff\xc0\xff\xd7\xff\xeb\xff\x02\x00\x16\x00*\x00=' + \
        b'\x00Q\x00d\x00u\x00\x83\x00\x90\x00\x97\x00\x9b\x00\x9c\x00\x98\x00\x8b\x00|\x00h\x00R\x007\x00\x1d\x00\x04\x00\xec\xff\xd5\xff\xc1\xff\xb1\xff\xa2\xff\x95\xff\x8b\xff\x84\xff\x7f\xff{\xffy\xffx\xffz\xff\x7f\xff\x88\xff\x96\xff\xa6\xff\xbb\xff\xd1\xff\xe9\xff\x01\x00' + \
        b'\x1b\x003\x00F\x00X\x00e\x00n\x00r\x00s\x00r\x00p\x00j\x00d\x00\\\x00R\x00H\x00;\x00-\x00\x1f\x00\x0e\x00\xfd\xff\xeb\xff\xd8\xff\xc5\xff\xb3\xff\xa3\xff\x95\xff\x8e\xff\x8a\xff\x8a\xff\x8c\xff\x93\xff\x9d\xff\xa9\xff\xb5\xff\xc5\xff\xd3\xff\xe2\xff\xef\xff\xfc\xff' + \
        b'\x08\x00\x14\x00!\x00-\x00:\x00E\x00O\x00W\x00]\x00b\x00b\x00`\x00[\x00Q\x00G\x008\x00(\x00\x19\x00\x08\x00\xf8\xff\xeb\xff\xe1\xff\xd5\xff\xcc\xff\xc4\xff\xbe\xff\xb9\xff\xb6\xff\xb3\xff\xb3\xff\xb1\xff\xb2\xff\xb5\xff\xba\xff\xc1\xff\xcb\xff\xd6\xff\xe2\xff\xf0\xff' + \
        b'\xfe\xff\x0c\x00\x1a\x00%\x000\x008\x00=\x00@\x00A\x00A\x00>\x00=\x009\x005\x00/\x00)\x00#\x00\x1b\x00\x14\x00\x0b\x00\x00\x00\xf7\xff\xed\xff\xe2\xff\xd8\xff\xce\xff\xc7\xff\xc3\xff\xbf\xff\xbe\xff\xbf\xff\xc2\xff\xc6\xff\xce\xff\xd4\xff\xdc\xff\xe4\xff\xec\xff\xf2' + \
        b'\xff\xf9\xff\x00\x00\x06\x00\r\x00\x13\x00\x19\x00\x1f\x00$\x00)\x00,\x00.\x000\x00.\x00,\x00(\x00"\x00\x1c\x00\x14\x00\r\x00\x05\x00\xfd\xff\xf6\xff\xf0\xff\xeb\xff\xe6\xff\xe2\xff\xdf\xff\xdd\xff\xda\xff\xda\xff\xd9\xff\xd8\xff\xd9\xff\xdb\xff\xdc\xff\xe0\xff\xe3' + \
        b'\xff\xe8\xff\xef\xff\xf3\xff\xfb\xff\x02\x00\x08\x00\r\x00\x12\x00\x16\x00\x19\x00\x1a\x00\x1a\x00\x1b\x00\x1a\x00\x19\x00\x18\x00\x16\x00\x14\x00\x11\x00\x0f\x00\x0c\x00\x08\x00\x03\x00\x00\x00\xfc\xff\xf8\xff\xf4\xff\xef\xff\xeb\xff\xe8\xff\xe5\xff\xe3\xff\xe3\xff' + \
        b'\xe4\xff\xe4\xff\xe7\xff\xe9\xff\xed\xff\xef\xff\xf2\xff\xf6\xff\xf8\xff\xfb\xff\xfe\xff\x00\x00\x03\x00\x06\x00\x07\x00\n\x00\x0c\x00\x0e\x00\x0f\x00\x10\x00\x10\x00\x10\x00\x0f\x00\r\x00\r\x00\n\x00\x08\x00\x04\x00\x01\x00\xfe\xff\xfc\xff\xfb\xff\xf9\xff\xf7\xff' + \
        b'\xf6\xff\xf4\xff\xf3\xff\xf3\xff\xf3\xff\xf3\xff\xf2\xff\xf2\xff\xf3\xff\xf4\xff\xf4\xff\xf6\xff\xf6\xff\xf9\xff\xfb\xff\xfc\xff\xff\xff\x01\x00\x03\x00\x04\x00\x05\x00\x06\x00\x06\x00\x07\x00\x06\x00\x07\x00\x06\x00\x06\x00\x04\x00\x04\x00\x03\x00\x03\x00\x02\x00' + \
        b'\x01\x00\xff\xff\x00\x00\xfe\xff\xfd\xff\xfc\xff\xfb\xff\xfa\xff\xf9\xff\xf8\xff\xf8\xff\xf7\xff\xf8\xff\xf9\xff\xf8\xff\xf9\xff\xfb\xff\xfa\xff\xfb\xff\xfc\xff\xfd\xff\xfe\xff\xfe\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x02\x00\x01\x00\x02\x00' + \
        b'\x01\x00\x02\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\xff\xff\xfe\xff\xff\xff\xfd\xff\xfe\xff\xfe\xff\xfd\xff\xfc\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfc\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\xff\xff\xff\xff' + \
        b'\x00\x00\xfe\xff\x00\x00\x00\x00\xfe\xff\xfe\xff\x00\x00\xff\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xfe\xff\xfe\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\xfd\xff\xfe\xff\xfd\xff\xfe\xff\xff\xff\xfe\xff\xfe\xff' + \
        b'\xfe\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xfe\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xff\xff\xfe\xff\xff\xff'

