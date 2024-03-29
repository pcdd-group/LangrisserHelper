import os
import time
from datetime import datetime

import pyautogui

from src.common.constants import Consts


class PAGUtils:

    @staticmethod
    def click_img(img, retry=True):
        while True:
            # 获取图片定位，当grayscale=True时会使图像和屏幕截图中的颜色去饱和，解决由于显示器饱和度不同从而引起的颜色细微差异因而导致的图像定位失败问题。
            try:
                location = pyautogui.locateCenterOnScreen(img, confidence=0.8, grayscale=True)
                # 单击坐标位置，duration表示移动光标的耗时
                pyautogui.click(location.x, location.y, duration=0.2)
                return True
            # pyautogui 0.9.41 前，找不到图像返回 None，之后改为抛 ImageNotFoundException 异常
            except pyautogui.ImageNotFoundException:
                if retry:
                    print('未匹配到样本图片：%s，1秒后重试' % img)
                    time.sleep(1)
                else:
                    break

    @staticmethod
    def click_imgs(img1, img2):
        retry_num = 0
        while True:
            try:
                location = pyautogui.locateCenterOnScreen(img1)
                pyautogui.click(location.x, location.y, duration=0.2)
                return True
            except pyautogui.ImageNotFoundException:
                try:
                    print('样本图片 1 未匹配 {}，1 秒后尝试匹配图片 2（第 {} 次重试）'.format(img1, retry_num))
                    time.sleep(1)
                    location = pyautogui.locateCenterOnScreen(img2, confidence=0.8, grayscale=True)
                    pyautogui.click(location.x, location.y, duration=0.2)
                    return True
                except pyautogui.ImageNotFoundException:
                    print('样本图片 2 未匹配 {}，1 秒后尝试匹配图片 1（第 {} 次重试）'.format(img2, retry_num))
                    retry_num += 1
                    time.sleep(1)

    @staticmethod
    def img_exists(img):
        try:
            pyautogui.locateCenterOnScreen(img, confidence=0.8, grayscale=True)
            return True
        except pyautogui.ImageNotFoundException:
            return False

    @staticmethod
    def scroll(val, n):
        # 屏幕尺寸
        width, height = pyautogui.size()
        pyautogui.moveTo(width / 2, height / 2, duration=0.2)
        time.sleep(1)
        for _ in range(n):
            pyautogui.scroll(val)

    # 点击最高等级（最下方）的扫荡球
    @staticmethod
    def click_godless_ball():
        region_list = list(
            pyautogui.locateAllOnScreen(Consts.IMG_DAILY_PATH + 'bless_ball.png', confidence=0.7, grayscale=True))
        if len(region_list) != 0:
            region = region_list[-1]
            print(region.left, region.top)
            pyautogui.click(region.left, region.top, duration=0.2)

    @staticmethod
    def screenshot(img_name):
        path = 'screenshot/{}/'.format(datetime.now().strftime('%Y-%m-%d'))
        if not os.path.exists(path):
            os.makedirs(path)
        im1 = pyautogui.screenshot()
        im1.save(path + '{}_{}.png'.format(img_name, datetime.now().strftime("%H-%M-%S")))
