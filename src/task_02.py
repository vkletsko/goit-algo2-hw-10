# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, own_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.own_subjects = own_subjects
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.age} років, email: {self.email}"


def create_schedule(subjects, teachers):
    schedule = []
    subjects_pool = set(subjects)

    while subjects_pool:
        teachers = sorted(
            teachers,
            key=lambda t: (-len(t.own_subjects & subjects_pool), t.age)
        )

        for teacher in teachers:
            available_subjects = teacher.own_subjects & subjects_pool
            if available_subjects:
                assigned_subject = available_subjects.pop()
                teacher.assigned_subjects.add(assigned_subject)
                subjects_pool.remove(assigned_subject)
                schedule.append(teacher)
                break
        else:
            return None

    return schedule


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Інформатика', 'Історія',
                'Географія', 'Фізика', 'Хімія', 'Біологія'}

    # Список викладачів
    teachers = [
        Teacher("Василь", "Ігоревич", 35, "v.igori4@example.com",
                {"Математика", "Інформатика"}),
        Teacher("Віталіна", "Стерненко", 38,
                "v.sternenko@example.com", {"Географія"}),
        Teacher("Олексій", "Тулько", 50,
                "o.tulkoko@example.com", {"Фізика", "Біологія"}),
        Teacher("Олеся", "Петрівна", 29, "o.petrivna@example.com",
                {"Історія", "Географія"}),
        Teacher("Олег", "Пушко", 35, "o.pushko@example.com",
                {"Фізика", "Математика"}),
        Teacher("Наталья", "Гарашко", 42,
                "n.garashko@example.com", {"Історія"}),
        Teacher("Люся", "Хімікашко", 42,
                "l.chimikashko@example.com", {"Хімія"})
    ]

    # Cтворення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in teachers:
            if teacher.assigned_subjects:
                print(
                    f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
                print(
                    f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
