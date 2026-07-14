import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.title("Tic Tac Toe")
root.geometry("420x520")
root.configure(bg="#222222")
root.resizable(False,False)

current_player="X"
board=[""]*9
buttons=[]
score_x=0
score_o=0

title=tk.Label(root,text="TIC TAC TOE",font=("Arial",22,"bold"),bg="#222222",fg="white")
title.pack(pady=10)
turn_label=tk.Label(root,text="Player X Turn",font=("Arial",16),bg="#222222",fg="yellow")
turn_label.pack()
score_label=tk.Label(root,text="X : 0    O : 0",font=("Arial",16),bg="#222222",fg="white")
score_label.pack(pady=10)
frame=tk.Frame(root,bg="#222222")
frame.pack()

wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def update_score():
    score_label.config(text=f"X : {score_x}    O : {score_o}")

def reset_board():
    global board,current_player
    board=[""]*9
    current_player="X"
    turn_label.config(text="Player X Turn")
    for b in buttons:
        b.config(text="",bg="white",state="normal")

def check_winner():
    for a,b,c in wins:
        if board[a]==board[b]==board[c]!="":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return board[a]
    return None

def check_draw():
    return "" not in board

def end_game(msg):
    messagebox.showinfo("Game Over",msg)
    reset_board()

def click(i):
    global current_player,score_x,score_o
    if board[i]!="":
        return
    board[i]=current_player
    buttons[i]["text"]=current_player
    buttons[i]["fg"]="red" if current_player=="X" else "blue"
    w=check_winner()
    if w:
        if w=="X": score_x+=1
        else: score_o+=1
        update_score()
        root.after(300,lambda:end_game(f"Player {w} wins!"))
        return
    if check_draw():
        root.after(300,lambda:end_game("Draw!"))
        return
    current_player="O" if current_player=="X" else "X"
    turn_label.config(text=f"Player {current_player} Turn")

for i in range(9):
    btn=tk.Button(frame,text="",width=5,height=2,font=("Arial",24,"bold"),
                  bg="white",command=lambda i=i:click(i))
    btn.grid(row=i//3,column=i%3,padx=4,pady=4)
    buttons.append(btn)

def reset_scores():
    global score_x,score_o
    score_x=0
    score_o=0
    update_score()
    reset_board()

tk.Button(root,text="New Game",font=("Arial",14),command=reset_board).pack(pady=8)
tk.Button(root,text="Reset Scores",font=("Arial",14),command=reset_scores).pack()

root.mainloop()
# Practice line 91
# Practice line 92
# Practice line 93
# Practice line 94
# Practice line 95
# Practice line 96
# Practice line 97
# Practice line 98
# Practice line 99
# Practice line 100
# Practice line 101
# Practice line 102
# Practice line 103
# Practice line 104
# Practice line 105
# Practice line 106
# Practice line 107
# Practice line 108
# Practice line 109
# Practice line 110
# Practice line 111
# Practice line 112
# Practice line 113
# Practice line 114
# Practice line 115
# Practice line 116
# Practice line 117
# Practice line 118
# Practice line 119
# Practice line 120
# Practice line 121
# Practice line 122
# Practice line 123
# Practice line 124
# Practice line 125
# Practice line 126
# Practice line 127
# Practice line 128
# Practice line 129
# Practice line 130
# Practice line 131
# Practice line 132
# Practice line 133
# Practice line 134
# Practice line 135
# Practice line 136
# Practice line 137
# Practice line 138
# Practice line 139
# Practice line 140
# Practice line 141
# Practice line 142
# Practice line 143
# Practice line 144
# Practice line 145
# Practice line 146
# Practice line 147
# Practice line 148
# Practice line 149
# Practice line 150
# Practice line 151
# Practice line 152
# Practice line 153
# Practice line 154
# Practice line 155
# Practice line 156
# Practice line 157
# Practice line 158
# Practice line 159
# Practice line 160
# Practice line 161
# Practice line 162
# Practice line 163
# Practice line 164
# Practice line 165
# Practice line 166
# Practice line 167
# Practice line 168
# Practice line 169
# Practice line 170
# Practice line 171
# Practice line 172
# Practice line 173
# Practice line 174
# Practice line 175
# Practice line 176
# Practice line 177
# Practice line 178
# Practice line 179
# Practice line 180
# Practice line 181
# Practice line 182
# Practice line 183
# Practice line 184
# Practice line 185
# Practice line 186
# Practice line 187
# Practice line 188
# Practice line 189
# Practice line 190
# Practice line 191
# Practice line 192
# Practice line 193
# Practice line 194
# Practice line 195
# Practice line 196
# Practice line 197
# Practice line 198
# Practice line 199
# Practice line 200