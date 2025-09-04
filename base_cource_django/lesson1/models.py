from django.db import models

# Create your models here.

"""
Создать форму для отправки отзыва на продукт для интернет-магазина. Форма должна вмещать:
● Файл с картинкой.
● Почту пользователя.
● Описание.
● Выбор оценки.
● Негативный или позитивный отзыв.
● Номер телефона.
"""

class Report(models.Model):
    POSITIV_NEGATIV = [
        ('1', "positiv"),
        ("2", "negativ"),
    ]
    image = models.ImageField(null=True, blank=True)
    email_user = models.EmailField( )
    text = models.TextField()
    rating = models.FloatField()
    positiv_or_negativ = models.CharField(max_length=10, choices=POSITIV_NEGATIV)
    telefon_number = models.CharField(max_length=13, help_text="ex: +380........")
    
    
    def __str__(self):
        return f"{self.email_user} {self.positiv_or_negativ}"
    
    
    