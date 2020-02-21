from PIL import Image
from PIL import ImageGrab


class Picture():
    def __init__(self,Image_path):
        self.Image_path =Image_path

#图片对比，传入图片展示列表
    def write_picture(self,name):
        """
        :param name: 传入图片的名称
        :return:
        """
        picture = Image.open(self.Image_path+name)
        return picture.histogram()

#截图
    def shot_picture(self,name):
        """
        :param name: 传入图片的名称
        :return:
        """
        image = ImageGrab.grab()
        image.save(self.Image_path+name)


# a = Picture("C:/Users\Administrator\Desktop/tp/")
# print(a.write_picture("tu.png"))