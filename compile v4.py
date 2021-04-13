from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import requests, json
import pandas as pd
from pandas import DataFrame
import random

#UI PLACEMENT-----------------------------------------------------------------------------------------------------------------#
root = Tk(className="Weather wear")
root.geometry("320x480")

#WEATHER & TIPS LISTS---------------------------------------------------------------------------------------------------------#
#weather tip 1 - light rain
rainLight = ["light rain", "light intensity shower rain"]
rainLightSuggest = ["Dont forget your umbrella!" , 
                    "A hat, hat, hat to protect your head, head, head", 
                    "Time to bring out your hat!"]
#weather tip 2 - moderate rain
rainMod = ["moderate rain", "shower rain", "rain"]
rainModSuggest = ["Dont forget your umbrella!", 
                    "Dont forget your raincoat!",
                    "Grab your raincoat!"]
#weather tip 3 - heavy rain
rainHeavy = ["heavy intensity rain", "very heavy rain", "extreme rain", "freezing rain", "heavy intensity shower rain", "ragged shower rain"]
rainHeavySuggest = ["Time to bring out the rain boots", 
                    "Time to polish your rain boots!",
                    "Dont forget your raincoat!",
                    "Layer up! it'll be windy!"]
#weather tip 4 - light thunder storm
thunderLight = ["thunderstorm with light rain", "light thunderstorm", "thunderstorm with light drizzle"]
thunderLightSuggest = ["Layer up! a light storm is coming your way",
                    "A hat, hat, hat to protect your head, head, head",
                    "Layer up! prepare for the wind"]
#weather tip 5 - moderate thunder storm
thunderMod = ["thunderstorm with rain", "thunderstorm", "thunderstorm with drizzle", "thunderstorm"]
thunderModSuggest = ["Layer up! a thunderstorm is coming your way", 
                    "Laye up your sweater! It's going to be windy",
                    "Dont forget your raincoat!"]
#weather tip 6 - heavy thunder storm
thunderHeavy = ["thunderstorm with heavy rain", "heavy thunderstorm", "ragged thunderstorm", "thunderstorm with heavy drizzle"]
thunderHeavySuggest = ["Stay inside or layer up!",
                    "Layer up! its going to be windy", 
                    "Maybe forget about that flip flops",
                    "Time to bring our your rain boots!"]
#weather tip 7 - light drizzle
drizzleLight = ["light intensity drizzle", "light intensity drizzle rain"]
drizzleLightSuggest = ["A hat, hat, hat to protect your head, head, head",
                    "Maybe forget about that flip flops, and opt for that boots",
                    "Don't forget your hat!"]
#weather tip 8 - moderate drizzle 
drizzleMod = ["drizzle", "drizzle rain", "shower rain and drizzle", "shower drizzle"]
drizzleModSuggest = ["Don't forget your raincoat!",
                    "Time to bring out your raincoat!",
                    "A hat, hat, hat to protect your head, head, head",
                    "Rainboots if you're feeling extra"]
#weather tip 9 - heavy drizzle
drizzleHeavy = ["heavy intensity drizzle", "heavy intensity drizzle rain", "heavy shower rain and drizzle"]
drizzleHeavySuggest = ["Don't forget your umbrella!",
                    "Time to bring out your raincoat!"]
#weather tip 10 - light snow 
snowLight = ["light snow", "Light shower sleet", "Light rain and snow", "Light shower snow"]
snowLightSuggest = ["Time to bring out a thicker coat!",
                    "It's sweater weather!"]
#weather tip 11 - moderate snow
snowMod = ["Snow", "Sleet", "Rain and snow", "Shower snow", "snow"]
snowModSuggest = ["Time to bring out a thicker coat!",
                    "It's sweater weather!"]
#weather tip 12 - heavy snow
snowHeavy = ["Heavy snow", "Shower sleet", "Heavy shower snow"]
snowHeavySuggest = ["Time to bring out a thicker coat!",
                    "It's sweater weather!"]
#weather tip 13 - mist 
atmospheric = ["mist", "Smoke", "Haze", "sand/ dust whirls", "fog", "sand", "dust", "volcanic ash", "squalls", "tornado"]
atmoSuggest = ["Wear your mask Today!",
                    "A hat and glasses to protect you from the dust!",
                    "Dont forget your mask! it will be dusty today"]
#weather tip 14 - clear sky
clear = ["clear sky"]
clearSuggest = ["Time to bring out your flip flops!",
                    "Time to raid your sunglasses collection!", 
                    "Don't forget your sun screen!",
                    "Avoid black clothing items to avoid over heating!"]
#weather tip 15 - clouds 
clouds = ["few clouds: 11-25%", "scattered clouds: 25-50%", "broken clouds: 51-84%", "overcast clouds: 85-100%", "few clouds", "scattered clouds", "broken clouds"]
cloudsSuggest = ["Maybe rethink that flip flops, its a little windy today", 
                    "layer up, its a little cloudy today"]

#--------------------------------------------------------------------------------------------------------------------------#
# base URL
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
    # -6.274259859821331, 106.71096816585639
BASE_URL = "https://api.openweathermap.org/data/2.5/onecall?"
LATITUDE = "1.290270"
LONGITUDE = "103.851959"
API_KEY = "deeed82620935ce57fe10b65b34c7975"
UNITS = "metric"
EXCLUDE = "minutely,daily,alerts"
# upadting the URL
URL = BASE_URL + "lat=" + LATITUDE + "&lon=" + LONGITUDE + "&appid=" + API_KEY + "&units=" + UNITS + "&exclude=" + EXCLUDE
# HTTP request
response = requests.get(URL)


def update():
    print("-------------------------------------------------------------------------------------------------------------")
    #updates here
    print("SOFTWARE IS UPDATING...")
    print("-------------------------------------------------------------------------------------------------------------")
    
    #1. light rain
    if hourlyWeather['description'] in rainLight:
        lightRainTips = random.choice(rainLightSuggest)
        lightRainTip.config(text=lightRainTips)
        print("Tip of the day:", lightRainTips)
    
    #2. moderate rain
    if hourlyWeather['description'] in rainMod:
        modRainTips = random.choice(rainModSuggest)
        modRainTip.config(text=modRainTips)
        print("Tip of the day:", modRainTips)

    #3. heavy rain
    if hourlyWeather['description'] in rainHeavy:
        heavyRainTips = random.choice(rainHeavySuggest)
        heavyRainTip.config(text=heavyRainTips)
        print("Tip of the day:", heavyRainTips)

    #4. light thunder
    if hourlyWeather['description'] in thunderLight:
        lightThunderTips = random.choice(thunderLightSuggest)
        lightThunderTip.config(text=lightThunderTips)
        print("Tip of the day:", lightThunderTips)

    #5. moderate thunder
    if hourlyWeather['description'] in thunderMod:
        modThunderTips = random.choice(thunderModSuggest)
        modThunderTip.config(text= modThunderTips)
        print("Tip of the day:", modThunderTips)

    #6. heavy thunder
    if hourlyWeather['description'] in thunderHeavy:
        heavyThunderTips = random.choice(thunderHeavySuggest)
        heavyThunderTip.config(text=heavyThunderTips)
        print("Tip of the day:", heavyThunderTips)

    #7. light drizzle
    if hourlyWeather['description'] in drizzleLight:
        lightDrizzleTips = random.choice(drizzleLightSuggest)
        lightDrizzleTip.config(text=lightDrizzleTips)
        print("Tip of the day:", lightDrizzleTips)

    #8. moderate drizzle
    if hourlyWeather['description'] in drizzleMod:
        modDrizzleTips = random.choice(drizzleModSuggest)
        modDrizzleTip.config(text=modDrizzleTips)
        print("Tip of the day:", modDrizzleTips)

    #9. heavy drizzle
    if hourlyWeather['description'] in drizzleHeavy:
        heavyDrizzleTips = random.choice(drizzleHeavySuggest)
        heavyDrizzleTip.config(text=heavyDrizzleTips)
        print("Tip of the day:", heavyDrizzleTips)
    
    #10. light snow
    if hourlyWeather['description'] in snowLight:
        lightSnowTips = random.choice(snowLightSuggest)
        lightSnowTip.config(text=lightSnowTips)
        print("Tip of the day:", lightSnowTips)

    #11. moderate snow
    if hourlyWeather['description'] in snowMod:
        modSnowTips = random.choice(snowModSuggest)
        modSnowTip.config(text=modSnowTips)
        print("Tip of the day:", modSnowTips)

    #12. heavy snow
    if hourlyWeather['description'] in snowHeavy:
        heavySnowTips = random.choice(snowHeavySuggest)
        heavySnowTip.config(text=heavySnowTips)
        print("Tip of the day:", heavySnowTips)
    
    #13. atmospheric
    if hourlyWeather['description'] in atmospheric:
        atmoTips = random.choice(atmoSuggest)
        atmoTip.config(text= atmoTips)
        print("Tip of the day:", atmoTips)

    #14. cloudy
    if hourlyWeather['description'] in clouds:
        cloudTips = random.choice(cloudsSuggest)
        cloudyTip.config(text=cloudTips)
        print("Tip of the day:", cloudTips)


    #current weather data set configuration
    tempNow.config(text=tempNowMod)
    print("Current Temperature:", tempNowMod)
    mainNow.config(text=mainNowCollect)
    descNow.config(text=descNowCollect)
    print("Current weather:", mainNowCollect, ",", descNowCollect)

    #weather data set in 2 hours
        #temperature
    updateTempTwo = hourly[2]['temp']
    updateTempTwo = round(updateTempTwo, 1)
    updatedTempTwo = updateTempTwo, "\N{DEGREE SIGN}C"
    tempTwo.config(text=updatedTempTwo)
    print("Temperature in 2 hours:", updatedTempTwo)
        #main
    weaIn2Collect = hourly[2]['weather']
    weaIn2Collect = weaIn2Collect[0]
    print(weaIn2Collect['main'])
    weaIn2Mod = weaIn2Collect['main']
    descTwo.config(text=weaIn2Mod)
    print("Weather in 2 hours:", weaIn2Mod)


    #weather data set in 4 hours
        #temperature
    updateTempFour = hourly[4]['temp']
    updateTempFour = round(updateTempFour, 1)
    updatedTempFour = updateTempFour, "\N{DEGREE SIGN}C"
    tempFour.config(text=updatedTempFour)
    print("Temperature in 4 hours:", updatedTempFour)
        #main
    weaIn4Collect = hourly[4]['weather']
    weaIn4Collect = weaIn4Collect[0]
    print(weaIn4Collect['main'])
    weaIn4Mod = weaIn4Collect['main']
    descFour.config(text=weaIn4Mod)
    print("Weather in 4 hours:", weaIn4Mod)


if response.status_code == 200:
    data = response.json()
    current = data['current']
    hourly = data['hourly']
    dataframe = pd.DataFrame.from_dict(data, orient="index")

    #Collect data set
    hourlyWeather = hourly[0]['weather'] # This is a 0 - length list
    hourlyWeather = hourlyWeather[0] # This is a dictionary
    

    #---TIP FRAME-----------------------------------------------------------------------------------------------------#
    #fixed values
    x= 10
    y= 6
    tipBg = "#ffffff"

    #image background
    imgFrame = tk.Frame(root, bg='#535353', width=320, height=480)
    imgFrame.place(x = -1,y = -1)
    imgFrame.pack_propagate(0)
    backImg = Image.open("wire.png")
    
    #restart button
    restartFrame = tk.Frame(root, bg='#535353', width=30, height=30)
    restartFrame.place(x = 268,y = 22)
    restartFrame.pack_propagate(0)

    restartImg = PhotoImage(file="Group 5.png")
    restartBtn = Button(restartFrame, image=restartImg, command=update) #insert command
    restartBtn.pack()

    #frame settings
    tipFrame = tk.Frame(root, bg=tipBg, width=170, height=80)
    tipFrame.place(x = 20,y = 40)
    tipFrame.pack_propagate(0)

    #condition 1 - light rain
    if hourlyWeather['description'] in rainLight:
        print(random.choice(rainLightSuggest))
        randomLightRainTip = random.choice(rainLightSuggest)
        global lightRainTip
        lightRainTip = Label(tipFrame, text=randomLightRainTip, wraplengt=150, bg=tipBg)
        lightRainTip.pack(anchor= CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 2 - moderate rain
    if hourlyWeather['description'] in rainMod:
        print(random.choice(rainModSuggest))
        radomModRainTip = random.choice(rainModSuggest)
        global modRainTip
        modRainTip = Label(tipFrame, text=radomModRainTip, wraplengt=150, bg=tipBg)
        modRainTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire3.png")

    #condition 3 - heavy rain
    if hourlyWeather['description'] in rainHeavy:
        print(random.choice(rainHeavySuggest))
        randomHeavyRainTip = random.choice(rainHeavySuggest)
        global heavyRainTip
        heavyRainTip = Label(tipFrame, text=randomHeavyRainTip, wraplengt=150, bg=tipBg)
        heavyRainTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 4 - light thunder
    if hourlyWeather['description'] in thunderLight:
        print(random.choice(thunderLightSuggest))
        randomLightThunderTip = random.choice(thunderLightSuggest)
        global lightThunderTip
        lightThunderTip = Label(tipFrame, text=randomLightThunderTip, wraplengt=150, bg=tipBg)
        lightThunderTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 5 - moderate thunder
    if hourlyWeather['description'] in thunderMod:
        print(random.choice(thunderModSuggest))
        randomModThunderTip = random.choice(thunderModSuggest)
        global modThunderTip
        modThunderTip = Label(tipFrame, text=randomModThunderTip, wraplengt=150, bg=tipBg)
        modThunderTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 6 - heavy thunder
    if hourlyWeather['description'] in thunderHeavy:
        print(random.choice(thunderHeavySuggest))
        randomHeavyThunderTip = random.choice(thunderHeavySuggest)
        global heavyThunderTip
        heavyThunderTip = Label(tipFrame, text=randomHeavyThunderTip, wraplengt=150, bg=tipBg)
        heavyThunderTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 7 - light drizzle
    if hourlyWeather['description'] in drizzleLight:
        print(random.choice(drizzleLightSuggest))
        randomLightDrizzleTip = random.choice(drizzleLightSuggest)
        global lightDrizzleTip
        lightDrizzleTip = Label(tipFrame, text=randomLightDrizzleTip, wraplengt=150, bg=tipBg)
        lightDrizzleTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 8 - moderate drizzle
    if hourlyWeather['description'] in drizzleMod:
        print(random.choice(drizzleModSuggest))
        randomModDrizzleTip = random.choice(drizzleModSuggest)
        global modDrizzleTip
        modDrizzleTip = Label(tipFrame, text=randomModDrizzleTip, wraplengt=150, bg=tipBg)
        modDrizzleTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 9 - heavy drizzle
    if hourlyWeather['description'] in drizzleHeavy:
        print(random.choice(drizzleHeavySuggest))
        randomHeavyDrizzleTip = random.choice(drizzleHeavySuggest)
        global heavyDrizzleTip
        heavyDrizzleTip = Label(tipFrame, text=randomHeavyDrizzleTip, wraplengt=150, bg=tipBg)
        heavyDrizzleTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 10 - light snow
    if hourlyWeather['description'] in snowLight:
        print(random.choice(snowLightSuggest))
        randomLightSnowTip = random.choice(snowLightSuggest)
        global lightSnowTip
        lightSnowTip = Label(tipFrame, text=randomLightSnowTip, wraplengt=150, bg=tipBg)
        lightSnowTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 11 - moderate snow
    if hourlyWeather['description'] in snowMod:
        print(random.choice(snowModSuggest))
        randomModSnowTip = random.choice(snowModSuggest)
        global modSnowTip
        modSnowTip = Label(tipFrame, text=randomModSnowTip , wraplengt=150, bg=tipBg)
        modSnowTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 12 - heavy snow
    if hourlyWeather['description'] in snowHeavy:
        print(random.choice(snowHeavySuggest))
        randomHeavySnowTip = random.choice(snowHeavySuggest)
        global heavySnowTip
        heavySnowTip = Label(tipFrame, text=randomHeavySnowTip, wraplengt=150, bg=tipBg)
        heavySnowTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 13 - atmospheric
    if hourlyWeather['description'] in atmospheric:
        print(random.choice(atmoSuggest))
        randomAtmoTip = random.choice(atmoSuggest)
        global atmoTip
        atmoTip = Label(tipFrame, text=randomAtmoTip, wraplengt=150, bg=tipBg)
        atmoTip.pack(anchor=CENTER, pady=x, padx=y)
        backImg = Image.open("wire.png")

    #condition 14 : cloudy
    if hourlyWeather['description'] in clouds:
        print(random.choice(cloudsSuggest))
        randomCloudyTip = random.choice(cloudsSuggest)
        global cloudyTip
        cloudyTip = Label(tipFrame, text=randomCloudyTip, wraplengt=150, bg=tipBg)
        cloudyTip.pack(anchor= CENTER, pady=x, padx=y)
        backImg = Image.open("cloudy.jpg")

    resized = backImg.resize((321,481), Image.ANTIALIAS)
    backImgNew = ImageTk.PhotoImage(resized)
    imgBg = Label(imgFrame, image = backImgNew)
    imgBg.place(x = 0,y = 0)
    imgBg.pack_propagate(0)

    #---CURRENT DATA FRAME-----------------------------------------------------------------------------------------------------#
    #fixed values
    mainBG = "#ffffff"
        
    nowFrame = tk.Frame(root, bg=mainBG , width=160, height=140)
    nowFrame.place(x = 20,y = 140)
    nowFrame.pack_propagate(0)

    #current temperature textbox
    tempNowCollect = hourly[0]['temp']
    tempNowCollect = round(tempNowCollect,1)
    print("weather: ", tempNowCollect )
    global tempNowMod
    tempNowMod = tempNowCollect,"\N{DEGREE SIGN}C"
    global tempNow 
    tempNow = Label(nowFrame, text=tempNowMod,
        font = ("Helvetica Neue",30),
        bg='#ffffff')
    tempNow.pack(pady=(18,0))

    #Main (weather condition) textbox 
    global mainNowCollect
    mainNowCollect = hourlyWeather['main']
    print(hourlyWeather['main'])
    global mainNow
    mainNow = Label(nowFrame, text=mainNowCollect,
                    font = ("Helvetica Neue",18),
                    bg='#ffffff')
    mainNow.pack(pady=(3,0))

    #Weather description textbox
    global descNowCollect
    descNowCollect = hourlyWeather['description']
    print(hourlyWeather['description'])
    global descNow
    descNow = Label(nowFrame, text=descNowCollect,
                    font=("Helvetica Neue", 14),
                    bg='#ffffff', fg='#7E7E7E',)
    descNow.pack(pady=(0, 0))

    #---WEATHER DATA SET IN THE NEXT 2 HOURS-----------------------------------------------------------------------------------------------------#
    #+2h data frame
    in2Frame = tk.Frame(root, bg='#ffffff', width=130, height=90)
    in2Frame.place(x=20, y=360)
    in2Frame.pack_propagate(0)

    #Image
    iconTwo = Image.open("clock.png")
    resized = iconTwo.resize((25, 25), Image.ANTIALIAS)
    iconTwoNew = ImageTk.PhotoImage(resized)
    my_label = Label(in2Frame, image=iconTwoNew, bg='#ffffff')
    my_label.pack(anchor=W, pady=(8, 0), padx=(12, 0))

    #temperature in 2 hours textbox
    global tempTwoCollect
    tempTwoCollect = hourly[2]['temp']
    tempTwoCollect = round(tempTwoCollect, 1)
    print("weather in 2 hours: ", tempTwoCollect)
    global tempTwoMod
    tempTwoMod = tempTwoCollect, "\N{DEGREE SIGN}C"
    global tempTwo
    tempTwo = Label(in2Frame, text=tempTwoMod,
                    font=("Helvetica Neue", 16),
                    bg='#ffffff')
    tempTwo.pack(anchor=W, padx=(12, 0), pady=(0, 0))

    #Main (weather condition in 2 hours) textbox
    global weatherIn2Collect
    weatherIn2Collect = hourly[2]['weather']
    weatherIn2Collect = weatherIn2Collect[0]
    print(weatherIn2Collect['main'])
    global weatherIn2Mod
    weatherIn2Mod = weatherIn2Collect['main']
    global descTwo
    descTwo = Label(in2Frame, text=weatherIn2Mod,
                    font=("Helvetica Neue", 12),
                    bg='#ffffff')
    descTwo.pack(anchor=W, padx=(12, 0), pady=(0, 0))

    #---WEATHER DATA SET IN THE NEXT 4 HOURS-----------------------------------------------------------------------------------------------------#
    #+4h data frame
    in4Frame = tk.Frame(root, bg='#ffffff', width=130, height=90)
    in4Frame.place(x=170, y=360)
    in4Frame.pack_propagate(0)

    #Image 
    iconFour = Image.open("clock.png")
    resized = iconFour.resize((25,25), Image.ANTIALIAS)
    iconFourNew = ImageTk.PhotoImage(resized)
    my_label = Label(in4Frame, image = iconTwoNew,bg='#ffffff')
    my_label.pack(anchor= W, pady=(8,0), padx=(12,0))

    #temperature in 4 hours textbox
    global tempFourCollect
    tempFourCollect = hourly[4]['temp']
    tempFourCollect = round(tempFourCollect,1)
    print("weather in 4 hours: ", tempFourCollect )
    global tempFourMod
    tempFourMod = tempFourCollect,"\N{DEGREE SIGN}C"
    global tempFour
    tempFour = Label(in4Frame, text=tempFourMod,
        font = ("Helvetica Neue",16),
        bg='#ffffff')
    tempFour.pack(anchor= W, padx=(12,0), pady=(0,0))
        
    #weather in 4 hours
    global weatherIn4Collect
    weatherIn4Collect = hourly[4]['weather']
    weatherIn4Collect = weatherIn4Collect[0]
    print(weatherIn4Collect['main'])
    global weatherIn4Mod
    weatherIn4Mod = weatherIn4Collect['main']
    global descFour
    descFour = Label(in4Frame, text=weatherIn4Mod,
        font = ("Helvetica Neue",12),
        bg='#ffffff')
    descFour.pack(anchor= W, padx=(12,0), pady=(0,0))

    #--------------------------------------------------------------------------------------------------------#
    #Looping TKInter
    root.mainloop()

else:
    print("Error in the HTTP request")