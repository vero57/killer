import pyautogui
import time

pertanyaan1 = input('Sebelum menjalankan program, apakah anda yakin?: Jawab "iya" atau "tidak" ')
if pertanyaan1 == 'iya':
    print('Pertanyaan terakhir')
    killer = ["neofetch"]
    for text in killer:
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(1)
        break
else:
    print('Jika berubah pikiran silahkan jalankan program lagi')




    
    