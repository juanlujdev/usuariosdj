from django import forms

from .models import User


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
