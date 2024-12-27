from django.shortcuts import render
from medical.models import MedicalService, Doctor
from django.templatetags.static import static  # Импортируем тег static
#  from letters.models import Mailing, Customer
#from django.db.models import Count


def get_general_page(request):
    services = MedicalService.objects.all()
    svg_list = [
        'medical/1.png',
        'medical/2.png',
        'medical/3.png',
        'medical/4.png',
        'medical/5.png',
        'medical/6.png',
        'medical/7.png',
        'medical/8.png',
        'medical/9.png',
    ]
    print(svg_list)
    context = {
        'services': services,
        'active_menu': 'home',
        'svg_list': svg_list,
    }
    return render(request, 'medical/general_page.html', context)



def about(request):
    doctors = Doctor.objects.all()

    context = {
        'doctors': doctors,
        'active_menu': 'about',
    }
    return render(request, 'medical/about.html', context)


def contacts(request):

    context = {
        'active_menu': 'contacts',
    }
    return render(request, 'medical/contacts.html', context)

