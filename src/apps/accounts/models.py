from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.core import validators
from django.utils import timezone
from django.utils.translation import gettext as _


# create user in admin and create superuser in manage.py
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email,
                                password=password,
                                username=username)
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=_('username'), max_length=255, unique=True,
                                help_text=u'Обязательное поле. Не более 30 символов. '
                                          u'Только буквы, цифры и символы @/./+/-/_.',
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$',
                                      ('Enter a valid username. This value may contain only letters, numbers '
                                       'and @/./+/-/_ characters.'), 'invalid'),],
                                error_messages={'unique': _("A user with that username already exists."),}
                                )
    first_name = models.CharField(verbose_name=_('first name'), max_length=30)
    last_name = models.CharField(verbose_name=_('last name'), max_length=30)
    middle_name = models.CharField(verbose_name=_('middle name'),  max_length=255)
    email = models.EmailField(verbose_name=_('E-mail'), max_length=255, blank=True, null=True, unique=True)
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=255, blank=True)
    is_staff = models.BooleanField(verbose_name=_('user status'), default=False,
                                   help_text=_(u"Отметьте, если пользователь может входить"
                                               u" в административную часть сайта."))
    is_active = models.BooleanField(u'Активный', default=False,
                                    help_text=_(u'Отметьте, если пользователь должен считаться активным.'
                                                u' Уберите эту отметку вместо удаления учётной записи.'))
    registration_date = models.DateTimeField(verbose_name=_('registration date'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        who_i_am = (self.last_name, self.first_name, self.middle_name)
        if all(who_i_am):
            return ' '.join(who_i_am)
        return ''

    @staticmethod
    def get_first_letter_in_string(name, dot=None):
        """ Возвращает первую букву строки если она не пустая

        :param unicode str name: принимаемое значение не пустой строки
        :param bool dot: нужна ли точка в конце ? (для инициалов, в них весь сыр-бор)
        """
        letter = ''
        if name:
            letter = next(iter(name))
            if dot and letter:
                letter = letter + '.'
        return letter

    def get_short_last_name(self):
        """ Получение Фимилии И.О. - с инициалами, если они есть """
        return '%s %s%s' % (
            self.last_name,
            self.get_first_letter_in_string(self.first_name, dot=True),
            self.get_first_letter_in_string(self.middle_name, dot=True)
        )

    def get_initial(self):
        return '%s%s' % (
            self.get_first_letter_in_string(self.last_name),
            self.get_first_letter_in_string(self.first_name)
        )

    def get_short_name(self):
        return '%s %s' % (self.last_name, self.first_name)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = u'Пользователя'
        verbose_name_plural = u'Пользователи'
