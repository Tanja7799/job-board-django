from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва вакансії')
    company = models.CharField(max_length=255, verbose_name='Компанія')
    location = models.CharField(max_length=255, verbose_name='Локація')
    link = models.URLField(unique=True, verbose_name='Посилання на вакансію')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')

    class Meta:
        verbose_name = "Вакансія"
        verbose_name_plural = "Вакансії"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title} - {self.company}'