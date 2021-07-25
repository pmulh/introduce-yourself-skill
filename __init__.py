from mycroft import MycroftSkill, intent_file_handler


class IntroduceYourself(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('yourself.introduce.intent')
    def handle_yourself_introduce(self, message):
        self.speak_dialog('yourself.introduce')


def create_skill():
    return IntroduceYourself()

