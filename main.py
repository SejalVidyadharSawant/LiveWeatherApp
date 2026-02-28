import tkinter as tk
import requests     #pip install requests
from PIL import Image,ImageTk   #pip install pillow

root=tk.Tk()

root.title("Live Weather App")
root.geometry("600x500")

#api ket = 68ac1a9f5efc5d765e77da1a0eb5fbef
#Api url = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#API url = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
        try:
            city=weather['name']
            condition=weather['weather'][0]['description']
            temp = weather['main']['temp']
            feels = weather['main']['feels_like']
            humidity = weather['main']['humidity']
            wind = weather['wind']['speed']
            

            final_str=' City : %s\n Condition : %s,\n Tempeture : %s\n Feels like : %s\n Humidity : %s,\n Wind : %s'%(city,condition,temp,feels,humidity,wind)


            # final_str = f'''City : {city}
            #     Condition : {condition}
            #     Temperature : {temp} °C 
            #     Feels like : {feels} °C
            #     Humidity : {humidity} %
            #     Wind : {wind} m/s'''
        
        except:
             final_str='There was a problem retriveing taht information'

        return final_str

def get_weather(city):
    result['text'] = "Loading..."
    weather_key='68ac1a9f5efc5d765e77da1a0eb5fbef'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={
        'appid':weather_key,
        'q': city,
        #'units':'imperial'
        'units':'metric'
        }
    
    response = requests.get(url, params=params)
    # print(response.json())

    weather=response.json()
    if weather['cod'] != 200:
         result['text'] = "City not found "
         return

    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

# def open_image(icon):
#      size=int(frame_two.winfo_height()*0.25)
#      img=ImageTk.PhotoImage(Image.open('img/'+icon+'.png').resize((size,size)))
#      weather_icon.delete('all')
#      weather_icon.create_image(0,0,anchor='nw',image=img)
#      weather_icon.image=img

def open_image(icon):
    size = int(frame_two.winfo_height()*0.25)

    url = f"https://openweathermap.org/img/wn/{icon}@2x.png"

    response = requests.get(url, stream=True)

    img = Image.open(response.raw).resize((size, size))
    img = ImageTk.PhotoImage(img)

    weather_icon.delete('all')
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


img=Image.open('./bg.jpg')
img = img.resize((600, 500), Image.Resampling.LANCZOS)     #img=img.resize((600,500),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text=' Live Weather for All Cities Worldwide ',fg="#3007A9",bg="#EAEAF4",font=('Algerian',18,'bold'))
heading_title.place(relx=0.5, y=15,anchor='n')

frame_one=tk.Frame(bg_lbl,bg="red",bd=5)
frame_one.place(x=80,y=70,width=450,height=51)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='Get Weather',fg='green',font=('Arial Black',13,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=13)

frame_two=tk.Frame(bg_lbl,bg='red',bd=5)
frame_two.place(x=80,y=150,width=450,height=300)

result=tk.Label(frame_two,bg='white',font=('times new roman',16,'bold'),justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)


root.mainloop()