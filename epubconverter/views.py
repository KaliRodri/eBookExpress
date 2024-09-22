from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFUploadForm
import pypandoc 
import os

def convert_pdf_to_epub(pdf_path):
    output_path = pdf_path.replace('.pdf', '.epub')
    pypandoc.convert_file(pdf_path, 'epub', outputfile=output_path)
    return output_path

def pdf_upload_view(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            pdf_path = os.path.join('/tmp', pdf_file.name)
        
        # Salva o arquivo PDF em um diretório temporário
            with open(pdf_path, 'wb') as f:
                for chunk in pdf_file.chunks():
                    f.write(chunk)
        
        # Converte o arquivo PDF para EPUB
        epub_path = convert_pdf_to_epub(pdf_path)
        
        # Prepara o arquivo EPUB para download
        with open(epub_path, 'rb') as epub_file:
            response = HttpResponse(epub_file.read(), content_type='application/epub+zip')
            response['Content-Disposition'] = f'attachment; filename={os.path.basename(epub_path)}'
            return response
        
    else:
        form = PDFUploadForm()
        
    return render(request, 'epubconverter/pdf_upload.html',{'form':form})

        
        

        
