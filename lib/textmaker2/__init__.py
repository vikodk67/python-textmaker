from PIL import Image, ImageDraw, ImageFont
from numpy import random
gambaran = random.choice(['lib/textmaker2/gambar.jpg', 'lib/textmaker2/gambar2.jpg', 'lib/textmaker2/gambar3.jpg', 'lib/textmaker2/gambar4.jpg',])
class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open(gambaran), ImageFont.truetype("lib/textmaker2/Lato-Black.ttf",25),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 535:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=530
        for i in spliter[:56]:
            draw.text((50, int(line)), i, font=font, fill=("white")) #selisih = Line
            line+=17 + 19
        self.output.append(img)
        if len(spliter) > 80:
            self.output+=tulis(spliter[80:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
