# импортируем библиотеку abc для реализации абстрактных классов
import abc
# импортируем разметку клавиатуры и клавиш
from markup.markup import Keyboards
# импортируем класс-менеджер для работы с биьлиотекой
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализация разметки кнопок
        self.keyboards = Keyboards()
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
