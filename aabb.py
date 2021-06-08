import tkinter as tk
import random



window = tk.Tk()
window.title('猜數字')
window.geometry('800x600')
window.configure(background='Pale Goldenrod')

ans = []
ans = random.sample('123456789', 4)

ansli = []
time = 0
def ab():
    global time
    time = time + 1
    counta = 0
    countb = 0
    gue = num_entry.get()
    ansli.append(gue)
    g = []
    for ii in gue:
        g.append(ii)
    if len(g) != 4:
        result = '請輸入四位數字'
    elif len(g) == 4 :
        for ii in range(0, 4):
            if g[ii] == ans[ii]:
                counta += 1
                continue
            for iii in range(0, 4):
                if g[ii] == ans[iii]:
                    countb += 1
                 
        result = '{}A{}B\n 答案是{}\n歷史紀錄為{}'.format(counta, countb, ans,ansli)
        if counta == 4:
            result = '恭喜你答對了'
    result_label.configure(text=result)



header_label = tk.Label(window, text='猜AB', font=('Arial', 30))
num_label = tk.Label(window, text='輸入', font=('Arial', 30))
num_entry = tk.Entry(window, font=('Arial', 30))
calculate_btn = tk.Button(window, text='馬上猜', command = ab , font=('Arial', 30))
result_label = tk.Label(window, font=('Arial', 20), width=30, height=3)

header_label.grid(row=0, column=0, columnspan=2)
num_label.grid(row=1, column=0)
num_entry.grid(row=1, column=1)
calculate_btn.grid(row=3, column=0)
result_label.grid(row=3, column=1)


window.mainloop()
