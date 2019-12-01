from django import forms
from django.core.exceptions import ValidationError


def validate_cpf_by_digit(cpf: str, rng: range, validator_digit: str):
    """
    Should be called as:

    if (not validate_cpf_by_digit(value, range(10, 1, -1), value[-2]) or
            not validate_cpf_by_digit(value, range(11, 1, -1), value[-1])):
        raise ValidationError('CPF tem formato inválido.')
    """
    return str((sum(int(t[0]) * t[1] for t in zip(cpf, rng)) * 10) % 11) == validator_digit


def validate_cpf(value: str):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')
    if value == len(value) * value[0]:
        raise ValidationError('CPF não deve conter todos os números iguais.', 'repeated')


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if (not self.cleaned_data.get('email') and
                not self.cleaned_data.get('phone')):
            raise ValidationError("Informe seu e-mail ou telefone")
        return self.cleaned_data
