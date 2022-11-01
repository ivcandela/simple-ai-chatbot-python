class TerminalInterface:
    class Color:
        PINK = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        GOLDEN = '\033[93m'
        RED = '\033[91m'

    @staticmethod
    def get_user_input(name="User: ", name_colour=Color.PINK):
        """Text and color of the chatbot (user side) can be personalized"""
        user_input = input(f"{name_colour}{name}")
        return user_input

    @staticmethod
    def bot_response(text, name="Bot: ", name_colour=Color.GOLDEN, text_colour=Color.RED):
        """Text and color of the chatbot (bot side) can be personalized"""
        print(f"{name_colour}{name}{text_colour}{text}")
