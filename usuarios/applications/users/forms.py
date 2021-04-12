from django import forms

from .models import User

from django.contrib.auth import authenticate


class UserRegisterForm(forms.ModelForm):  # forms.ModelForm cuando queremos que dependa de un modelo
    password1 = forms.CharField(
        label='Contaseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    password2 = forms.CharField(
        label='Contaseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        # fields=('__all__') asi llamamos todos los campos
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )

    # funcion para validar que un campo cumpla ciertos parametros, siempre se llama clea_"nombre de campo a validar"
    # nunca guardara un formulario si no esta ok todos los formularios
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'El password no coincide')


class LoginForm(forms.Form):  # se utiliza asi cuando no queremos depender de un modelo
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'username',
                'style': '{margin:10px}',
            }
        )
    )

    password = forms.CharField(
        label='Contaseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    # Validacion si un usuario existe o no existe o si el usuario es correcto. Como no sabemos a quien hacerle la
    # validacion y realmente la tiene que hacer en los dos campos se utiliza la funcion clean(self)  a solas

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()  # devuelveme to_dos los datos, .clean xq estamos
        # sobreescribiendo un metodo
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password=password):  # si no coinciden
            raise forms.ValidationError('Los datos de usuario no son correctos')  # Para que corte to_do el proceso
            # si no es correcto y manda el mensaje de error
        return self.cleaned_data


class UpdatePasswordView(forms.Form):  # no va a depender exclusivo de un modelo, poreso traemos forms.Form.
    password1 = forms.CharField(
        label='Contaseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contaseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )


class VerificationForm(forms.Form):
    codregistro = forms.CharField(required=True)

    #La funcion init es la funcion que se ejecuta en el momento en el q se esta inicializando el formulario
    def __init__(self, pk, *args, **kwargs):
        self.id_user=pk
        super(VerificationForm, self).__init__(*args,**kwargs)

    # Hacemos la verificacion del codigo que recibimos en nuestro mail
    def clean_codregistro(self):
        codigo = self.cleaned_data['codregistro']

        if len(codigo) == 6:
            # Verificamos si el codigo y el id del usuario son validos
            activo = User.objects.cod_validation(
                self.id_user, #Accedo al id de usuario
                codigo
            )
            if not activo:
                raise forms.ValidationError('el codigo no es correctos')

        else:
            raise forms.ValidationError('el codigo no es correctos')
