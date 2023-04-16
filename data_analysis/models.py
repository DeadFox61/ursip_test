from django.db import models


class AnalysisAbstract(models.Model):
    fact_Qliq_data1 = models.IntegerField()
    fact_Qliq_data2 = models.IntegerField()
    fact_Qoil_data1 = models.IntegerField()
    fact_Qoil_data2 = models.IntegerField()
    forecast_Qliq_data1 = models.IntegerField()
    forecast_Qliq_data2 = models.IntegerField()
    forecast_Qoil_data1 = models.IntegerField()
    forecast_Qoil_data2 = models.IntegerField()

    class Meta:
        abstract = True


class Analysis(AnalysisAbstract):
    """Одна строка измерения + прогноза"""

    company_name = models.CharField("Название компании", max_length=255)
    date = models.DateField("Дата анализа")

    def __str__(self):
        return f"Анализ {self.pk}"

    class Meta:
        verbose_name = "Строка данных"
        verbose_name_plural = "Строки данных"


class AnalysisSumByDate(AnalysisAbstract):
    """Сумма данных сгруппированных по дате"""

    date = models.DateField("Дата", unique=True)

    def __str__(self):
        return f"Тотал за {self.date}"

    class Meta:
        ordering = ("date",)
        verbose_name = "Расчетный тотал по дате"
        verbose_name_plural = "Расчетные тоталы по дате"
