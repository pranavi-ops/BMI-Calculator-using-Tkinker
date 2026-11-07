import tkinter as tk

screen=tk.Tk("screen1")
screen.geometry("500x500")
screen.title("BMI Calculator")
screen.configure(bg="pink")


title=tk.Label(screen,text="BMI calculator", bg="white", fg="black", font=("arial", 20, "bold"), borderwidth=2, border=0.5)
title.pack(pady=50)
height_label=tk.Label(screen,text="Height(cm)", bg="pink", fg="black", font=("arial", 15))
height_label.place(x=20,y=100)
weight_label=tk.Label(screen,text="Weight(kg)", bg="pink", fg="black", font=("arial", 15))
weight_label.place(x=20,y=140)

height_input=tk.Entry(screen, width=25, justify="center")
#height_input.insert(0,"height in cm")
height_input.place(x=150, y=100)

weight_input=tk.Entry(screen, width=25, justify="center")
#weight_input.insert(0,"weight in kg")
weight_input.place(x=150, y=140)

def calculate_bmi():
    
    height_cm=float(height_input.get())
    weight_kg=float(weight_input.get())
    
    if height_cm<0 or weight_kg<0:
        result_label.configure(text="Your Input is Invalid")
        return
    
    if (height_cm<=91 or height_cm>=272) and (weight_kg<=25 or weight_kg>=454):
        label1.configure(text="Please enter a weight between 24.947 kgs and 453.592 kgs\n Height between 91.44 cm and 271.78 cm.", bg="red")
        return 
    
    if height_cm<=91 or height_cm>=272:
        label1.configure(text="Please enter a height between 91.44 cm and 271.78 cm.", bg="red")
        return
    if weight_kg<=25 or weight_kg>=454:
        label1.configure(text="Please enter a weight between 24.947 kgs and 453.592 kgs.", bg="red")
        return
  
    
    height_m=height_cm/100
    bmi=weight_kg/height_m**2
    
    if bmi<=18.5:
        result_label.configure(text= f"Your BMI is: {round(bmi,2)} kg/m2 \n You are underweight", fg="white")
    elif bmi>=18.5 and bmi<=24.9:
        result_label.configure(text= f"Your BMI is: {round(bmi,2)} kg/m2 \n You are healthy", fg="green")
    elif bmi>=25 and bmi<=29.9:
        result_label.configure(text= f"Your BMI is: {round(bmi,2)} kg/m2 \n You are overweight", fg="blue")
    else:
        result_label.configure(text= f"Your BMI is: {round(bmi,2)} kg/m2 \n You are obese", fg="purple")   
button1 = tk.Button(screen, text="Calculate BMI", command=calculate_bmi, bg="skyblue")
button1.place(x=150, y=200)

def clear_all():
    result_label.configure(text= "Result: ", fg="black")
    height_input.delete(0,tk.END)    
    weight_input.delete(0,tk.END)
    label1.configure(text="", bg="pink")
    
button2 = tk.Button(screen, text="Clear All", command=clear_all, bg="red")
button2.place(x=250, y=200)


label1=tk.Label(screen, text="", bg="pink", fg="white", font=("arial", 10, "bold"))
label1.place(x=20, y=250)
result_label=tk.Label(screen,text="Result: ", bg="pink", fg="green", font=("arial", 25, "bold"))
result_label.place(x=20,y=300)



screen.mainloop()

#write a code to make sure that the height is between this range: Please enter a height between 91.44 cm and 271.78 cm.
#Please enter a weight between 24.947 kgs and 453.592 kgs.
#https://www.nhlbi.nih.gov/calculate-your-bmi
