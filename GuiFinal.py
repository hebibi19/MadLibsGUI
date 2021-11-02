# Villanueva, Bryan // Serrano, Marco // Molina, Jacqueline
from tkinter import *

window = Tk()
window.title("GUI Project")
window.geometry("1180x750")
window.configure(bg="black")


# -------------------------------------------------------------
# functions master list


def go_howto():
    frame2.tkraise()


def go_home():
    frame1.tkraise()
    # if home button is pressed, all entry boxes are reset for story 1
    frame3_e1.delete(0, "end")
    frame3_l3.configure(text="")
    frame4_l3.configure(text="-----")
    frame3_e2.delete(0, "end")
    frame3_l5.configure(text="")
    frame4_l6.configure(text="-----")
    frame3_e3.delete(0, "end")
    frame3_l7.configure(text="")
    frame4_l8.configure(text="-----")
    frame3_e4.delete(0, "end")
    frame3_l9.configure(text="")
    frame4_l10.configure(text="-----")
    frame3_e5.delete(0, "end")
    frame3_l11.configure(text="")
    frame4_l12.configure(text="-----")
    frame3_e6.delete(0, "end")
    frame3_l13.configure(text="")
    frame4_l14.configure(text="-----")
    frame3_e7.delete(0, "end")
    frame3_l15.configure(text="")
    frame4_l17.configure(text="-----")
    frame3_e8.delete(0, "end")
    frame3_l17.configure(text="")
    frame4_l19.configure(text="-----")
    # if home button is pressed, all entry boxes are reset for story 2
    frame5_e1.delete(0, "end")
    frame5_l3.configure(text="")
    frame6_l3.configure(text="-----")
    frame5_e2.delete(0, "end")
    frame5_l5.configure(text="")
    frame6_l7.configure(text="-----")
    frame5_e3.delete(0, "end")
    frame5_l7.configure(text="")
    frame6_l9.configure(text="-----")
    frame5_e4.delete(0, "end")
    frame5_l9.configure(text="")
    frame6_l13.configure(text="-----")
    frame5_e5.delete(0, "end")
    frame5_l11.configure(text="")
    frame6_l18.configure(text="-----")
    frame5_e6.delete(0, "end")
    frame5_l13.configure(text="")
    frame6_l21.configure(text="-----")
    # if home button is pressed, all entry boxes are reset for story 3
    frame7_e1.delete(0, "end")
    frame7_l3.configure(text="")
    frame8_l3.configure(text="-----")
    frame7_e2.delete(0, "end")
    frame7_l5.configure(text="")
    frame8_l6.configure(text="-----")
    frame7_e3.delete(0, "end")
    frame7_l7.configure(text="")
    frame8_l8.configure(text="-----")
    frame7_e4.delete(0, "end")
    frame7_l9.configure(text="")
    frame8_l10.configure(text="-----")
    frame7_e5.delete(0, "end")
    frame7_l11.configure(text="")
    frame8_l2.configure(text="-----")
    frame7_e6.delete(0, "end")
    frame7_l13.configure(text="")
    frame8_l7.configure(text="-----")
    frame7_e7.delete(0, "end")
    frame7_l15.configure(text="")
    frame8_l21.configure(text="-----")


def go_story1():
    frame3.tkraise()


def do_story1():
    frame4.tkraise()


def s1_entry():
    s1_str_var1 = frame3_e1.get()
    frame3_l3.configure(text=s1_str_var1)
    frame4_l3.configure(text=s1_str_var1)
    s1_str_var2 = frame3_e2.get()
    frame3_l5.configure(text=s1_str_var2)
    frame4_l6.configure(text=s1_str_var2)
    s1_str_var3 = frame3_e3.get()
    frame3_l7.configure(text=s1_str_var3)
    frame4_l8.configure(text=s1_str_var3)
    s1_str_var4 = frame3_e4.get()
    frame3_l9.configure(text=s1_str_var4)
    frame4_l10.configure(text=s1_str_var4)
    s1_str_var5 = frame3_e5.get()
    frame3_l11.configure(text=s1_str_var5)
    frame4_l12.configure(text=s1_str_var5)
    s1_str_var6 = frame3_e6.get()
    frame3_l13.configure(text=s1_str_var6)
    frame4_l14.configure(text=s1_str_var6)
    s1_str_var7 = frame3_e7.get()
    frame3_l15.configure(text=s1_str_var7)
    frame4_l17.configure(text=s1_str_var7)
    s1_str_var8 = frame3_e8.get()
    frame3_l17.configure(text=s1_str_var8)
    frame4_l19.configure(text=s1_str_var8)


def go_story2():
    frame5.tkraise()


def do_story2():
    frame6.tkraise()


def s2_entry():
    s2_str_var1 = frame5_e1.get()
    frame5_l3.configure(text=s2_str_var1)
    frame6_l3.configure(text=s2_str_var1)
    s2_str_var2 = frame5_e2.get()
    frame5_l5.configure(text=s2_str_var2)
    frame6_l7.configure(text=s2_str_var2)
    s2_str_var3 = frame5_e3.get()
    frame5_l7.configure(text=s2_str_var3)
    frame6_l9.configure(text=s2_str_var3)
    s2_str_var4 = frame5_e4.get()
    frame5_l9.configure(text=s2_str_var4)
    frame6_l13.configure(text=s2_str_var4)
    s2_str_var5 = frame5_e5.get()
    frame5_l11.configure(text=s2_str_var5)
    frame6_l18.configure(text=s2_str_var5)
    s2_str_var6 = frame5_e6.get()
    frame5_l13.configure(text=s2_str_var6)
    frame6_l21.configure(text=s2_str_var6)


def go_story3():
    frame7.tkraise()


def do_story3():
    frame8.tkraise()


def s3_entry():
    s3_str_var1 = frame7_e1.get()
    frame7_l3.configure(text=s3_str_var1)
    frame8_l3.configure(text=s3_str_var1)
    s3_str_var2 = frame7_e2.get()
    frame7_l5.configure(text=s3_str_var2)
    frame8_l6.configure(text=s3_str_var2)
    s3_str_var3 = frame7_e3.get()
    frame7_l7.configure(text=s3_str_var3)
    frame8_l8.configure(text=s3_str_var3)
    s3_str_var4 = frame7_e4.get()
    frame7_l9.configure(text=s3_str_var4)
    frame8_l10.configure(text=s3_str_var4)
    s3_str_var5 = frame7_e5.get()
    frame7_l11.configure(text=s3_str_var5)
    frame8_l12.configure(text=s3_str_var5)
    s3_str_var6 = frame7_e6.get()
    frame7_l13.configure(text=s3_str_var6)
    frame8_l17.configure(text=s3_str_var6)
    s3_str_var7 = frame7_e7.get()
    frame7_l15.configure(text=s3_str_var7)
    frame8_l21.configure(text=s3_str_var7)


bottom = Frame(window)
bottom.grid(row=0, column=0)
# --------------------------------------------------------------------------------------------------------------
# Story 3
frame8 = Frame(bottom, bg="Black")
frame8.grid(row=0, column=0, ipady=200, sticky="news")

# return to home
frame8_b1 = Button(frame8, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame8_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# Title label + empty label in order to separate the title from the story
frame8_empty = Label(frame8, bg="black")
frame8_empty.grid(row=0, column=1)
# enter the title of your mad libs here on frame 3
frame8_l1 = Label(frame8, text="The Crazy Dream", font=("FunSized", 35), fg="white", bg="black")
frame8_l1.grid(row=1, column=1, padx=200)

frame8_line = Label(frame8, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame8_line.grid(row=2, column=1)

# image
f8_img1 = PhotoImage(file="sleep.png")
frame8_l2 = Label(frame8, image=f8_img1, bg="black")
frame8_l2.grid(row=3, column=1, pady=5)

# # # # # Line 1
frame8_text = Frame(frame8, bg="red")
frame8_text.grid(row=4, column=1)

frame8_l2 = Label(frame8_text, text="A boy had a bizarre dream in which his house was surrounded by",
                  font=("FunSized", 20), fg="white", bg="black")
frame8_l2.grid(row=0, column=0)
# # # # # Line 2
frame8_text2 = Frame(frame8)
frame8_text2.grid(row=5, column=1)

frame8_l3 = Label(frame8_text2, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l4 = Label(frame8_text2, text="and had to flee. His backpack had enough for a couple", font=("FunSized", 20),
                  fg="white", bg="black")

frame8_l3.grid(row=1, column=0)
frame8_l4.grid(row=1, column=1)

# # # # # Line 3
frame8_text3 = Frame(frame8)
frame8_text3.grid(row=6, column=1)

frame8_l5 = Label(frame8_text3, text="items and decided to take", font=("FunSized", 20), fg="white", bg="black")
frame8_l6 = Label(frame8_text3, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l7 = Label(frame8_text3, text="and", font=("FunSized", 20), fg="white", bg="black")
frame8_l8 = Label(frame8_text3, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l9 = Label(frame8_text3, text=". He was headed to", font=("FunSized", 20), fg="white", bg="black")

frame8_l5.grid(row=2, column=0)
frame8_l6.grid(row=2, column=1)
frame8_l7.grid(row=2, column=2)
frame8_l8.grid(row=2, column=3)
frame8_l9.grid(row=2, column=4)
# # # # # Line 4
frame8_text4 = Frame(frame8)
frame8_text4.grid(row=7, column=1)

frame8_l10 = Label(frame8_text4, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l11 = Label(frame8_text4, text="when he encountered a", font=("FunSized", 20), fg="white", bg="black")
frame8_l12 = Label(frame8_text4, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l13 = Label(frame8_text4, text="which began to", font=("FunSized", 20), fg="white", bg="black")

frame8_l10.grid(row=3, column=0)
frame8_l11.grid(row=3, column=1)
frame8_l12.grid(row=3, column=2)
frame8_l13.grid(row=3, column=3)
# # # # # Line 5
frame8_text5 = Frame(frame8)
frame8_text5.grid(row=8, column=1)

frame8_l14 = Label(frame8_text5, text="chase him, so the boy ran for his life. After running on for miles he",
                   font=("FunSized", 20), fg="white", bg="black")
frame8_l14.grid(row=4, column=0)
# # # # # Line 6
frame8_text6 = Frame(frame8)
frame8_text6.grid(row=9, column=1)

frame8_l15 = Label(frame8_text6, text="was no longer being chased, but he faced a problem; he was hungry. He",
                   font=("FunSized", 20), fg="white", bg="black")
frame8_l15.grid(row=5, column=0)
# # # # # Line 7
frame8_text7 = Frame(frame8)
frame8_text7.grid(row=10, column=1)

frame8_l16 = Label(frame8_text7, text="managed to find", font=("FunSized", 20), fg="white", bg="black")
frame8_l17 = Label(frame8_text7, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l18 = Label(frame8_text7, text="and ate it to relive his hunger. He went days", font=("FunSized", 20),
                   fg="white", bg="black")

frame8_l16.grid(row=6, column=0)
frame8_l17.grid(row=6, column=1)
frame8_l18.grid(row=6, column=2)
# # # # # Line 8
frame8_text8 = Frame(frame8)
frame8_text8.grid(row=11, column=1)

frame8_l19 = Label(frame8_text8, text="without another meal. He heard his stomach growl like never before.",
                   font=("FunSized", 20), fg="white", bg="black")
frame8_l19.grid(row=7, column=0)
# # # # # Line 9
frame8_text9 = Frame(frame8)
frame8_text9.grid(row=12, column=1)

frame8_l20 = Label(frame8_text9, text="It was so", font=("FunSized", 20), fg="white", bg="black")
frame8_l21 = Label(frame8_text9, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame8_l22 = Label(frame8_text9, text="he woke up from his horrid dream.", font=("FunSized", 20),
                   fg="white", bg="black")

frame8_l20.grid(row=8, column=0)
frame8_l21.grid(row=8, column=1)
frame8_l22.grid(row=8, column=2)
# # # # # The end + click to play again
frame8_text10 = Frame(frame8, bg="black")
frame8_text10.grid(row=13, column=1)

frame8_l23 = Label(frame8_text10, text="The End!", font=("FunSized", 35), fg="white", bg="black")
frame8_l24 = Label(frame8_text10, text="Click 'Home' to play again!", font=("FunSized", 20), fg="white", bg="black")

frame8_l23.grid(row=4, column=1, ipady=10)
frame8_l24.grid(row=5, column=1)

# User Input Page 2
frame7 = Frame(bottom, bg="Black")
frame7.grid(row=0, column=0, ipadx=10, ipady=200, sticky="NEWS")

# return to home
frame7_b1 = Button(frame7, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame7_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# filler labels so i can use the .grid method properly
filler1 = Label(frame7, bg="black")
filler1.grid(row=0, column=0, rowspan=4, columnspan=1, ipadx=110)
filler2 = Label(frame7, bg="black")
filler2.grid(row=0, column=2, rowspan=4)

# enter the title of your mad libs here on frame 5
frame7_l1 = Label(frame7, text="The Crazy Dream", font=("FunSized", 35), fg="white", bg="black")
frame7_l1.grid(row=1, column=1, padx=200)

frame7_line = Label(frame7, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame7_line.grid(row=2, column=1)

# entry boxes go into this sub frame
frame7_input = Frame(frame7, bg="black")
frame7_input.grid(row=3, column=1, pady=20)
# # # # # #
frame7_l2 = Label(frame7_input, text="Enter a bug", font=("FunSized", 20), fg="white", bg="black")
frame7_l2.grid(row=1, column=0, pady=10, padx=5)
frame7_e1 = Entry(frame7_input, font=("FunSized", 20))
frame7_e1.grid(row=1, column=1, pady=10, padx=5)
frame7_l3 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l3.grid(row=1, column=3, pady=10, padx=5)
# # # # # #
frame7_l4 = Label(frame7_input, text="Enter a object", font=("FunSized", 20), fg="white", bg="black")
frame7_l4.grid(row=2, column=0, pady=10, padx=5)
frame7_e2 = Entry(frame7_input, font=("FunSized", 20))
frame7_e2.grid(row=2, column=1, pady=10, padx=5)
frame7_l5 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l5.grid(row=2, column=3, pady=10, padx=5)
# # # # # #
frame7_l6 = Label(frame7_input, text="Enter a object", font=("FunSized", 20), fg="white", bg="black")
frame7_l6.grid(row=3, column=0, pady=10, padx=5)
frame7_e3 = Entry(frame7_input, font=("FunSized", 20))
frame7_e3.grid(row=3, column=1, pady=10, padx=5)
frame7_l7 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l7.grid(row=3, column=3, pady=10, padx=5)
# # # # # #
frame7_l8 = Label(frame7_input, text="Enter a noun", font=("FunSized", 20), fg="white", bg="black")
frame7_l8.grid(row=4, column=0, pady=10, padx=5)
frame7_e4 = Entry(frame7_input, font=("FunSized", 20))
frame7_e4.grid(row=4, column=1, pady=10, padx=5)
frame7_l9 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l9.grid(row=4, column=3, pady=10, padx=5)
# # # # # #
frame7_l10 = Label(frame7_input, text="Enter an animal", font=("FunSized", 20), fg="white", bg="black")
frame7_l10.grid(row=5, column=0, pady=10, padx=5)
frame7_e5 = Entry(frame7_input, font=("FunSized", 20))
frame7_e5.grid(row=5, column=1, pady=10, padx=5)
frame7_l11 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l11.grid(row=5, column=3, pady=10, padx=5)
# # # # # #
frame7_l12 = Label(frame7_input, text="Enter a food", font=("FunSized", 20), fg="white", bg="black")
frame7_l12.grid(row=6, column=0, pady=10, padx=5)
frame7_e6 = Entry(frame7_input, font=("FunSized", 20))
frame7_e6.grid(row=6, column=1, pady=10, padx=5)
frame7_l13 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l13.grid(row=6, column=3, pady=10, padx=5)
# # # # # #
frame7_l14 = Label(frame7_input, text="Enter an adjective", font=("FunSized", 20), fg="white", bg="black")
frame7_l14.grid(row=7, column=0, pady=10, padx=5)
frame7_e7 = Entry(frame7_input, font=("FunSized", 20))
frame7_e7.grid(row=7, column=1, pady=10, padx=5)
frame7_l15 = Label(frame7_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame7_l15.grid(row=7, column=3, pady=10, padx=5)
# # # # # #
# this will confirm the user's inputs
frame7_b2 = Button(frame7_input, text="Enter", font=("FunSized", 20), command=s3_entry, highlightbackground="#58A4B0")
frame7_b2.grid(row=9, column=1, pady=10, padx=5)
# line to make it look nice
frame7_line2 = Label(frame7, text="___________________________________________________________________________________"
                     , font=35, fg="white", bg="black")
frame7_line2.grid(row=4, column=1)
# this will lead to the story
frame7_b7 = Button(frame7, text="Click here to begin your story", font=("FunSized", 20), command=do_story3,
                   highlightbackground="#E3B23C")
frame7_b7.grid(row=10, column=1, pady=30)
# --------------------------------------------------------------------------------------------------------------
# Story 2
frame6 = Frame(bottom, bg="Black")
frame6.grid(row=0, column=0, ipady=200, sticky="news")

# return to home
frame6_b1 = Button(frame6, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame6_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# Title label + empty label in order to separate the title from the story
frame6_empty = Label(frame6, bg="black")
frame6_empty.grid(row=0, column=1)
# enter the title of your mad libs here on frame 3
frame6_l1 = Label(frame6, text="The Year 2020", font=("FunSized", 35), fg="white", bg="black")
frame6_l1.grid(row=1, column=1, padx=200)

frame6_line = Label(frame6, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame6_line.grid(row=2, column=1)
# image
f6_img1 = PhotoImage(file="2020.png")
frame6_l2 = Label(frame6, image=f6_img1, bg="black")
frame6_l2.grid(row=3, column=1, pady=10)

# # # # # Line 1
frame6_text = Frame(frame6, bg="red")
frame6_text.grid(row=4, column=1)

frame6_l2 = Label(frame6_text, text="It was late 2020, and the virus Covid-19", font=("FunSized", 20), fg="white",
                  bg="black")
# for some reason i've forgotten how to underline, someone please make l3 underlined
frame6_l3 = Label(frame6_text, text="---", font=("FunSized", 20), fg="white", bg="black")
frame6_l4 = Label(frame6_text, text="through the United States.", font=("FunSized", 20), fg="white", bg="black")

frame6_l2.grid(row=0, column=0)
frame6_l3.grid(row=0, column=1)
frame6_l4.grid(row=0, column=2)
# # # # # Line 2
frame6_text2 = Frame(frame6)
frame6_text2.grid(row=5, column=1)

frame6_l5 = Label(frame6_text2, text="As I turned on the T.V. I heard news of people", font=("FunSized", 20),
                  fg="white", bg="black")
frame6_l6 = Label(frame6_text2, text="buying up all the", font=("FunSized", 20), fg="white", bg="black")
frame6_l7 = Label(frame6_text2, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame6_l8 = Label(frame6_text2, text="and", font=("FunSized", 20), fg="white", bg="black")

frame6_l5.grid(row=1, column=0)
frame6_l6.grid(row=1, column=1)
frame6_l7.grid(row=1, column=2)
frame6_l8.grid(row=1, column=3)

# # # # # Line 3
frame6_text3 = Frame(frame6)
frame6_text3.grid(row=6, column=1)

frame6_l9 = Label(frame6_text3, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame6_l10 = Label(frame6_text3, text="that were available.", font=("FunSized", 20), fg="white", bg="black")
frame6_l11 = Label(frame6_text3, text="Everything got closed due to the pandemic", font=("FunSized", 20),
                   fg="white", bg="black")

frame6_l9.grid(row=2, column=0)
frame6_l10.grid(row=2, column=1)
frame6_l11.grid(row=2, column=2)
# # # # # Line 4
frame6_text4 = Frame(frame6)
frame6_text4.grid(row=7, column=1)

frame6_l12 = Label(frame6_text4, text="including: sports,", font=("FunSized", 20), fg="white", bg="black")
frame6_l13 = Label(frame6_text4, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame6_l14 = Label(frame6_text4, text="and many other businesses.", font=("FunSized", 20), fg="white", bg="black")
frame6_l15 = Label(frame6_text4, text="Many people were trying", font=("FunSized", 20), fg="white", bg="black")

frame6_l12.grid(row=3, column=0)
frame6_l13.grid(row=3, column=1)
frame6_l14.grid(row=3, column=2)
frame6_l15.grid(row=3, column=3)
# # # # # Line 5
frame6_text5 = Frame(frame6)
frame6_text5.grid(row=8, column=1)

frame6_l16 = Label(frame6_text5, text="to find productive ways to entertain themselves", font=("FunSized", 20),
                   fg="white", bg="black")
frame6_l17 = Label(frame6_text5, text="while being stuck at", font=("FunSized", 20), fg="white", bg="black")
frame6_l18 = Label(frame6_text5, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame6_l19 = Label(frame6_text5, text=".", font=("FunSized", 20), fg="white", bg="black")

frame6_l16.grid(row=4, column=0)
frame6_l17.grid(row=4, column=1)
frame6_l18.grid(row=4, column=2)
frame6_l19.grid(row=4, column=3)
# # # # # Line 6
frame6_text6 = Frame(frame6)
frame6_text6.grid(row=9, column=1)

frame6_l20 = Label(frame6_text6, text="This year has been quite", font=("FunSized", 20), fg="white", bg="black")
frame6_l21 = Label(frame6_text6, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame6_l22 = Label(frame6_text6, text="for everyone, hopefully 2021 will be better!", font=("FunSized", 20),
                   fg="white", bg="black")

frame6_l20.grid(row=5, column=0)
frame6_l21.grid(row=5, column=1)
frame6_l22.grid(row=5, column=2)
# # # # # The end + click to play again
frame6_text7 = Frame(frame6, bg="black")
frame6_text7.grid(row=10, column=1)

frame4_l23 = Label(frame6_text7, text="The End!", font=("FunSized", 35), fg="white", bg="black")
frame4_l24 = Label(frame6_text7, text="Click 'Home' to play again!", font=("FunSized", 20), fg="white", bg="black")

frame4_l23.grid(row=4, column=1, ipady=20)
frame4_l24.grid(row=5, column=1)

# User Input Page 2
frame5 = Frame(bottom, bg="Black")
frame5.grid(row=0, column=0, ipadx=10, ipady=200, sticky="NEWS")

# return to home
frame5_b1 = Button(frame5, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame5_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# filler labels so i can use the .grid method properly
filler1 = Label(frame5, bg="black")
filler1.grid(row=0, column=0, rowspan=4, columnspan=1, ipadx=110)
filler2 = Label(frame5, bg="black")
filler2.grid(row=0, column=2, rowspan=4)

# enter the title of your mad libs here on frame 5
frame5_l1 = Label(frame5, text="The Year 2020", font=("FunSized", 35), fg="white", bg="black")
frame5_l1.grid(row=1, column=1, padx=200)

frame5_line = Label(frame5, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame5_line.grid(row=2, column=1)

# entry boxes go into this sub frame
frame5_input = Frame(frame5, bg="black")
frame5_input.grid(row=3, column=1, pady=50)
# # # # # #
frame5_l2 = Label(frame5_input, text="Enter a VERB", font=("FunSized", 20), fg="white", bg="black")
frame5_l2.grid(row=1, column=0, pady=10, padx=5)
frame5_e1 = Entry(frame5_input, font=("FunSized", 20))
frame5_e1.grid(row=1, column=1, pady=10, padx=5)
frame5_l3 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l3.grid(row=1, column=3, pady=10, padx=5)
# # # # # #
frame5_l4 = Label(frame5_input, text="Enter a NOUN", font=("FunSized", 20), fg="white", bg="black")
frame5_l4.grid(row=2, column=0, pady=10, padx=5)
frame5_e2 = Entry(frame5_input, font=("FunSized", 20))
frame5_e2.grid(row=2, column=1, pady=10, padx=5)
frame5_l5 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l5.grid(row=2, column=3, pady=10, padx=5)
# # # # # #
frame5_l6 = Label(frame5_input, text="Enter a NOUN", font=("FunSized", 20), fg="white", bg="black")
frame5_l6.grid(row=3, column=0, pady=10, padx=5)
frame5_e3 = Entry(frame5_input, font=("FunSized", 20))
frame5_e3.grid(row=3, column=1, pady=10, padx=5)
frame5_l7 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l7.grid(row=3, column=3, pady=10, padx=5)
# # # # # #
frame5_l8 = Label(frame5_input, text="Enter a PLACE", font=("FunSized", 20), fg="white", bg="black")
frame5_l8.grid(row=4, column=0, pady=10, padx=5)
frame5_e4 = Entry(frame5_input, font=("FunSized", 20))
frame5_e4.grid(row=4, column=1, pady=10, padx=5)
frame5_l9 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l9.grid(row=4, column=3, pady=10, padx=5)
# # # # # #
frame5_l10 = Label(frame5_input, text="Enter a PLACE", font=("FunSized", 20), fg="white", bg="black")
frame5_l10.grid(row=5, column=0, pady=10, padx=5)
frame5_e5 = Entry(frame5_input, font=("FunSized", 20))
frame5_e5.grid(row=5, column=1, pady=10, padx=5)
frame5_l11 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l11.grid(row=5, column=3, pady=10, padx=5)
# # # # # #
frame5_l12 = Label(frame5_input, text="Enter an ADJECTIVE", font=("FunSized", 20), fg="white", bg="black")
frame5_l12.grid(row=6, column=0, pady=10, padx=5)
frame5_e6 = Entry(frame5_input, font=("FunSized", 20))
frame5_e6.grid(row=6, column=1, pady=10, padx=5)
frame5_l13 = Label(frame5_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame5_l13.grid(row=6, column=3, pady=10, padx=5)
# # # # # #
# this will confirm the user's inputs
frame5_b2 = Button(frame5_input, text="Enter", font=("FunSized", 20), command=s2_entry, highlightbackground="#58A4B0")
frame5_b2.grid(row=9, column=1, pady=10, padx=5)
# line to make it look nice
frame5_line2 = Label(frame5, text="___________________________________________________________________________________"
                     , font=35, fg="white", bg="black")
frame5_line2.grid(row=4, column=1)
# this will lead to the story
frame5_b7 = Button(frame5, text="Click here to begin your story", font=("FunSized", 20), command=do_story2,
                   highlightbackground="#E3B23C")
frame5_b7.grid(row=10, column=1, pady=30)
# --------------------------------------------------------------------------------------------------------------
# Story 1
frame4 = Frame(bottom, bg="black")
frame4.grid(row=0, column=0, ipady=200, sticky="news")

# return to home
frame4_b1 = Button(frame4, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame4_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# Title label + empty label in order to separate the title from the story
frame4_empty = Label(frame4, bg="black")
frame4_empty.grid(row=0, column=1)
# enter the title of your mad libs here on frame 3
frame4_l1 = Label(frame4, text="Pets are Fun!", font=("FunSized", 35), fg="white", bg="black")
frame4_l1.grid(row=1, column=1, padx=200)

frame4_line = Label(frame4, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame4_line.grid(row=2, column=1)
# image
f4_img1 = PhotoImage(file="pets.png")
frame4_l2 = Label(frame4, image=f4_img1, bg="black")
frame4_l2.grid(row=3, column=1, pady=20)

# # # # # Line 1
frame4_text = Frame(frame4, bg="red")
frame4_text.grid(row=4, column=1)

frame4_l2 = Label(frame4_text, text="So many animals make", font=("FunSized", 20), fg="white", bg="black")
# for some reason i've forgotten how to underline, someone please make l3 underlined
frame4_l3 = Label(frame4_text, text="---", font=("FunSized", 20), fg="white", bg="black")
frame4_l4 = Label(frame4_text, text="pets! Many people prefer a cute,", font=("FunSized", 20), fg="white", bg="black")

frame4_l2.grid(row=0, column=0)
frame4_l3.grid(row=0, column=1)
frame4_l4.grid(row=0, column=2)
# # # # # Line 2
frame4_text2 = Frame(frame4)
frame4_text2.grid(row=5, column=1)

frame4_l5 = Label(frame4_text2, text="furry", font=("FunSized", 20), fg="white", bg="black")
frame4_l6 = Label(frame4_text2, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l7 = Label(frame4_text2, text="or a", font=("FunSized", 20), fg="white", bg="black")
frame4_l8 = Label(frame4_text2, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l9 = Label(frame4_text2, text="to cuddle. Most pets need", font=("FunSized", 20), fg="white", bg="black")
frame4_l10 = Label(frame4_text2, text="------", font=("FunSized", 20), fg="white", bg="black")

frame4_l5.grid(row=1, column=0)
frame4_l6.grid(row=1, column=1)
frame4_l7.grid(row=1, column=2)
frame4_l8.grid(row=1, column=3)
frame4_l9.grid(row=1, column=4)
frame4_l10.grid(row=1, column=5)
# # # # # Line 3
frame4_text3 = Frame(frame4)
frame4_text3.grid(row=6, column=1)

frame4_l11 = Label(frame4_text3, text="Care. like", font=("FunSized", 20), fg="white", bg="black")
frame4_l12 = Label(frame4_text3, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l13 = Label(frame4_text3, text=",", font=("FunSized", 20), fg="white", bg="black")
frame4_l14 = Label(frame4_text3, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l15 = Label(frame4_text3, text=", and a place to sleep in order to live comfortably!", font=("FunSized", 20),
                   fg="white", bg="black")

frame4_l11.grid(row=2, column=0)
frame4_l12.grid(row=2, column=1)
frame4_l13.grid(row=2, column=2)
frame4_l14.grid(row=2, column=3)
frame4_l15.grid(row=2, column=4)
# # # # # Line 4
frame4_text4 = Frame(frame4)
frame4_text4.grid(row=7, column=1)

frame4_l16 = Label(frame4_text4, text="Some", font=("FunSized", 20), fg="white", bg="black")
frame4_l17 = Label(frame4_text4, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l18 = Label(frame4_text4, text="live in", font=("FunSized", 20), fg="white", bg="black")
frame4_l19 = Label(frame4_text4, text="-----", font=("FunSized", 20), fg="white", bg="black")
frame4_l20 = Label(frame4_text4, text=". Everyone can agree having pets is fun!", font=("FunSized", 20),
                   fg="white", bg="black")

frame4_l16.grid(row=3, column=0)
frame4_l17.grid(row=3, column=1)
frame4_l18.grid(row=3, column=2)
frame4_l19.grid(row=3, column=3)
frame4_l20.grid(row=3, column=4)
# # # # # The End text
frame4_text5 = Frame(frame4, bg="black")
frame4_text5.grid(row=8, column=1)

frame4_l21 = Label(frame4_text5, text="The End!", font=("FunSized", 35), fg="white", bg="black")
frame4_l22 = Label(frame4_text5, text="Click 'Home' to play again!", font=("FunSized", 20), fg="white", bg="black")

frame4_l21.grid(row=4, column=1, ipady=20)
frame4_l22.grid(row=5, column=1)
# # # # #
# User Input Page 1
frame3 = Frame(bottom, bg="black")
frame3.grid(row=0, column=0, ipadx=10, ipady=200, sticky="NEWS")

frame3_b1 = Button(frame3, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame3_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# filler labels so i can use the .grid method properly
filler1 = Label(frame3, bg="black")
filler1.grid(row=0, column=0, rowspan=4, columnspan=1, ipadx=120)
filler2 = Label(frame3, bg="black")
filler2.grid(row=0, column=2, rowspan=4)

# enter the title of your mad libs here on frame 3
frame3_l1 = Label(frame3, text="Pets are Fun!", font=("FunSized", 35), fg="white", bg="black")
frame3_l1.grid(row=1, column=1, padx=200)

frame3_line = Label(frame3, text="_____________________________________________________________________________________"
                    , font=35, fg="white", bg="black")
frame3_line.grid(row=2, column=1)

# entry boxes go into this sub frame
frame3_input = Frame(frame3, bg="black")
frame3_input.grid(row=3, column=1, pady=20)
# # # # # #
frame3_l2 = Label(frame3_input, text="Enter an adjective!", font=("FunSized", 20), fg="white", bg="black")
frame3_l2.grid(row=1, column=0, pady=10, padx=5)
frame3_e1 = Entry(frame3_input, font=("FunSized", 20))
frame3_e1.grid(row=1, column=1, pady=10, padx=5)
frame3_l3 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l3.grid(row=1, column=3, pady=10, padx=5)
# # # # # #
frame3_l4 = Label(frame3_input, text="Enter an animal!", font=("FunSized", 20), fg="white", bg="black")
frame3_l4.grid(row=2, column=0, pady=10, padx=5)
frame3_e2 = Entry(frame3_input, font=("FunSized", 20))
frame3_e2.grid(row=2, column=1, pady=10, padx=5)
frame3_l5 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l5.grid(row=2, column=3, pady=10, padx=5)
# # # # # #
frame3_l6 = Label(frame3_input, text="Enter an animal!", font=("FunSized", 20), fg="white", bg="black")
frame3_l6.grid(row=3, column=0, pady=10, padx=5)
frame3_e3 = Entry(frame3_input, font=("FunSized", 20))
frame3_e3.grid(row=3, column=1, pady=10, padx=5)
frame3_l7 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l7.grid(row=3, column=3, pady=10, padx=5)
# # # # # #
frame3_l8 = Label(frame3_input, text="Enter an adjective!", font=("FunSized", 20), fg="white", bg="black")
frame3_l8.grid(row=4, column=0, pady=10, padx=5)
frame3_e4 = Entry(frame3_input, font=("FunSized", 20))
frame3_e4.grid(row=4, column=1, pady=10, padx=5)
frame3_l9 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l9.grid(row=4, column=3, pady=10, padx=5)
# # # # # #
frame3_l10 = Label(frame3_input, text="Enter a food!", font=("FunSized", 20), fg="white", bg="black")
frame3_l10.grid(row=5, column=0, pady=10, padx=5)
frame3_e5 = Entry(frame3_input, font=("FunSized", 20))
frame3_e5.grid(row=5, column=1, pady=10, padx=5)
frame3_l11 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l11.grid(row=5, column=3, pady=10, padx=5)
# # # # # #
frame3_l12 = Label(frame3_input, text="Enter a liquid!", font=("FunSized", 20), fg="white", bg="black")
frame3_l12.grid(row=6, column=0, pady=10, padx=5)
frame3_e6 = Entry(frame3_input, font=("FunSized", 20))
frame3_e6.grid(row=6, column=1, pady=10, padx=5)
frame3_l13 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l13.grid(row=6, column=3, pady=10, padx=5)
# # # # # #
frame3_l14 = Label(frame3_input, text="Enter a plural animal", font=("FunSized", 20), fg="white", bg="black")
frame3_l14.grid(row=7, column=0, pady=10, padx=5)
frame3_e7 = Entry(frame3_input, font=("FunSized", 20))
frame3_e7.grid(row=7, column=1, pady=10, padx=5)
frame3_l15 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l15.grid(row=7, column=3, pady=10, padx=5)
# # # # # #
frame3_l16 = Label(frame3_input, text="Enter a place!", font=("FunSized", 20), fg="white", bg="black")
frame3_l16.grid(row=8, column=0, pady=10, padx=5)
frame3_e8 = Entry(frame3_input, font=("FunSized", 20))
frame3_e8.grid(row=8, column=1, pady=10, padx=5)
frame3_l17 = Label(frame3_input, text="", font=("FunSized", 20), fg="white", bg="black")
frame3_l17.grid(row=8, column=3, pady=10, padx=5)
# # # # # #
# this will confirm the user's inputs
frame3_b2 = Button(frame3_input, text="Enter", font=("FunSized", 20), command=s1_entry, highlightbackground="#58A4B0")
frame3_b2.grid(row=9, column=1, pady=5, padx=5)
# line to make it look nice
frame3_line2 = Label(frame3, text="___________________________________________________________________________________"
                     , font=35, fg="white", bg="black")
frame3_line2.grid(row=4, column=1)
# this will start the mad libs
frame3_b3 = Button(frame3, text="Click here to begin your story", font=("FunSized", 20), command=do_story1,
                   highlightbackground="#E3B23C")
frame3_b3.grid(row=10, column=1, columnspan=2, pady=10)
# --------------------------------------------------------------------------------------------------------------
# How To Play Frame
frame2 = Frame(bottom, bg="Black")
frame2.grid(row=0, column=0, sticky="news")

# filler labels so i can use the .grid method properly
filler1 = Label(frame2, bg="black")
filler1.grid(row=0, column=0, rowspan=7, columnspan=1, ipadx=100)
filler2 = Label(frame2, bg="black")
filler2.grid(row=0, column=2, rowspan=7)

# home button
frame2_b1 = Button(frame2, text="Home", font=("FunSized", 20), command=go_home, highlightbackground="#E3B23C")
frame2_b1.grid(row=0, column=0, sticky="NW", padx=10, pady=10, ipadx=10)

# title
filler3 = Label(frame2, bg="black")
filler3.grid(row=0, column=1)

frame2_l1 = Label(frame2, text="How to Play", font=("FunSized", 40), bg="Black", fg="White")
frame2_l1.grid(row=1, column=1)

# image
f2_img1 = PhotoImage(file="rules.png")
frame2_l2 = Label(frame2, image=f2_img1, bg="black")
frame2_l2.grid(row=2, column=1, pady=20)

# rules
frame2_l3 = Label(frame2, text="1. Click the story you want to see", font=("FunSized", 30), bg="Black", fg="White")
frame2_l3.grid(row=3, column=1)

frame2_l4 = Label(frame2, text="2. Input the type of word that is asked", font=("FunSized", 30), bg="Black", fg="White")
frame2_l4.grid(row=4, column=1, pady=10)

frame2_l5 = Label(frame2, text="3. Click 'Enter' to confirm your answers", font=("FunSized", 30),
                  bg="Black", fg="White")
frame2_l5.grid(row=5, column=1)

frame2_l6 = Label(frame2, text="4. Click 'Begin your Story'", font=("FunSized", 30), bg="Black", fg="White")
frame2_l6.grid(row=6, column=1, pady=10)

frame_l7 = Label(frame2, text="5. Most importantly have FUN!", font=("FunSized", 30), bg="Black", fg="White")
frame_l7.grid(row=7, column=1)
# --------------------------------------------------------------------------------------------------------------
# Home Screen
frame1 = Frame(bottom, bg="black")
frame1.grid(row=0, column=0, sticky="NEWS")

# filler labels so i can use the .grid method properly
filler1 = Label(frame1, bg="black")
filler1.grid(row=0, column=0, rowspan=9, columnspan=1, ipadx=130)
filler2 = Label(frame1, bg="black")
filler2.grid(row=0, column=2, rowspan=9)

# title
filler3 = Label(frame1, bg="black")
filler3.grid(row=0, column=1)

frame1_l1 = Label(frame1, text="Welcome to our Mad libs!", font=("FunSized", 40), bg="Black", fg="White")
frame1_l1.grid(row=1, column=1)

frame1_l2 = Label(frame1, text="_____________________________________________________________________________________"
                  , font=35, fg="white", bg="black")
frame1_l2.grid(row=2, column=1)

# image
f1_img1 = PhotoImage(file="home.png")
frame1_l3 = Label(frame1, image=f1_img1, bg="black")
frame1_l3.grid(row=3, column=1, pady=20)

frame1_l4 = Label(frame1, text="______________________________________________________________", font=35,
                  fg="white", bg="black")
frame1_l4.grid(row=4, column=1)

frame1_b1 = Button(frame1, text="How to Play", font=("FunSized", 30), command=go_howto, highlightbackground="#58A4B0")
frame1_b1.grid(row=5, column=1, pady=10, ipadx=15)

frame1_l5 = Label(frame1, text="_____________________________________________________________", font=35,
                  fg="white", bg="black")
frame1_l5.grid(row=6, column=1)

frame1_b2 = Button(frame1, text="Pets are Fun!", font=("FunSized", 25), command=go_story1,
                   highlightbackground="#E3B23C")
frame1_b2.grid(row=7, column=1, ipadx=25)

frame1_b3 = Button(frame1, text="The Year 2020", font=("FunSized", 25), command=go_story2,
                   highlightbackground="#E3B23C")
frame1_b3.grid(row=8, column=1, ipadx=25, pady=7)

frame1_b4 = Button(frame1, text="The Crazy Dream", font=("FunSized", 25), command=go_story3,
                   highlightbackground="#E3B23C")
frame1_b4.grid(row=9, column=1, ipadx=20)

window.mainloop()
