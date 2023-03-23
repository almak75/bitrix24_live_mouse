import win32api, win32con
import time
import streamlit as st
st.write('Просто оставьте эту страниццу открытой')
st.write('Битрикс будет думать, что Вы работаете')
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
while True:
    click(10,10)
    time.sleep(60)
    click(11,10)
    time.sleep(60)
