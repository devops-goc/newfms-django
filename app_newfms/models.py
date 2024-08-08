from django.db import models

class Alarma(models.Model):
    ID = models.BigAutoField(primary_key=True)
    TECNOLOGIA = models.CharField(max_length=10, default='')
    FILTRO = models.CharField(max_length=10, default='')
    CODIGO = models.CharField(max_length=10, default='')
    HUB = models.CharField(max_length=10, default='')
    AMO = models.CharField(max_length=256, default='')
    DESCRIPCION = models.CharField(max_length=256, default='')
    SEVERIDAD = models.CharField(max_length=10, default='')
    FIRSTTIME = models.DateTimeField(auto_now_add=True)
    LASTTIME = models.DateTimeField(auto_now=True)
    CONTADOR = models.BigIntegerField(default=1)
    USER = models.CharField(max_length=50, default='JIPAM')
    ACK = models.BigIntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'ALARMA'
        unique_together = ('TECNOLOGIA', 'AMO')
        indexes = [
            models.Index(fields=['TECNOLOGIA']),
            models.Index(fields=['FILTRO']),
            models.Index(fields=['CODIGO']),
            models.Index(fields=['HUB']),
            models.Index(fields=['SEVERIDAD']),
        ]
