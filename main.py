#0901
#experimental
import random
import cv2
import pyperclip
import numpy as np
import pyautogui
import time
from PIL import ImageGrab
from pynput import keyboard
import pygame


# Флаг для отслеживания состояния
active = False


pygame.mixer.init()

text_to_copy = "/start"
pyperclip.copy(text_to_copy)
def locate_image_on_screen(template_path):
    # Снимок экрана
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)

    # Шаблон изображения
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    # Поиск шаблона на экране
    res = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.93

    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return (pt[0] + w / 2, pt[1] + h / 2)
    return None


def click_on_image(image_path):
    location = locate_image_on_screen(image_path)
    if location:
        pyautogui.click(location)

def scenario0():
    click_on_image('clickbee3.png')
    time.sleep(1)
    click_on_image('back.png')
    function_calls = [
        lambda: click_on_image('joinbots.png'),
        lambda: click_on_image('visitsites.png'),
        lambda: click_on_image('joinchannels.png'),
    ]
    time.sleep(1)
    random.shuffle(function_calls)




    for func in function_calls:
        func()

    time.sleep(2)

    if locate_image_on_screen('joined.png'):
        scenario2()
    elif locate_image_on_screen('gotosite.png'):
        scenario1()
    elif locate_image_on_screen('startthebot.png'):
        scenario3()
    else:
        click_on_image('back.png')

def scenario1():
    time.sleep(0.5)
    click_on_image('gotosite.png')
    time.sleep(0.5)
    click_on_image('open.png')
    time.sleep(4)
    start_time = time.time()
    timeout = 93  # Тайм-аут в секундах
    while time.time() - start_time < timeout:
        if locate_image_on_screen('stay.png'):
            time.sleep(1)
        else:

            break  # Прерываем цикл, если изображение больше не найдено

    # pyautogui.hotkey('alt', 'tab')
    # pyautogui.click(270, 1060, button='left')
    if locate_image_on_screen('visitsitestrap.png'):
        click_on_image('visitsitestrap.png')
        time.sleep(1)
        if locate_image_on_screen('closeanyway.png'):
            click_on_image('closeanyway.png')
    if locate_image_on_screen('launch.png'):
        click_on_image('clickbee3.png')

        time.sleep(1)
    time.sleep(1)
    if locate_image_on_screen('tgtray.png'):
        click_on_image('tgtray.png')
    else:
        click_on_image('tgtray2.png')
        time.sleep(1)
        click_on_image('skipsites.png')
    #else:
       # pyautogui.click(270, 1060, button='left')
        #click_on_image('skip.png')
    time.sleep(3)

    if locate_image_on_screen('bylaunchingthis.png'):
        pyautogui.click(1400, 450, button='left')

    time.sleep(2)
    while(not(locate_image_on_screen('clickbeeisopen.png'))):
        click_on_image('tgtray2.png')
        time.sleep(0.5)
        click_on_image('clickbee.png')
        time.sleep(0.5)
        click_on_image('back.png')
        time.sleep(1)

    if locate_image_on_screen('wouldliketoopen.png'):
        pyautogui.click(1400, 450, button='left')
        time.sleep(1)

    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()


def scenario2():
    if locate_image_on_screen('jointhechannel.png'):
        click_on_image('jointhechannel.png')
    time.sleep(1)
    if locate_image_on_screen('moreaboutthisbot.png'):
        pyautogui.click(1400, 450, button='left')
        time.sleep(1)
        click_on_image('joined.png')
    if locate_image_on_screen('isexpired.png'):
        click_on_image('ok.png')
        time.sleep(1)
        click_on_image('skip.png')
        return
    if locate_image_on_screen('requesttojoin.png'):
        click_on_image('requesttojoin.png')
        time.sleep(1)
        click_on_image('joined.png')
    if locate_image_on_screen('joinchannel.png'):
        pyautogui.click(1400, 450, button='left')
        time.sleep(1)
        click_on_image('joinchannel.png')
    if locate_image_on_screen('alreadyjoined.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('joined.png')
    if locate_image_on_screen('joingroup.png'):
        click_on_image('joingroup.png')
        time.sleep(0.7)
    time.sleep(0.3)
    if locate_image_on_screen('mute.png'):
        click_on_image('mute.png')
        time.sleep(0.3)
    click_on_image('clickbee.png')
    time.sleep(1)
    click_on_image('joined.png')
    time.sleep(1)
    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beepchannels.wav')
        pygame.mixer.music.play()
        pyautogui.click(1400, 450, button='left')
        time.sleep(1)
        click_on_image('back.png')

def scenario3():

    time.sleep(1)
    click_on_image('thistelegrambot.png')
    time.sleep(1)
    click_on_image('3dots.png')
    # click_on_image('3dots2.png')
    time.sleep(1)
    click_on_image('openbot.png')
    time.sleep(1)
    click_on_image('moreaboutthisbot.png')
    time.sleep(1)
    if locate_image_on_screen('joinchannel.png') or locate_image_on_screen('videochat.png') or locate_image_on_screen('retardbot1.png') or locate_image_on_screen('joingroup.png') or locate_image_on_screen('retardbot2.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('skip.png')
        return
    if locate_image_on_screen('unmute.png'):
        click_on_image('clickbee.png')
        time.sleep(1)
        click_on_image('skip.png')
        time.sleep(1)
        if locate_image_on_screen('skipohno.png'):
            click_on_image('back.png')
            backwait = locate_image_on_screen('backwait.png')
            while backwait:
                time.sleep(0.5)
                backwait = locate_image_on_screen('backwait.png')
        return
    if locate_image_on_screen('launch.png'):
        click_on_image('launch.png')
        time.sleep(3)
        click_on_image('3dots.png')
        #click_on_image('3dots2.png')
        time.sleep(1)
        click_on_image('openbot.png')
        time.sleep(1)

    time.sleep(1)

    if locate_image_on_screen('start.png'):
        click_on_image('start.png')
        time.sleep(1)
        click_on_image('start.png')
        time.sleep(5)

    if locate_image_on_screen('youallowed.png'):
        for q in range(3):
            click_on_image('writeamessage.png')

            for qw in range(4):
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                pyperclip.paste()


                #pyautogui.typewrite('/start')
                time.sleep(1)  # Небольшая пауза перед нажатием Enter
                pyautogui.press('enter')
            time.sleep(1)

    location = locate_image_on_screen('botrespond.png')
    location2 = locate_image_on_screen('botrespond2.png')
    location3 = locate_image_on_screen('botrespond3.png')
    location5 = locate_image_on_screen('botrespond5.png')
    location6 = locate_image_on_screen('botrespond6.png')
    location7 = locate_image_on_screen('botrespond4.png')

    if location5:
        x, y = location5
        pyautogui.click(x, y, button='right')
        time.sleep(0.5)
        forwardlocation = locate_image_on_screen('forward.png')
        if forwardlocation:
            click_on_image('forward.png')
        else:
            time.sleep(0.5)
            click_on_image('clickbee3.png')
            time.sleep(0.5)
            click_on_image('clickbee.png')
            time.sleep(0.5)
            click_on_image('skip.png')
            return

        time.sleep(0.5)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        if locate_image_on_screen('congratulations.png'):
            pygame.mixer.music.load('beepbots.wav')
            pygame.mixer.music.play()

        return
    elif location2:
        x, y = location2
        pyautogui.click(x, y, button='right')
        time.sleep(0.5)

        forwardlocation = locate_image_on_screen('forward.png')
        if forwardlocation:
            click_on_image('forward.png')
        else:
            time.sleep(0.5)
            click_on_image('clickbee3.png')
            time.sleep(0.5)
            click_on_image('clickbee.png')
            time.sleep(0.5)
            click_on_image('skip.png')
            return
        time.sleep(0.5)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        if locate_image_on_screen('congratulations.png'):
            pygame.mixer.music.load('beepbots.wav')
            pygame.mixer.music.play()

        return
    elif location7:
        x, y = location7
        pyautogui.click(x, y, button='right')
        time.sleep(0.5)
        forwardlocation = locate_image_on_screen('forward.png')
        if forwardlocation:
            click_on_image('forward.png')
        else:
            time.sleep(0.5)
            click_on_image('clickbee3.png')
            time.sleep(0.5)
            click_on_image('clickbee.png')
            time.sleep(0.5)
            click_on_image('skip.png')
            return

        time.sleep(0.5)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        if locate_image_on_screen('congratulations.png'):
            pygame.mixer.music.load('beepbots.wav')
            pygame.mixer.music.play()

        return
    elif location:
        x, y = location
        pyautogui.click(x + 50, y, button='right')
        time.sleep(0.5)
        forwardlocation = locate_image_on_screen('forward.png')
        if forwardlocation:
            click_on_image('forward.png')
        else:
            time.sleep(0.5)
            click_on_image('clickbee3.png')
            time.sleep(0.5)
            click_on_image('clickbee.png')
            time.sleep(0.5)
            click_on_image('skip.png')
            return

        time.sleep(0.5)
        click_on_image('clickbee2.png')
        time.sleep(1)
        click_on_image('started.png')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        if locate_image_on_screen('congratulations.png'):
            pygame.mixer.music.load('beepbots.wav')
            pygame.mixer.music.play()

        return

    time.sleep(1)


    if locate_image_on_screen('norespond.png') or locate_image_on_screen('norespond2.png'):
        pyautogui.click(1600, 300, button='left')
        time.sleep(0.9)
        click_on_image('clickbee3.png')
        time.sleep(0.9)
        click_on_image('clickbee.png')
        time.sleep(0.7)
        click_on_image('skip.png')
        time.sleep(2)
        if locate_image_on_screen('skipohno.png'):
            click_on_image('back.png')
            backwait = locate_image_on_screen('backwait.png')
            while backwait:
                time.sleep(0.5)
                backwait = locate_image_on_screen('backwait.png')
        return
    else:

        time.sleep(1)

    #location = locate_image_on_screen('botrespond.png')

    #time.sleep(1)
    if locate_image_on_screen('forward.png'):
        click_on_image('forward.png')
    else:
        pyautogui.click(1600, 300, button='left')
        time.sleep(0.5)
        click_on_image('clickbee.png')
        time.sleep(0.7)
        click_on_image('clickbee3.png')
        time.sleep(0.7)
        click_on_image('skip.png')
        return
    time.sleep(1)
    click_on_image('clickbee2.png')
    time.sleep(1)
    click_on_image('started.png')
    pyautogui.press('enter')
    time.sleep(1)
    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beepbots.wav')
        pygame.mixer.music.play()
    if locate_image_on_screen('skipohno.png'):
        click_on_image('back.png')
        backwait = locate_image_on_screen('backwait.png')
        while backwait:
            time.sleep(0.5)
            backwait = locate_image_on_screen('backwait.png')

        return
    time.sleep(1)

    if locate_image_on_screen('congratulations.png'):
        pygame.mixer.music.load('beepbots.wav')
        pygame.mixer.music.play()
        time.sleep(1)

def scenario4():
    # Добавьте реализацию четвертого сценария здесь
    time.sleep(1)
    click_on_image('back.png')
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('viewposts.png')
    time.sleep(1)
    if locate_image_on_screen('ohnoposts.png'):
        click_on_image('back.png')
        return
    else:
        time.sleep(1)
        if not (locate_image_on_screen('watched.png')):
            pyautogui.click(700, 500, button='right')
            time.sleep(0.5)
            click_on_image('delete.png')
            time.sleep(0.5)
            click_on_image('delete2.png')
        time.sleep(11)
        click_on_image('watched.png')
        time.sleep(1)
        if locate_image_on_screen('congratulations.png'):
            pygame.mixer.music.load('beepposts.wav')
            pygame.mixer.music.play()
            time.sleep(1)
        scenario4()


def scenario5():
    time.sleep(1)
    click_on_image('back.png')
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('twitterraids.png')
    time.sleep(1)
    click_on_image('tweettoearn.png')
    time.sleep(1)
    if locate_image_on_screen('ohnotwitter.png'):
        click_on_image('back.png')
        return
    if locate_image_on_screen('openprofile.png'):
        while True:
            pygame.mixer.music.load('beeptweettoearn.wav')
            pygame.mixer.music.play()
            time.sleep(0.5)

def scenario6():
    time.sleep(1)
    click_on_image('back.png')
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('twitterraids.png')
    time.sleep(1)
    click_on_image('follow.png')
    time.sleep(1)
    if locate_image_on_screen('ohnotwitter.png'):
        click_on_image('back.png')
        return
    if locate_image_on_screen('openprofile.png'):
        while True:
            pygame.mixer.music.load('beepfollow.wav')
            pygame.mixer.music.play()
            time.sleep(0.5)
def scenario7():
    time.sleep(1)
    click_on_image('back.png')
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('twitterraids.png')
    time.sleep(1)
    click_on_image('retweet.png')
    time.sleep(1)
    if locate_image_on_screen('ohnotwitter.png'):
        click_on_image('back.png')
        return
    if locate_image_on_screen('openprofile.png'):
        while True:
            pygame.mixer.music.load('beepretweet.wav')
            pygame.mixer.music.play()
            time.sleep(0.5)
def scenario8():
    time.sleep(1)
    click_on_image('back.png')
    time.sleep(1)
    click_on_image('more.png')
    time.sleep(1)
    click_on_image('twitterraids.png')
    time.sleep(1)
    click_on_image('comment.png')
    time.sleep(1)
    if locate_image_on_screen('ohnotwitter.png'):
        click_on_image('back.png')
        return
    if locate_image_on_screen('openprofile.png'):
        while True:
            pygame.mixer.music.load('beepcomment.wav')
            pygame.mixer.music.play()
            time.sleep(0.5)

def on_press(key):
    global active
    if key == keyboard.Key.space:
        active = not active
        print(f"{'Начало' if active else 'Остановка'} выполнения сценариев.")

def main():

    print("starting in 5 sec...")

    time.sleep(5)
    active = True


    while True:
        if active:
            scenario0()
            time.sleep(1)
        else:
            time.sleep(1)


if __name__ == "__main__":
    main()
