# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 03:18:44 2022

@author: PACMAN
"""
from twilio.rest import Client

client = Client("YOUR SID","YOUR TOKEN")

def create_text():
    
    sms = input("What do you want to say? ")
    sender = input("Enter your twilio #? ")
    receiver = input("Enter receiver #? ")
    msg = client.messages.create(
    to=receiver,
    from_=sender,
    body=sms
    
    print(msg)
    
    )
    
    
