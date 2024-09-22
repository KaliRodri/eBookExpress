from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(lavel='Selecione um arquivo PDF para converter')