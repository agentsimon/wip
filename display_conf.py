import pygame
import requests
from PIL import Image
from io import BytesIO
import datetime


display = pygame.display.set_mode((480,256))

        # Display the information
def data2_display(data, hour_req):
    
    pygame.init()
    font = pygame.font.SysFont("arial", 24)
    h1_font = pygame.font.SysFont("arial", 32)
    #display = pygame.display.set_mode((480,256))
# Fill the display with this colour
    display.fill((100,10,10))
    pygame.display.set_caption("Weather")  
    pygame.display.flip()
    #pygame.display.update()  


    current_icon = (data["hourly"][hour_req]['weather'][0]["icon"])

        # create image from URL
    rsp = requests.get('http://openweathermap.org/img/wn/'+current_icon+'@4x.png')
    pilimage = Image.open(BytesIO(rsp.content)).convert("RGBA")

    pgimg = pygame.image.fromstring(pilimage.tobytes(), pilimage.size, pilimage.mode)

    display.blit(pgimg,(30,40))
    #current_weather = h1_font.render('Current weather', True, (255,255,255))
    date_info = data["hourly"][hour_req]["dt"]
    current_weather = font.render((datetime.datetime.fromtimestamp(data["hourly"][hour_req]["dt"]).strftime('%m-%d %H:%M')), True, (255,255,255))
    display.blit(current_weather,(10,30))
    current_temp = font.render('Temperature: '+f'{(data["hourly"][hour_req]["temp"])-273:.2f} C', True, (255,255,255))
    display.blit(current_temp,((display.get_width()-current_temp.get_width())-20,90))
    current_hum = font.render('Humidity: '+str((data["hourly"][hour_req]["humidity"]))+'%', True, (255,255,255))
    display.blit(current_hum,((display.get_width()-current_hum.get_width())-20,120))
    current_wind = font.render('Wind speed: '+f'{(((data["hourly"][hour_req]["wind_speed"])*3600)/1000):.0f}  kph', True, (255,255,255))
    display.blit(current_wind,((display.get_width()-current_wind.get_width())-20,150))
    display.blit(current_weather,(10,30))
# Final print to display
    
    pygame.display.update() 
    print("Display done")

    #Remove thus at a alter date 
    while True:
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
