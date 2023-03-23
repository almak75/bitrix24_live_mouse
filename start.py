#import win32api, win32con
import time
import streamlit as st
import pyautogui

st.write('Просто оставьте эту страниццу открытой')
st.write('Битрикс будет думать, что Вы работаете')

while True:
    #click(10,10)
    pyautogui.click(10, 10)
    time.sleep(60)
    pyautogui.click(10, 10)
   
    time.sleep(60)

    
