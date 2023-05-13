from django.db import models

class Osoba(models.Model):
    jmeno = models.CharField(max_length=45, verbose_name="Jméno", help_text="Zadejte jméno osoby")
    prijmeni = models.CharField(max_length=45, verbose_name="Přijmení", help_text="Zadejte příjmení")
    reputace = models.CharField(max_length=10, verbose_name="Reputatace", help_text="Zadejte reputaci")

    class Meta:
        verbose_name = 'Osoba'
        verbose_name_plural = 'Osoby'
        ordering = ['reputace']

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'

class Majitel(models.Model):
    osoba = models.ForeignKey('Osoba', on_delete=models.CASCADE, verbose_name='Majitel', help_text='Vyberte majitele', default=0)

    class Meta:
        verbose_name = 'Majitel'
        verbose_name_plural = 'Majitelé'
        ordering = ['osoba']

        def __str__(self):
            return self.osoba

class Najemnik(models.Model):
    osoba = models.ForeignKey('Osoba', on_delete=models.CASCADE, verbose_name='Najemnik', help_text='Vyberte najemnika', default=0)

    class Meta:
        verbose_name = 'Najemnik'
        verbose_name_plural = 'Najemníci'
        ordering = ['osoba']

        def __str__(self):
            return self.osoba

class Nemovitost(models.Model):
    majitel = models.ForeignKey('Majitel', on_delete=models.CASCADE, verbose_name='Osoba', help_text='Vyberte majitele', default=0)
    mesto = models.CharField(max_length=45, verbose_name="Město", help_text="Zadejte jméno města")
    ulice = models.CharField(max_length=45, verbose_name="Ulice", help_text="Zadejte jméno ulice")
    cena = models.PositiveIntegerField(verbose_name="Cena", help_text="Zadejte cenu")
    fotka = models.ImageField(upload_to="nemovitost", verbose_name="Fotka nemovitosti", help_text="Nahrejte fotku nemovitosti")

    class Meta:
        verbose_name = 'Nemovitost'
        verbose_name_plural = 'Nemovitosti'
        ordering = ['majitel']

        def __str__(self):
            return f'{self.majitel}, {self.mesto}, {self.ulice}'

class Najem(models.Model):
    nemovitost = models.ForeignKey('Nemovitost', on_delete=models.CASCADE, verbose_name='Nemovitost', help_text='Vyberte nemovitost', default=0)
    najemnik = models.ForeignKey('Najemnik', on_delete=models.CASCADE, verbose_name='Nájemník', help_text='Vyberte nájemníka', default=0)
    vyse_najmu = models.PositiveIntegerField(verbose_name="Výše nájmu", help_text="Zadejte výši nájmu")
    datum_splatnosti = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Datum splatnosti', help_text='Zadejte datum splatnosti')

    class Meta:
        verbose_name = 'Nájem'
        verbose_name_plural = 'Nájmy'
        ordering = ['nemovitost']

        def __str__(self):
            return self.vyse_najmu