from tkinter import ttk
import tkinter as tk
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def login(username, password, text1, text2):
    browser = webdriver.Chrome(executable_path="chromedriver.exe")
    # browser = webdriver.Chrome()
    browser.get(
        'https://id.zalo.me/account?continue=https%3A%2F%2Fchat.zalo.me%2F%3Fnull')
    sleep(2)
    phoneclick = browser.find_element(By.XPATH,
                                      '/html/body/div[1]/div/div/div[2]/div[2]/div[1]/ul/li[2]')
    phoneclick.click()
    phonelink = browser.find_element('id', 'input-phone')
    phonelink.send_keys(username)
    passwordlink = browser.find_element("xpath",
                                        '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/input')
    passwordlink.send_keys(password)
    submit = browser.find_element("xpath",
                                  '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div/div/div/div[4]/a')

    submit.click()
    sleep(20)
    while True:
        user1 = browser.find_element("xpath",
                                     '/html/body/div/div/div[2]/nav/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div[4]')
        user1.click()
        sleep(3)
        #  send text
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text1)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)
        #  send text
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text1)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)
        #  send text
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text1)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)

        #  send text 2
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text2)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)
        #  send text 2
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text2)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)
        #  send text 2
        inputtext = browser.find_element(By.ID, 'input_line_0')
        inputtext.send_keys(text2)

        btnsend = browser.find_element("xpath",
                                       '/html/body/div/div/div[2]/main/div/article/div[4]/div[3]/div/div/div/div/div[2]/div[5]')
        btnsend.click()
        sleep(1)

        # outgroup
        findoutbtn = browser.find_element(
            "xpath", '/html/body/div/div/div[2]/main/div/header/div[2]/div[4]')
        findoutbtn.click()
        sleep(2)

        btnout = browser.find_element(
            "xpath", '/html/body/div/div/div[2]/main/aside/div[2]/div[2]/div/div/div[1]/div/div[9]/div[5]')
        btnout.click()
        # sleep(1)

        confirmbtn = browser.find_element(
            "xpath", '/html/body/div[2]/div/div/div[3]/div/div/div[2]')
        confirmbtn.click()
        sleep(2)


def create_main_window():
    root = tk.Tk()
    root.title('Zalo auto')
    root.geometry('700x250')
    root.resizable(0, 0)
    root.attributes('-toolwindow', True)
# input
    ttk.Label(root, text='Phone:').grid(column=0, row=0, sticky=tk.W)
    phone = ttk.Entry(root, width=70)
    phone.focus()
    phone.grid(column=1, row=1, sticky=tk.E)
    ttk.Label(root, text='Password:').grid(column=0, row=2, sticky=tk.W)
    password = ttk.Entry(root, width=70)
    password.grid(column=1, row=3, sticky=tk.W)

    ttk.Label(root, text='Text1:').grid(column=0, row=4, sticky=tk.W)
    text1 = ttk.Entry(root, width=70)
    text1.grid(column=1, row=5, sticky=tk.W)

    ttk.Label(root, text='Text 2:').grid(column=0, row=6, sticky=tk.W)
    text2 = ttk.Entry(root, width=70)
    text2.grid(column=1, row=7, sticky=tk.W)

    def submit():
        login(phone.get(), password.get(), text1.get(), text2.get())

    ttk.Button(root, text='RUN', command=submit).grid(column=2, row=11)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
