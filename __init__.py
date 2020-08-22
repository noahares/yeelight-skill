from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from yeelight import Bulb

bulb = Bulb("192.168.0.129")

class Yeelight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        yeelight_on_intent = IntentBuilder('OnIntent').require('lightKeyword').require('onKeyword').build()
        self.register_intent(yeelight_on_intent, self.handle_yeelight_on_intent)

    def handle_yeelight_on_intent(self, message):
        self.speak_dialog('yeelight.on')
        bulb.turn_on()

def stop(self):
    pass

def create_skill():
    return Yeelight()
