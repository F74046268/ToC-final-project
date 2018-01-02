from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'attack red slime'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'attack blue slime'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'attack green slime'
    
    def on_enter_state1(self, update):
        update.message.reply_text("Congradulaions! You are Swordman now.")
        update.message.reply_text("Oh no!A Demogorgan show up!")
        update.message.reply_text("Demogorgan starts attack.")
        update.message.reply_text("You died.")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("Congradulaions! You are Magician now.")
        update.message.reply_text("Oh no!A Demogorgan show up!")
        update.message.reply_text("Demogorgan starts attack.")
        update.message.reply_text("You died.")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
        
    def on_enter_state3(self, update):
        update.message.reply_text("Congradulaions! You are Archer now.")
        update.message.reply_text("Oh no!A Demogorgan show up!")
        update.message.reply_text("Demogorgan starts attack.")
        update.message.reply_text("You died.")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
        
