from PIL import Image, ImageDraw, ImageFont

class tulis:
    """
    listOrText : String
    """
    def __init__(self, listOrText):
        self.text = listOrText
        self.output = []
    def tulis(self):
        img, font, kata, tempkata=Image.open("lib/textmaker/pemandangan.jpg"), ImageFont.truetype("lib/textmaker/font.ttf",55),'',''
        draw=ImageDraw.Draw(img)
        if type(self.text) is not list:
            self.output=[]
            for i in self.text:
                if draw.textsize(tempkata, font)[0] < 850:
                    tempkata+=i
                else:
                    kata, tempkata=kata+'%s\n'%tempkata, i
            if tempkata:
                kata+="%s"%tempkata
            spliter=kata.split("\n")
        else:
            spliter=self.text
        line=113
        for i in spliter[:56]:
            draw.text((40, int(line)), i, font=font, fill=("white")) #selisih = Line
            line+=66 + 4.0
        self.output.append(img)
        if len(spliter) > 66:
            self.output+=tulis(spliter[66:]).tulis()
        return self.output
    def __repr__(self):
        return "<length: %s char>"%len(self.text)
