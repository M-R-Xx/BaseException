class InvalidInputError(BaseException):
    pass


class PermissionDeniedError(BaseException):
    pass


class DataProcessor:
    def validate_data(self, data):
        if not data:
            raise InvalidInputError("Некорректные данные переданы для обработки")

    def process_data(self, data):
        try:
            self.validate_data(data)
            print("Данные успешно обработаны.")
        except InvalidInputError as e:
            raise InvalidInputError(f"Ошибка при обработке данных: {str(e)}")

    def check_permission(self, user):
        if not user.is_admin:
            raise PermissionDeniedError("У пользователя отсутствуют необходимые права доступа")

    def save_data(self, data, user):
        try:
            self.check_permission(user)
            print("Данные успешно сохранены.")
        except PermissionDeniedError as e:
            raise PermissionDeniedError(f"Ошибка при сохранении данных: {str(e)}")


class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin


class Application:
    def __init__(self):
        self.data_processor = DataProcessor()

    def process_data(self, data, user):
        try:
            self.data_processor.process_data(data)
            self.data_processor.save_data(data, user)
        except InvalidInputError as e:
            print(f"Ошибка ввода данных: {str(e)}")
        except PermissionDeniedError as e:
            print(f"Ошибка доступа: {str(e)}")
        except Exception as e:
            print(f"Необработанная ошибка: {str(e)}")


app = Application()
user = User(is_admin=True)
data = "Example Data"
app.process_data(data, user)
