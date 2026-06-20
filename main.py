from tkinter import *
from tkinter import ttk
from datetime import date
root = Tk()
main_frame = Frame(
    root,
    bg="#ffffff",
    padx=40,
    pady=30
)

main_frame.pack(pady=30)

root.title(" Age calculator ")
root.geometry("650x650")
root.configure(bg="#eef2ff")
root.title("Age Calculator")
heading = Label(
   main_frame,
    text="Age Calculator",
    font=("Segoe UI", 28, "bold"),
    bg="#eef2ff",
    fg="#1e293b"
)

heading.pack(pady=25)


#Name Label
Name_Label = Label(
    main_frame,
    text="Full Name",
    font=("Segoe UI", 11),
    bg="#eef2ff",
    fg="#475569"
)

Name_Label.pack(pady=5)

#Name input box
name_entry = Entry(
    main_frame,
    font=("Segoe UI", 12),
    width=25,
    justify="center"
)

name_entry.pack(pady=10)
print(name_entry.get())

#Day dropdown 
day = ttk.Combobox( main_frame, width = 10)
day['values'] = list( range(1,32))
day.set("Day")
day.pack(pady=5)

#Month dropdown
month= ttk.Combobox(main_frame, width = 10)
month['values'] = ["january","february","march","april","may","june","july","august","september","october","november","december"]
month.set("Month")
month.pack(pady=5)

#Year dropdown
year= ttk.Combobox(main_frame, width = 10)
year['values'] = list(range( 2025, 1900, -1))
year.set("Year")
year.pack(pady=5)

#result_Label
result_label = Label(
    main_frame,
    text="",
    font=("Segoe UI", 12, "bold"),
    bg="#dcfce7",
    fg="#166534",
    padx=20,
    pady=15,
    wraplength=450,
    relief="solid",
    borderwidth=1,
    justify="center"
)

result_label.pack(pady=20)


#messages directory
def get_message(age):

    messages = {

        1: "One year old. Professional dribbler, zero responsibilities. 🍼",
        2: "Two years in. Absolute menace to furniture. 😈",
        3: "Three. Running on biscuits and chaos. 🍪",
        4: "Four. Asking 'why' has become a full-time job. 🤔",
        5: "Five. Kindergarten veteran. 🎒",

        6: "Six. Playground politics begins. ⚽",
        7: "Seven. Still thinks naps are punishment. 😭",
        8: "Eight. Peak cartoon enthusiast. 📺",
        9: "Nine. One year from double digits, mate. 😎",
        10: "Double digits! Feeling proper grown-up now, are we? 🎉",

        11: "Eleven. Awkwardness loading... ⏳",
        12: "Twelve. Last stop before the teen disaster. 🚆",
        13: "Official teenager. Brace yourself. 😵‍💫",
        14: "Fourteen. Opinions detected. Wisdom not found. 💀",
        15: "Fifteen. Main character syndrome unlocked. 🎬",

        16: "Sixteen. Acting grown while still asking for pocket money. 😂",
        17: "Seventeen. Nearly an adult. Nearly. 🤏",
        18: "Eighteen. Congrats, now the government knows you exist. 🫡",
        19: "Nineteen. Teen trial ending soon, mate. ⌛",

        20: "Twenty. Tutorial completed. Good luck. 😎",
        21: "Twenty-one. Adulting still feels like a scam. 🎭",
        22: "Twenty-two. Chill, life's barely started. 😌",
        23: "Twenty-three. Winging it professionally. 💼",
        24: "Twenty-four. Quarter-life panic approaching. 🚨",

        25: "Quarter century. That's mildly terrifying. 🎂",
        26: "Twenty-six. Back pain has your number now. 📞",
        27: "Twenty-seven. Sleep is luxury. 😴",
        28: "Twenty-eight. Everyone's getting married somehow. 💍",
        29: "Last year of your twenties. Make it count. 🔥",

        30: "Thirty. Welcome to premium adulthood. 🏆",
        31: "Thirty-one. Making noises while standing up. 💀",
        32: "Thirty-two. Bedtime suddenly sounds exciting. 😭",
        33: "Thirty-three. Young enough for fun, old enough for ibuprofen. 💊",
        34: "Thirty-four. Your knees have opinions now. 🦵",

        35: "Thirty-five. Midlife trailer just dropped. 🎬",
        40: "Forty. Factory warranty expired. 🏭",
        45: "Forty-five. Dad jokes become unavoidable. 😭",
        50: "Fifty. Half a century. Respect. 🎩",
        55: "Fifty-five. Professional advice dispenser. 📚",

        60: "Sixty. Wisdom DLC installed. 🧙",
        65: "Sixty-five. Retirement brochure unlocked. 🏖️",
        70: "Seventy. Still standing. Legendary. 👑",
        75: "Seventy-five. Walking history lesson. 📜",
        80: "Eighty. Vintage human edition. 🏆",

        85: "Eighty-five. The Grim Reaper keeps missing appointments. 💀",
        88: "Eighty-eight. Proper legend status achieved. 👏",
        89: "Eighty-nine. Death seems too shy to ask. 😭",
        90: "Ninety. Ancient but still operational. ⚙️",
        91: "Ninety-one. A historical artefact at this point. 🏺",
        92: "Ninety-two. The calendar fears you. 📅",
        93: "Ninety-three. Time itself is impressed. ⏳",
        94: "Ninety-four. Refusing to log out. 😂",
        95: "Ninety-five. The Grim Reaper left you on read. 📱",
        96: "Ninety-six. Pure stubbornness keeping things running. 🔋",
        97: "Ninety-seven. Built different, mate. 💪",
        98: "Ninety-eight. Scientists want a word. 🧪",
        99: "Ninety-nine. Achievement unlocked: Still Here. 🏅",
        100: "One hundred. Fair play. That's outrageous. 👑"
    }

    if age in messages:
        return messages[age]

    elif 36 <= age <= 39:
        return "Still pretending you've got everything sorted. 😎"

    elif 41 <= age <= 49:
        return "Your back now predicts tomorrow's weather. 🌦️"

    elif 51 <= age <= 59:
        return "Experience level: absurdly high. 📈"

    elif 61 <= age <= 79:
        return "You've seen trends die and return twice. 🧙"

    elif 81 <= age <= 87:
        return "Proper legend. The youngsters need your stories. 📖"

    else:
        return "Either immortal or there's a bug in my code. 🤖"


# program logic
def calculate_age():

    #check if user selected everything 
    if(
        day.get() == " day "
        or month.get() == "month"
        or year.get() == "year"
    ):
       
        result_label.config(
            text="please select all fields."
        )
        return
    
    today = date.today()
    birth_day = int(day.get())
    birth_month = month.current() + 1
    birth_year = int(year.get())
    
    age= today.year - birth_year

    if(
        today.month < birth_month or (today.month == birth_month and today.day < birth_day)
    ):
        age -= 1

    name = name_entry.get()
    message = get_message(age)


    result_label.config(
    text=f"🎉 Hey {name}!! You're {age}. \n{message}"
)

 #Calculate button
calculate_button = Button(
    main_frame,
    text="Calculate Age",
    font=("Segoe UI", 14, "bold"),
    bg="#ff5f6d",
    fg="white",
    activebackground="#ff416c",
    activeforeground="white",
    padx=20,
    pady=10,
    command=calculate_age,
    cursor="hand2"
)

calculate_button.pack(pady=25)
   
root.mainloop()
