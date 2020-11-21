import pygame as pg


class App:
    """
    Класс приложения.
    Управляет всеми процессами приложений.
    """
    def __init__(self):
        """
        Инициализация главных настроек приложения.
        """
        
        # Настройка окна игры.
        self.WIDTH = 1200
        self.HIGHT = 600
        self.TITLE = 'alien invasion'
        self.WINDOW = pg.display.set_mode((self.WIDTH, self.HIGHT))
        pg.display.set_caption(self.TITLE)


    def quit(self):
        """
        Завершает программу.
        """

        pg.quit()
        quit()


    def check_events(self):
        """
        Обработка событий программы.
        """

        # Нажатие на крестик.
        [self.quit() for event in pg.event.get() if event.type == pg.QUIT]


    def run(self):
        """
        Запуск главного цикла приложения.
        """

        while True:
            self.check_events()




