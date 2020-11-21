import pygame as pg


class App:
    """
    Класс приложения.
    Управляет всеми процессами приложений.
    """
    def __init__(self):
        """
        Инициализация главных настроек приложения
        """
        
        # Настройка окна игры
        self.WIDTH = 1200
        self.HIGHT = 600
        self.TITLE = 'alien invasion'
        self.WINDOW = pg.display.set_mode((self.WIDTH, self.HIGHT))
        pg.display.set_caption(self.TITLE)

        


