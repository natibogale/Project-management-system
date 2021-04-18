from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager
# Create your models here.
from django.core.validators import RegexValidator, MinValueValidator
from django.urls import reverse
from django.utils.safestring import mark_safe


titles = (
            ('Director','Director'),
            ('Team Leader','Team Leader'),
            ('Office Assistant','Office Assistant'),
            ('Lead Engineer','Lead Engineer'),
            ('Record Officer','Record Officer'),
            ('Project Engineer','Project Engineer'),
            ('Secretary','Secretary'),
            ('HR Officer','HR Officer'),
            )


gender = (
        ('Male','Male'),
        ('Female','Female'),
        )

class Directorates(models.Model):
    directorate = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.directorate}'

    class Meta:
        verbose_name_plural = 'Directorates'



class Teams(models.Model):
    team = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.team}'

    class Meta:
        verbose_name_plural = 'Teams'





class Manager(BaseUserManager):
    def create_user(self, username,email, firstName, middleName, lastName,gender,title,directorate ,team, password=None):
        if not username:
            raise ValueError("Users must have a Badge Number")
        if not firstName:
            raise ValueError("Users must have First Names")
        if not middleName:
            raise ValueError("Users must have Middle Names")
        if not lastName:
            raise ValueError("Users must have Last Names")
        if not gender:
            raise ValueError("Users must have a Gender")
        if not email:
            raise ValueError("Users must have Email")
        # if not directorate:
        #     raise ValueError("Choose the correct Directorate for Users")
        if not title:
            raise ValueError("Users need their job Title or their position ")
        # if not team:
        #     raise ValueError("Choose All for the Director and the teams for other Users.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstName = firstName,
            middleName = middleName,
            lastName = lastName,
            directorate = directorate,
            team = team,
            gender = gender,
            title  =title,
        )

        user.set_password(password)
        user.save(using=self._db)
        # user.directorate.set([directorate])
        # user.team.set([team])
        return user

    def create_superuser(self, username,email, password, gender, directorate = None, team = None):
        user = self.create_user(
            password =password,
            email = self.normalize_email(email),
            username = username,
            firstName = ' ',
            lastName = ' ',
            middleName = ' ',
            title = ' ',
            gender=gender,
            directorate = directorate,
            team = team,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        # user.directorate.set([directorate])
        # user.team.set([team])
        return user






class User(AbstractBaseUser):
    username = models.CharField(max_length=500, verbose_name="Badge Number", unique=True )
    firstName = models.CharField(max_length=500, verbose_name="First Name", blank=True)
    middleName = models.CharField(max_length=500, verbose_name="Middel Name", blank=True)
    lastName = models.CharField(max_length=500, verbose_name="Last Name", blank=True)
    gender =  models.CharField(choices=gender,   max_length=100, verbose_name="Gender", blank=True, default='Male')
    email = models.CharField(max_length=500, verbose_name="Email", unique=True)
    phoneValidator = RegexValidator(regex=r'^\+?1?\d{10,15}$',message='Please enter your phonenumber in the format starting with: 09 or +251',)
    phoneNumber = models.CharField(validators=[phoneValidator], max_length=15, blank=True, verbose_name="Phone Number")
    directorate = models.ForeignKey(Directorates, on_delete=models.CASCADE,max_length=500, default=1, verbose_name="Directorate", blank=True, null=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE,  max_length=500, default=1, verbose_name="Team", blank=True, null=True)
    title = models.CharField(choices=titles,   max_length=100, verbose_name="Title", blank=True)
    emergencyContactName = models.CharField(max_length=500, verbose_name="Emergency Contact Name", blank=True)
    emergencyContactPhone = models.CharField(validators=[phoneValidator], max_length=15, blank=True, verbose_name="Emergency Contact Phone")
    profilePicture = models.ImageField(upload_to='Profile_Pictures/', default='Profile_Pictures/default.png', verbose_name="Profile Picture")
    # registeredBy = models.CharField(max_length= 400, default='Admin', blank=True ,verbose_name="Registered By")

    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="last login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS= ['email',]

    objects = Manager()

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.profilePicture.url))
    admin_photo.short_description = 'Profile Picture'
    admin_photo.allow_tags = True


    # def get_absolute_url(self):
    #     return reverse('ro-profile', kwargs={'pk' : self.pk})


    # def save(self, *args, **kwargs):
    #     try:
    #         self.directorate
    #     except:
    #         self.directorate = Directorates.objects.first()
    #     super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     try:
    #         self.team
    #     except:
    #         self.team = Teams.objects.first()
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
