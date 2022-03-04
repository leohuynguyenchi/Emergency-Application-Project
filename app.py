"""
My first application
"""

from re import M
from tkinter.messagebox import NO, QUESTION, YES
from turtle import onclick
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import webbrowser
import httpx
import geopy


class Emergency(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

#Contact
        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
    
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))

        name_box.add(name_label)
        name_box.add(self.name_input)
        
#Blood type
        blood_type = toga.Label(
            'Your blood type: ',
            style=Pack(padding=(0, 5))
        )
        self.blood_input = toga.Selection(style=Pack(flex=1), items = ['A positive', 'A negative', 'B positive', 'B negative', 'AB positive', 'AB negative', 'O positive', 'O negative'])
    
        blood_box = toga.Box(style=Pack(direction=ROW, padding=5))
        blood_box.add(blood_type)
        blood_box.add(self.blood_input)
#Age
        DOB = toga.Label(
            'Your Date of Birth: ',
            style=Pack(padding=(0, 5))
        )
        self.DOB_input = toga.TextInput(style=Pack(flex=1))
    
        DOB_box = toga.Box(style=Pack(direction=ROW, padding=5))
        DOB_box.add(DOB)
        DOB_box.add(self.DOB_input)
#Location
        Location = toga.Label(
            'Your current location: ',
            style=Pack(padding=(0, 5))
        )
        self.location_input = toga.TextInput(style=Pack(flex=1))
    
        location_box = toga.Box(style=Pack(direction=ROW, padding=5))
        location_box.add(Location)
        
# importing geopy library
        from geopy.geocoders import Nominatim
        
# calling the Nominatim tool
        loc = Nominatim(user_agent="GetLoc")
        
# entering the location name
        getLoc = loc.geocode(self.location_input)
        location_box.add(self.location_input)

        submit_button = toga.Button(
            'Submit',
            on_press=self.submit,
            style=Pack(padding=5, width = 500, height = 30)
        )
        submit1_button = toga.Button(
            'Submit',
            on_press=self.submit1,
            style=Pack(padding=5, width = 500, height = 30)
        )
        submit2_button = toga.Button(
            'Submit',
            on_press=self.submit2,
            style=Pack(padding=5, width = 500, height = 30)
        )

        submit3_button = toga.Button(
            'Submit',
            on_press=self.submit3,
            style=Pack(padding=5, width = 500, height = 30)
        )


        button = toga.Button(
            'Emergency?',
            on_press = self.identify, style = Pack( width = 400, height = 50, padding = 20)   
        )
#Identify info
        button1 = toga.Button(
            'Identify',
            on_press=self.give,
            style=Pack(padding = 20, width = 400, height= 50)
        )
#Submit comment button
        button2 = toga.Button(
            'Submit emergency!',
            on_press=self.comment,
            style=Pack(padding=5, width = 500, height = 30)
        )
#Send pictures button        
        button3 = toga.Button(
            'Send your pictures',
            on_press=self.access,
            style=Pack(padding=20, width = 400, height = 60)
        )
#Access the location button
        button4 = toga.Button(
            'Access your location',
            on_press=self.map,
            style=Pack(padding=20, width = 400, height = 60)
        )
#Comment label
        emergency_label = toga.Label(
            'Emergency: ',
            style=Pack(padding=(0, 5))
        )
#Or label
        name_label1 = toga.Label(
            'AND/OR ',
            style=Pack(padding=(0,0))
        )

        self.emergency_input = toga.TextInput(style=Pack(width = 500, height = 50, flex=1))
        
        emergency_box = toga.Box(style=Pack(direction=ROW, padding=5))

        emergency_box.add(emergency_label)
        emergency_box.add(self.emergency_input)        

        main_box.add(button)

        main_box.add(name_box, submit3_button)
        main_box.add(DOB_box, submit1_button)
        main_box.add(blood_box, submit_button)
        main_box.add(location_box, submit2_button) 

        main_box.add(button1)              
        main_box.add(emergency_box)

        main_box.add(button2)
        main_box.add(button3, name_label1, button4)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def identify(self, widget):
        self.main_window.info_dialog(
            'Warning!',
            'If it is an EMERGENCY, follow through this app.'
        )
    def give(self, widget):
        self.main_window.info_dialog(
            'Warning!',
            'Provide your emergency below and follow through. '
        )
    def access(self, widget):
        self.main_window.info_dialog(
            'Warning!',
            'Access your camera to take and send the pictures to us.'
        )
        self.main_window.select_folder_dialog("Send your picture","",multiselect = True)
        if True:
            self.main_window.info_dialog(
            'Warning!',
            'Your picture has been submitted.'
            ) 
            
#Go up to Google Map to cap screenshot of current Location
    def map(self, widget):
        self.main_window.info_dialog(
            'Warning!',
            'Take the picture of your location using GPS from Google Map and send it to us. If you are on a moving vehicle, wait until it stops.'
        )
        self.main_window.info_dialog(
            'Warning!',
            'You will need to take the picture of your location and send it to us'
        ) 
        webbrowser.open("https://www.google.com/maps")
        self.main_window.info_dialog(
            'Warning!',
            'Get your picture ready.'
        ) 
    
        self.main_window.select_folder_dialog("Send your picture","",multiselect = False)
        self.main_window.info_dialog(
            'Warning!',
            'Your picture has been submitted.'
        ) 
        self.main_window.info_dialog(
            'Warning!',
            'STAY AT YOUR LOCATION! HELP IS ON THE WAY!'
        )             
            
#Submit each categories to the main screen
    def submit(self, widget):
        print(self.blood_input.value)

    def submit1(self, widget):
        print(self.DOB_input.value)

    def submit2(self, widget):
        print(self.location_input.value)
    
    def submit3(self, widget):
        print(self.name_input.value)
        
#Instruction for submitting pictures        
    def comment(self, widget):
        print(self.emergency_input.value)
        self.main_window.info_dialog(
            'Warning!',
            'The emergency has been submitted. The following steps will ask you to send pictures of the situation. If you cannot do that, click on the "Access your location" button.'
        )

    async def say_hello(self, widget):
        if self.name_input.value:
            name = self.name_input.value
        else:
            name = 'stranger'

        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json()

        self.main_window.info_dialog(
            "Hello, {}".format(name),
            payload["body"],
        )
    
def main():
    return Emergency()