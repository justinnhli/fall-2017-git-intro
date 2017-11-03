class Cookies:
    def __init__(self, initial_tasty_level=100, tasty_level_decay=0):
        self.initial_tasty_level = initial_tasty_level

        self.tasty_level_decay = tasty_level_decay

    def get_current_tasty_level(self, current_time):
        current_tasty_level = self.initial_tasty_level - self.tasty_level_decay * current_time

        return current_tasty_level


if __name__ == '__main__':
    cookie = Cookies(1000, 10)

    print(cookie.get_current_tasty_level(20))