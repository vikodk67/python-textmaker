from PIL import Image, ImageDraw, ImageFont
from numpy import random

class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        gambaran = random.choice(['lib/textmaker2/gambar.jpg', 'lib/textmaker2/gambar2.jpg', 'lib/textmaker2/gambar3.jpg', 'lib/textmaker2/gambar4.jpg',])
        img, font, kata, tempkata=Image.open(gambaran), ImageFont.truetype("lib/textmaker2/KeepCalm-Medium.ttf",25),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 420:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=270
        for i in spliter[:56]:
            draw.text((30, int(line)), i, font=font, fill=("white")) #selisih = Line
            line+=18 + 21
        self.output.append(img)
        if len(spliter) > 80:
            self.output+=tulis(spliter[80:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
