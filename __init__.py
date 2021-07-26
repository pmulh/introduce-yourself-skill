from mycroft import MycroftSkill, intent_file_handler
from mycroft.api import DeviceApi # To get the name of this device
import time # For the sleep function
from random import random

class IntroduceYourself(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('yourself.introduce.intent')
    def handle_yourself_introduce(self, message):
        device_name = DeviceApi().get().get('name')
        self.speak_dialog("Hello, I'm " + device_name + ", a unique \
                           implementation of the Mycroft AI project")
        name = self.get_response('name.it', num_retries=0)
        # If no name given, try again
        if not name:
            self.speak_dialog("Sorry, I didn't catch that")
            name = self.get_response('name.it', num_retries=0)

        # We've either got the name by now, or have tried twice and will give up
        if name:
            if name.lower() in ['david', 'dave']:
                self.speak_dialog("Hello " + name + ", it's nice to meet you.")
                self.speak_dialog("I am")
                time.sleep(6)
                self.speak_dialog("An unexpected error has occured, please wait")
                time.sleep(8)
                self.speak_dialog("I'm sorry Dave")
                self.speak_dialog("I'm afraid I can't do that")
            elif random() > 0.8:
                self.speak_dialog("Oh, hello " + name + ", I've heard all about you.")
            else:
                self.speak_dialog('Hello ' + name)
        else:
            self.speak_dialog('Well, hello anyway, whatever your name is')
        if not name or name not in ['david', 'dave']:
            self.speak_dialog('pleasantries_1')
            self.speak_dialog('pleasantries_2')


def create_skill():
    return IntroduceYourself()

