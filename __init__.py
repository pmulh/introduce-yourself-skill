from mycroft import MycroftSkill, intent_file_handler


class IntroduceYourself(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('yourself.introduce.intent')
    def handle_yourself_introduce(self, message):
        self.speak_dialog('yourself.introduce')
        # TODO - wait for response and use name to say 'hello <name>'
        self.speak_dialog('pleasantries_1')
        # TODO - add a special response when the name received above is 'David' or 'Dave'
        # Something like 'Hi David, it's nice to me-- I'm sorry Dave, I'm afraid I can't do that'
        self.speak_dialog('pleasantries_2')


def create_skill():
    return IntroduceYourself()

