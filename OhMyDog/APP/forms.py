from .models import *
from django import forms

from django.core.exceptions import ValidationError 

# Aca creamos los formularios

class Perro_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Perro
        fields = ['nombre','raza', 'edad', 'emailDueño']
    # Creamos los campos del formulario
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')
    emailDueño = forms.EmailField(max_length=30, required=True, label='Email Dueño')

    # Clean son validaciones 
    # Se debe respetar que en el nombre de la validacion este
    # el nombre del campo , osea clean_<nombre de campo>
    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data
    
    def clean_emailDueño(self):
        data = self.cleaned_data.get('emailDueño')
        ok = Cliente.objects.filter(mail=data).exists()
        if not ok :
            raise ValidationError('El email no pertenece a un dueño')
        return data
    
class Paseador_form(forms.ModelForm):
    class Meta:
        model=Paseador
        fields=['nombre', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7 or len(str(data)) > 11:
            raise ValidationError("Telefono invalido")
        ok = Paseador.objects.filter(telefono=data).first()
        if ok is not None:
            raise ValidationError("Telefono ya registrado")
        return data
    
class Cuidador_form(forms.ModelForm):
    class Meta:
        model=Cuidador
        fields=['nombre', 'telefono', 'zona', 'disponibilidad']
    nombre = forms.CharField(max_length=50, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True, label='Telefono')
    zona = forms.CharField(max_length=20, required=True, label='Zona')
    disponibilidad = forms.CharField(max_length=30, required=True, label='Disponibilidad')
    
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7 or len(str(data)) > 11:
            raise ValidationError("El telefono debe tener entre 7 y 11 caracters")
        ok = Cuidador.objects.filter(telefono=data).first()
        if ok is not None:
            raise ValidationError("Telefono ya registrado")
        return data
    
class Turnos_form(forms.ModelForm):
    # Meta sirve para enlazar con la BD
    class Meta:
        model = Turnos
        fields = ['descripcion','raza', 'edad','nombre','fecha']
    # Creamos los campos del formulario
    descripcion = forms.Textarea()
    nombre = forms.CharField(max_length=15, required=True, label='Nombre')
    raza = forms.CharField(max_length=15, required=True, label='Raza')
    edad = forms.IntegerField(required=True, label='Edad')
    motivo = forms.Select()
    fecha = forms.DateField(required = True, label='Seleccione la fecha de su turno',
                            widget=forms.DateInput(attrs={"type": "date"}))
    # Clean son validaciones 
    def clean_edad(self):
        data = self.cleaned_data["edad"]
        if data < 1 or data > 20:
            raise ValidationError("Edad invalida")
        return data
    
class perroAdopcion_form(forms.ModelForm):
    class Meta:
        model= PerroAdopcion
        fields=['usuario','nombre', 'peso', 'raza', 'descripcion', 'zona', 'castrado']

    usuario= forms.CharField(max_length=30, required=True, label='usuario')
    nombre = forms.CharField(max_length=50, required=True, label='nombre')
    peso = forms.IntegerField(required=True, label='peso')
    #edad = forms.IntegerField(required=True, label='edad')
    zona = forms.CharField(max_length=50, required=True, label='zona')
    raza= forms.CharField(max_length=20, required=True, label='raza')
    descripcion= forms.CharField(max_length=30, required=True, label='description')
    castrado= forms.CharField(max_length=2,required=True, label='castrado')

    def clean_usuario(self):
        data = self.cleaned_data["usuario"]
        ok = Cliente.objects.filter(usuario=data).exists()
        if ok==False:
            raise ValidationError('no pertenece a ningun usuario')
        return data
    
class Cliente_form(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombreC','usuario','contra','mail','telefono']
    nombreC = forms.CharField(max_length=40, required=True, label='Nombre Completo')
    usuario = forms.CharField(max_length=20, required=True, label='Nombre de Usuario')
    contra = forms.CharField(max_length=20, required=True, label='Contraseña',widget=forms.PasswordInput)
    mail = forms.EmailField(max_length=30, required=True, label='Mail')
    telefono = forms.IntegerField(required=True, label='Telefono')
    
    def clean_usuario(self):
        data = self.cleaned_data["usuario"]
        ok = Cliente.objects.filter(usuario=data).exists()
        if ok==True:
            raise ValidationError('Usuario Ya Registrado')
        return data
    
    def clean_telefono(self):
        data = self.cleaned_data["telefono"]
        ok = Cliente.objects.filter(telefono=data).exists()
        if ok==True:
            raise ValidationError('Telefono Ya Registrado')
        return data
    
    def clean_mail(self):
        data = self.cleaned_data["mail"]
        ok = Cliente.objects.filter(mail=data).exists()
        if ok==True:
            raise ValidationError('Mail Ya Registrado')
        return data

    
class LogIn_form(forms.Form):
    usuario = forms.CharField(max_length=30, required=True, label='Nombre de Usuario')
    contra = forms.CharField(max_length=30, required=True, label='Contraseña',widget=forms.PasswordInput)
    
    def clean_usuario(self):
        usuario = self.cleaned_data['usuario']
        user = Cliente.objects.filter(usuario=usuario).first()
        if user is None:
            raise ValidationError('Nombre de usuario incorrecto')
        return usuario
    
    def clean_contra(self):
        password = self.cleaned_data['contra']
        username = self.cleaned_data.get('usuario')
        if username:
            user = Cliente.objects.filter(usuario=username).first()
            if user is not None and not user.contra==password:
                raise forms.ValidationError('Contraseña incorrecta')
        return password
    
class contacto_form(forms.Form):
    usuario = forms.CharField(max_length=40, required=True, label='Nombre')
    telefono = forms.IntegerField(required=True)
            
    def clean_telefono(self):
        data=self.cleaned_data["telefono"]
        if len(str(data)) < 7 or len(str(data)) > 11:
            raise ValidationError("El telefono debe tener entre 7 y 11 caracters")
        return data
    