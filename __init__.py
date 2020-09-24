from mycroft import MycroftSkill, intent_file_handler
from adapt.intent import IntentBuilder
from yeelight import Bulb, Flow
from yeelight.transitions import *
from time import sleep

bulb = Bulb("192.168.0.129")
effect_delay = 1000

class Yeelight(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        bulb_ip = self.settings.get('bulb_ip', "192.168.0.129")
        bulb = Bulb(bulb_ip, auto_on=True)

        yeelight_on_intent = IntentBuilder('OnIntent').require('lightKeyword').require('onKeyword').build()
        self.register_intent(yeelight_on_intent, self.handle_yeelight_on_intent)

        yeelight_off_intent = IntentBuilder('OffIntent').require('lightKeyword').require('offKeyword').build()
        self.register_intent(yeelight_off_intent, self.handle_yeelight_off_intent)

        yeelight_dim_intent = IntentBuilder('dimIntent').require('lightKeyword').require('dimKeyword').build()
        self.register_intent(yeelight_dim_intent, self. handle_yeelight_dim_intent)

        yeelight_bright_intent = IntentBuilder('brightIntent').require('lightKeyword').require('brightKeyword').build()
        self.register_intent(yeelight_bright_intent, self.handle_yeelight_bright_intent)

        yeelight_night_intent = IntentBuilder('nightIntent').require('lightKeyword').require('nightKeyword').build()
        self.register_intent(yeelight_night_intent, self.handle_yeelight_night_intent)

    def handle_yeelight_on_intent(self, message):
        self.speak_dialog('yeelight.on')
        bulb.turn_on()

    def handle_yeelight_off_intent(self, message):
        self.speak_dialog('yeelight.off')
        bulb.turn_off()

    def handle_yeelight_dim_intent(self, message):
        self.speak_dialog('yeelight.dim')
        bulb.set_brightness(5, duration=effect_delay)

    def handle_yeelight_bright_intent(self, message):
        self.speak_dialog('yeelight.bright')
        bulb.stop_flow()
        bulb.set_color_temp(3500)
        bulb.set_brightness(80, duration=effect_delay)

    def handle_yeelight_night_intent(self, message):
        self.speak_dialog('yeelight.night')
        bulb.stop_flow()
        bulb.set_color_temp(1700)
        bulb.set_brightness(1, duration=effect_delay)

    @intent_file_handler('brightness.intent')
    def handle_yeelight_brightness_intent(self, message):
        brightness = int(message.data.get('brightness'))
        self.speak_dialog('yeelight.brightness')
        bulb.set_brightness(brightness, duration=effect_delay)

    @intent_file_handler('colortemp.intent')
    def handle_yeelight_colortemp_intent(self, message):
        temp = message.data.get('temp')
        if temp == 'cold':
            temp = 5700
        elif temp == 'warm':
            temp = 2300
        else:
            temp = int(temp)
        self.speak_dialog('yeelight.colortemp')
        bulb.set_color_temp(temp, duration=effect_delay)

def stop(self):
    pass

def create_skill():
    return Yeelight()
