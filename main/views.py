from django.shortcuts import render
from django.core.mail import send_mail
from .forms import DemoFormForm

def home_view(request):
    return render(request, 'home.html')

# View for About Us Page
def about_us_view(request):
    return render(request, 'about_us.html')

# View for Courses Page
def courses_view(request):
    return render(request, 'courses.html')

# View for Form Page
def form_view(request):
    form = DemoFormForm() 
    if request.method == "POST":
        form = DemoFormForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form.html', {'form': form, 'success': True})
    return render(request, 'form.html', {'form': form})


def demo_form_view(request):
    if request.method == 'POST':
        form = DemoFormForm(request.POST)
        if form.is_valid():
            # Save to database
            form.save()

            # Send email
            send_mail(
                'New Demo Form Submission',
                f"Name: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n"
                f"Phone: {form.cleaned_data['phone']}\n"
                f"Message: {form.cleaned_data['message']}",
                'jollyvinayak67@gmail.com',  # Replace with your email
                ['vjolly7@gmail.com'],  # Replace with recipient email(s)
                fail_silently=False,
            )

            return render(request, 'thank_you.html')  # Thank-you page
    else:
        form = DemoFormForm()

    return render(request, 'form.html', {'form': form})

# Create your views here.
