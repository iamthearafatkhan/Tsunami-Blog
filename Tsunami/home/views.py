from django.shortcuts import render, redirect
from .models import Comment
# Create your views here.

from django.contrib import messages

def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def history(request):
    return render(request, 'history.html')

def real(request):
    return render(request, 'real.html')
    
#def course(request):
   # if request.method == "POST":
       # name = request.POST.get('name')
        # email = request.POST.get('email')
       #  password = request.POST.get('password')
       #  address = request.POST.get('address')
       #  city = request.POST.get('city')
        
       #  course = Course(email=email, password=password, address=address, name=name, city=city, date=datetime.today() )
       #  course.save()
       # 
    # return render(request, 'course.html')

def safety(request):
    return render(request, 'safety.html')

def discussion(request):
    comments = Comment.objects.all()  # Fetch all comments for display
    return render(request, 'discussion.html', {'comments': comments})

def add_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        comment_text = request.POST.get('comment')
        Comment.objects.create(name=name, comment=comment_text)  # Save the comment
        messages.success(request, "Comment added!")
        return redirect('discussion')  # Redirect back to the discussion page
def faq(request):
    return render(request, 'faq.html')

#API View
import openai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

openai.api_key = settings.OPENAI_API_KEY

@csrf_exempt
def faq_chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_question = data.get('question')

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Q: {user_question}\nA:",
                max_tokens=100,
                temperature=0.7
            )
            answer = response.choices[0].text.strip()
        except Exception as e:
            answer = "I'm having trouble answering right now. Please try again later."

        return JsonResponse({'answer': answer})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
