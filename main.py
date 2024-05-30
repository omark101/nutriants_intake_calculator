from PIL import ImageTk
import customtkinter
import pyodbc
import tkinter as tk
from tkinter import *

# creating the main application window
app = customtkinter.CTk()
app.geometry("1025x583")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app.title("Checkup")

# starting a connection with the microsoft access database
connection_string = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=H:\ZEWAIL CITY\PROJECT.accdb;"
)
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

# Set up canvas and background image
bg = ImageTk.PhotoImage(file="Blue Illustrated Medical Center Presentation (2).png")
canvas = tk.Canvas(app, width=1280, height=720)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

# Label for information
info = tk.Label(master=app, text="The information in this app is not 100% accurate")
info.pack(side=tk.TOP)


# creating buttons and inputs in main window and having them under the main function (first window)
def first_window():
    def sign_button():
        button = customtkinter.CTkButton(master=canvas, text="Sign in",
                                         state=customtkinter.NORMAL, width=150, height=35,
                                         command=check_credentials)
        button.place(x=150, y=350)
        return button

    def register_button():
        button = customtkinter.CTkButton(master=canvas, text='Register', state=customtkinter.NORMAL,
                                         width=150, height=35, command=lambda: switch_from_app_to_register())
        button.place(x=150, y=400)
        return button

    def guest_button():
        button = customtkinter.CTkButton(master=canvas, text="log as guest", state=customtkinter.NORMAL,
                                         width=150, height=35, command=switch)
        button.place(x=150, y=300)
        return button

    def password_entry():
        entry_password = customtkinter.CTkEntry(master=canvas, placeholder_text="enter the password",
                                                placeholder_text_color="lightgrey", border_color="deepskyblue",
                                                width=150, height=35)
        entry_password.place(x=150, y=250)
        return entry_password.get()

    def check_credentials():
        """Connects to the database, compares entered credentials with those in the database,
        and returns True if they match, False otherwise. Handles errors as well."""

        global connection_sign  # Declare as global
        global cursor
        try:
            # Establish a connection
            connection_string = (
                r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=H:\ZEWAIL CITY\PROJECT.accdb;"
            )
            connection_sign = pyodbc.connect(connection_string)
            cursor = connection_sign.cursor()

            # Retrieve user data from the database
            username = user_name()  # Call the user_name() function to get the entered username
            password_x = password_entry()  # Call the password_entry() function to get the entered password
            query = "SELECT * FROM python WHERE username = ? AND password_x = ?"
            cursor.execute(query, (username, password_x))
            result = cursor.fetchone()

            # Return True if credentials match, False otherwise
            return result is not None

        except pyodbc.Error as ex:
            print("Database error:", ex)
            return False  # Indicate error

        finally:
            # Close the connection
            if cursor:
                cursor.close()
            if connection_sign:
                connection_sign.close()

    def user_name():
        username_entry = customtkinter.CTkEntry(master=canvas, placeholder_text="enter your name.....",
                                                placeholder_text_color="lightgrey",
                                                border_color="deepskyblue",
                                                width=150, height=35)
        username_entry.grid_size()
        username_entry.place(x=150, y=200)
        return username_entry.get()

    user_name()
    password_entry()
    guest_button()
    sign_button()
    register_button()


second = customtkinter.CTkToplevel()
second.geometry("920x540")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
second.withdraw()
bg2 = ImageTk.PhotoImage(file="BG2.png")
canvas2 = tk.Canvas(master=second, width=920, height=540)
canvas2.configure(borderwidth=-5)
canvas2.pack(fill="both", expand=True)
canvas2.create_image(0, 0, image=bg2, anchor="nw")

error = customtkinter.CTk()
error.geometry("835x20")


def input_age():
    entry_age = customtkinter.CTkEntry(master=second, placeholder_text="enter age",
                                       placeholder_text_color="lightgrey",
                                       border_color="deepskyblue")
    entry_age.configure(bg_color="midnightblue")
    entry_age.place(x=475, y=275)

    age_str = entry_age.get()
    if age_str:
        return int(age_str)
    else:
        # Handle the case where the entry is empty
        return 0  # Default value


def input_height():
    # Create a CTkEntry widget for user input
    entry_height = customtkinter.CTkEntry(master=second, placeholder_text="enter height (cm)",
                                          placeholder_text_color="lightgrey",
                                          border_color="deepskyblue")
    entry_height.configure(bg_color="midnightblue")
    entry_height.place(x=750, y=200)

    # Get the user input as a string
    height_str = entry_height.get()

    # Validate the input and handle cases where it's empty or not a valid float
    if height_str:
        try:
            #  convert the input to a float
            height_float = float(height_str)

            # Check if the height is not 0
            if height_float != 0:
                return height_float
            else:
                # Handle the case where the height is 0
                return None  # Return None
        except ValueError:
            # Handle the case where the input is not a valid float
            return None  # Return None
    else:
        # Handle the case where the entry is empty
        return None  # Return None

def input_height_final():
    # Get the validated height from input_height
    the_height_float = input_height()

    # Check if the height is not None before using it
    if the_height_float is not None:
        return the_height_float
    else:
        # Handle the case where the height is None
        return None  # Return None


def input_weight():
    entry_weight = customtkinter.CTkEntry(master=second, placeholder_text="enter weight (kg)",
                                          placeholder_text_color="lightgrey",
                                          border_color="deepskyblue")
    entry_weight.configure(bg_color="midnightblue")
    entry_weight.place(x=475, y=200)

    weight_str = entry_weight.get()
    if weight_str:
        return float(weight_str)
    else:
        # Handle the case where the entry is empty
        return 0.0  # Default value


def continue_button2():
    button = customtkinter.CTkButton(master=second, text="continue", command=box_results)
    button.place(x=610, y=440)
    button.configure(bg_color="midnightblue")
    return button


def activity_level():
    global activalue
    optionmenu_activity_level = customtkinter.CTkOptionMenu(second,
                                                            values=["activity", "sedentary", "light active",
                                                                    "moderately active",
                                                                    "very active", "extra active",
                                                                    "professional athlete"])
    optionmenu_activity_level.place(x=750, y=350)
    optionmenu_activity_level.configure(bg_color="midnightblue")

    selected_activity = optionmenu_activity_level.get()

    # Assign a corresponding activalue based on the selected activity level
    if selected_activity == "sedentary":
        activalue = 1.2
    elif selected_activity == "light active":
        activalue = 1.4
    elif selected_activity == "moderately active":
        activalue = 1.6
    elif selected_activity == "very active":
        activalue = 1.75
    elif selected_activity == "extra active":
        activalue = 2
    elif selected_activity == "professional athlete":
        activalue = 2.3
    else:
        # Handle the case where no valid activity level is selected
        activalue = 0
    return activalue


def gender():
    optionmenu_gender = customtkinter.CTkOptionMenu(master=second, values=["Gender", "Male", "Female"])
    optionmenu_gender.place(x=475, y=350)
    optionmenu_gender.configure(bg_color="midnightblue")
    selected_gender = optionmenu_gender.get()
    if selected_gender == "Male":
        S_result = 5
    elif selected_gender == "Female":
        S_result = -161
    else:
        S_result = 0
    return S_result


def country():
    optionmenu = customtkinter.CTkOptionMenu(master=second,
                                             values=["enter your country",
                                                     "USA", "TURKEY", "EGYPT", "GREEK", "BRAZIL", "CHINA"])
    optionmenu.place(x=750, y=275)
    optionmenu.configure(bg_color="midnightblue")
    return optionmenu.get()


def second_window():
    country()
    gender()
    input_age()
    input_height()
    input_weight()
    continue_button2()
    activity_level()


register_window = customtkinter.CTk()
register_window.title("Register new user")
register_window.geometry("300x300")


def name():
    register_name = customtkinter.CTkEntry(
        master=register_window, placeholder_text="Enter your name"
    )
    register_name.place(x=75, y=100)
    return register_name


def password():
    register_password = customtkinter.CTkEntry(
        master=register_window, placeholder_text="Enter your password"
    )
    register_password.place(x=75, y=150)
    return register_password


def get_informations(name_widget,password_widget):
    """Get the username and password from the widgets and insert them into the database."""
    name_value = name_widget.get()
    password_value = password_widget.get()

    # Insert the information into the database using a parameterized query
    query = "INSERT INTO python (username, Password_x) VALUES (?, ?)"
    try:
        cursor.execute(query, name_value, password_value)
        connection.commit()
        print("username:", name_value)
        print("Password_x:", password_value)
        print("Data inserted into the database.")
    except pyodbc.Error as e:
        print("An error occurred:", e)

    # Close the database connection
    cursor.close()
    connection.close()


def calories():
    result = ((20 * input_weight()) + (6.25 * input_height_final())
              - (5 * input_age()) + gender()) * activalue
    return result


def carbs():
    if activity_level == "Sedentary":
        carbs_result = ((calories() * 0.45) / 4)
        return carbs_result
    elif activity_level() == "Light active":
        carbs_result = ((calories() * 0.5) / 4)
        return carbs_result
    elif activity_level() == "Moderately active":
        carbs_result = ((calories() * 0.55) / 4)
        return carbs_result
    elif activity_level() == "Very active":
        carbs_result = ((calories() * 0.6) / 4)
        return carbs_result
    elif activity_level() == "Extra active" or "Professional Athlete":
        carbs_result = ((calories() * 0.65) / 4)
        return carbs_result


def Magnesium():
    if 14 <= input_age() <= 18 and gender() == "Male":
        return 410
    elif 19 <= input_age() <= 30 and gender() == "Male":
        return 400
    elif 31 <= input_age() <= 100 and gender() == "Male":
        return 420
    elif 14 <= input_age() <= 18 and gender() == "Female":
        return 360
    elif 19 <= input_age() <= 30 and gender() == "Female":
        return 310
    elif 31 <= input_age() <= 100 and gender() == "Female":
        return 320


def sodium():
    if 19 <= input_age() <= 50:
        return 1500
    elif 50 <= input_age() <= 100:
        return 1300


def protein():
    protein_result = input_weight() * activalue * 0.8
    return protein_result


def water():
    water_result = 35 * input_weight() * activalue
    return float(water_result)


def calcium():
    if input_age() <= 8:
        calcium_result = 700
    elif input_age() <= 18:
        calcium_result = 1300
    elif input_age() <= 50:
        calcium_result = 1000
    elif input_age() > 50 and gender() == 'Male':
        calcium_result = 1000
    else:
        calcium_result = 1200
    return calcium_result


def potassium():
    if input_age() <= 3:
        potassium_result = 2000
    elif input_age() <= 8:
        potassium_result = 2300
    elif input_age() <= 13:
        potassium_result = 2500
    else:
        potassium_result = 2300
    return potassium_result


def phosphorous():
    if input_age() <= 3:
        phosphorous_result = 460
    elif input_age() <= 8:
        phosphorous_result = 500
    else:
        phosphorous_result = 700
    return phosphorous_result


continue_button = customtkinter.CTkButton(master=register_window, text="Continue")
continue_button.place(x=75, y=225)
name_widget = name()
password_widget = password()
continue_button.configure(command=lambda: (
    get_informations(name_widget, password_widget), switch_from_register_to_first_window()))


def switch():
    app.withdraw()
    second.deiconify()


def switch_from_register_to_first_window():
    register_window.withdraw()
    app.deiconify()


def switch_from_app_to_register():
    app.withdraw()
    register_window.deiconify()


def box_results():
    global activalue
    results = customtkinter.CTkToplevel()
    results.title('Results')

    def calories_result():
        Calories.configure(state='normal')
        Calories.delete(0, END)
        result = (calories())
        Calories.insert(0, result)
        Calories.configure(state='disabled')

    def carbs_result():
        Carbs.configure(state='normal')
        Carbs.delete(0, END)
        result = (carbs())
        Carbs.insert(0, result)
        Carbs.configure(state='disabled')

    def magnesium_result():
        result_magnesium = Magnesium.get()
        if result_magnesium:
            Magnesium.configure(state='normal')
            Magnesium.delete(0, tk.END)
            result = (result_magnesium)
            Magnesium.insert(0, result)
            Magnesium.configure(state='disabled')
        else:

            pass

    def sodium_result():
        Sodium.configure(state='normal')
        Sodium.delete(0, END)
        result = sodium()
        if result is not None:
            result = (result)
        Sodium.insert(tk.END, str(result))
        Sodium.configure(state='disabled')

    def protein_result():
        Protein.configure(state='normal')
        Protein.delete(0, END)
        result = (protein())
        Protein.insert(0, result)
        Protein.configure(state='disabled')

    def calcium_result():
        Calcium.configure(state='normal')
        Calcium.delete(0, END)
        result = (calcium())
        Calcium.insert(0, result)
        Calcium.configure(state='disabled')

    def potassium_result():
        Potassium.configure(state='normal')
        Potassium.delete(0, END)
        result = (potassium())
        Potassium.insert(0, result)
        Potassium.configure(state='disabled')

    def phosphorous_result():
        Phosphorous.configure(state='normal')
        Phosphorous.delete(0, END)
        result = (phosphorous())
        Phosphorous.insert(0, result)
        Phosphorous.configure(state='disabled')

    def water_result():
        Water.configure(state='normal')
        Water.delete(0, END)
        result = (water())
        Water.insert(0, result)
        Water.configure(state='disabled')

    # Add labels and entries for new nutrients
    Label(results, text="Calcium:").grid(row=7)
    Calcium = Entry(results)
    Calcium.grid(row=7, column=1)

    Label(results, text="Potassium:").grid(row=8)
    Potassium = Entry(results)
    Potassium.grid(row=8, column=1)

    Label(results, text="Phosphorous:").grid(row=9)
    Phosphorous = Entry(results)
    Phosphorous.grid(row=9, column=1)

    # Add label and entry for water
    Label(results, text="Water:").grid(row=10)
    Water = Entry(results)
    Water.grid(row=10, column=1)

    # Add buttons for new nutrients and water

    results.geometry('500x100')
    Label(results, text="The results are:").grid(row=2)
    Calories = Entry(results)
    Calories.grid(row=2, column=1)
    Carbs = Entry(results)
    Carbs.grid(row=3, column=1)
    Magnesium = Entry(results)
    Magnesium.grid(row=4, column=1)
    Sodium = Entry(results)
    Sodium.grid(row=5, column=1)
    Protein = Entry(results)
    Protein.grid(row=6, column=1)

    Button(results, text='Calcium', command=calcium_result).grid(row=0, column=8, sticky=W)
    Button(results, text='Potassium', command=potassium_result).grid(row=0, column=9, sticky=W)
    Button(results, text='Phosphorous', command=phosphorous_result).grid(row=0, column=10, sticky=W)
    Button(results, text='Water', command=water_result).grid(row=0, column=11, sticky=W)
    Button(results, text='Quit', command=results.destroy).grid(row=4, column=0, sticky=W)
    Button(results, text='Calories', command=calories_result).grid(row=0, column=3, sticky=W, )
    Button(results, text='Carbohydrates', command=carbs_result).grid(row=0, column=4, sticky=W, )
    Button(results, text='Magnesium', command=magnesium_result).grid(row=0, column=5, sticky=W, )
    Button(results, text='Sodium', command=sodium_result).grid(row=0, column=6, sticky=W, )
    Button(results, text='Protein', command=protein_result).grid(row=0, column=7, sticky=W, )


second_window()
first_window()
app.mainloop()
box_results()
