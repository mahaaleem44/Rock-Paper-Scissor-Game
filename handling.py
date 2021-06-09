f=open ("handling.txt","w")
f.write("#Reference by (https://www.youtube.com/watch?v=WexB24-_KCM&ab_channel=ADV.LEARNINGADV.LEARNING)\n\n\n")
f.write("from tkinter import *\n")
f.write("from PIL import Image,ImageTk\n")
f.write("from random import randint\n\n")

f.write("# main window\n")
f.write("root = Tk()\n")
f.write("root.title('Rock Paper Scissor')\n")
f.write("root.configure(background='yellow')\n\n\n")

f.write("#picture\n")
f.write("rock_img = ImageTk.PhotoImage(Image.open('rock-user.png'))\n")
f.write("paper_img = ImageTk.PhotoImage(Image.open('paper-user.png'))\n")
f.write("scissor_img = ImageTk.PhotoImage(Image.open('scissor-user.png'))\n")
f.write("rock_img_comp = ImageTk.PhotoImage(Image.open('rock.png'))\n")
f.write("paper_img_comp = ImageTk.PhotoImage(Image.open('paper.png'))\n")
f.write("scissor_img_comp = ImageTk.PhotoImage(Image.open('scissor.png'))\n\n\n")                             

f.write("#insert picture\n")
f.write("user_label = Label(root, image=scissor_img,bg='purple')\n")
f.write("comp_label = Label(root, image=scissor_img_comp,bg='purple')\n")
f.write("comp_label.grid(row=1, column=0)\n")
f.write("user_label.grid(row=1, column=4)\n\n\n")

f.write("#scores\n")
f.write("playerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')\n")
f.write("computerScore = Label(root, text=0, font=100, bg='#9b59b6', fg='white')\n")
f.write("computerScore.grid(row=1, column=1)\n")
f.write("playerScore.grid(row=1, column=3)\n\n\n")

f.write("#indicators\n")
f.write("user_indicator = Label(root, font=50, text='USER')\n")
f.write("comp_indicator = Label(root, font=50, text='COMPUTER')\n")
f.write("user_indicator.grid(row=0, column=3)\n")
f.write("comp_indicator.grid(row=0, column=1)\n\n\n")

f.write("#messages\n")
f.write("msg = Label(root, font=50,bg='#9b59b6',fg='white')\n")
f.write("msg.grid(row=3, column=2)\n\n\n")

f.write("#update message\n")
f.write("def updateMessage(x):\n")
f.write("msg['text'] = x\n\n\n")

f.write("#update user score\n")
f.write("def updateUserScore():\n")
f.write("score = int(playerScore['text'])\n")
f.write("score += 1\n")
f.write("playerScore['text'] = str(score)\n\n\n")

f.write("#update computer score\n")   
f.write("def updateCompScore():\n")
f.write("score = int(computerScore['text'])\n")
f.write("score += 1\n")
f.write("computerScore['text'] = str(score)\n\n\n")


f.write("#check winner\n")
f.write("def checkWin(player,computer):\n")
f.write("if player == computer:\n")
f.write("updateMessage('It's a tie!!!')\n")
f.write("elif player == 'rock':\n")
f.write("if computer == 'paper':\n")
f.write("updateMessage('You loose)\n")
f.write("updateCompScore()\n")
f.write("else:\n")
f.write("updateMessage('You Win')\n")
f.write("updateUserScore()\n")
f.write("elif player == 'paper':\n")
f.write("if computer == 'scissor':\n")
f.write("updateMessage('You loose')\n")
f.write("updateCompScore()\n")
f.write("else:\n")
f.write("updateMessage('You Win')\n")
f.write("updateUserScore()\n")
f.write("elif player == 'scissor':\n")
f.write("if computer == 'rock':\n")
f.write("updateMessage('You loose')\n")
f.write("updateCompScore()\n")
f.write("else:\n")
f.write("updateMessage('You Win')\n")
f.write("updateUserScore()\n")
f.write("else:\n")
f.write("pass\n\n\n")


f.write("#update choices\n")
f.write("choices = ['rock','paper','scissor']\n")
f.write("def updateChoice(x):\n\n\n")

f.write("#for computer\n")
f.write("if compChoice == 'rock':\n")
f.write("comp_label.configure(image=rock_img_comp)\n")
f.write("elif compChoice == 'paper':\n")
f.write("comp_label.configure(image=paper_img_comp)\n")
f.write("else:\n")
f.write("comp_label.configure(image=scissor_img_comp)\n\n\n")
        
f.write("#for user\n")
f.write("if x == 'rock':\n")
f.write("user_label.configure(image=rock_img)\n")
f.write("elif x == 'paper':\n")
f.write("user_label.configure(image=paper_img)\n")
f.write("else:\n")
f.write("user_label.configure(image=scissor_img)\n")
f.write("checkWin(x,compChoice)\n\n\n")
        
f.write("#buttons\n")
f.write("rock = Button(root, width=20, height=2,text='ROCK', bg='#FF3E4D', fg='white', command = lambda: updateChoice('rock')).grid(row=2,column=1)\n")
f.write("paper = Button(root, width=20, height=2,text='PAPER', bg='#FAD02E', fg='white', command = lambda: updateChoice('paper')).grid(row=2,column=2)\n")
f.write("scissor = Button(root, width=20, height=2,text='SCISSOR', bg='#0ABDE3', fg='white', command = lambda: updateChoice('scissor')).grid(row=2,column=3)\n\n\n")




f.write("root.mainloop()\n\n\n")



f.close()

