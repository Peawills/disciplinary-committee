from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import StudentOffense

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def offense_list(request):
    offenses = StudentOffense.objects.all()
    return render(request, 'committe/offense_list.html', {'offenses': offenses})




def offense_detail(request, offense_id):
    offense = get_object_or_404(StudentOffense, id=offense_id)
    return render(request, 'commitee/offense_detail.html', {'offense': offense})





def render_pdf_view(request, offense_id):
    offense = get_object_or_404(StudentOffense, id=offense_id)
    template_path = 'records/offense_pdf.html'
    context = {'offense': offense}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="offense_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
