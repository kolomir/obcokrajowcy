from django.db import models
from django.contrib.auth.models import User


class Dzial(models.Model):
    dzial = models.CharField(max_length=20, unique=True)
    aktywny = models.BooleanField(default=True)

    def __str__(self):
        return self.dzial


class Pracownik(models.Model):
    nr_akt = models.DecimalField(max_digits=4,decimal_places=0,unique=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=40)
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)
    zatrudniony = models.BooleanField(default=True)

    def pracownik(self):
        return '(' + str(self.nr_pracownika) + ') ' + self.nazwisko + ' ' + self.imie

    def __str__(self):
        return str(self.pracownik)


class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lider_dzial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lider")
    dzial = models.ForeignKey(Dzial, on_delete=models.CASCADE)

    def __str__(self):
        return "{}_{}".format(self.user.__str__(), self.dzial.__str__())


class rejestr(models.Model):
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    data_przyjscia = models.DateField('data przyjscia', blank=True, null=True)
    godzina_przyjscia = models.TimeField('godzina przyjscia', blank=True, null=True)
    data_wyjscia = models.DateField('data wyjscia')
    godzina_wyjscia = models.TimeField('godzina wyjscia')
    cofnieta = models.BooleanField(default=False)
    czas = models.TimeField('czas trwania')
    czas_w_minutach = models.IntegerField(default=0)

    def __str__(self):
        return self.pracownik()