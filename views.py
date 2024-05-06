import os
import cv2
import csv
from PIL import Image
import pandas as pd
import datetime
import time
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect,render,redirect
from django.http import HttpResponse
import numpy as np
import random
import google.generativeai as genai
from django.db import connection
import cv2
import numpy as np
import random
import time
import re
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection

logo="{% static '/images/logo.png' %}"
boy_names = [
    "Liam", "Noah", "William", "James", "Oliver", 
    "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
    "Alexander", "Ethan", "Jacob", "Michael", "Daniel",
    "Henry", "Jackson", "Sebastian", "Aiden", "Matthew"
]

girl_names = [
    "Emma", "Olivia", "Ava", "Isabella", "Sophia", 
    "Charlotte", "Mia", "Amelia", "Harper", "Evelyn",
    "Abigail", "Emily", "Elizabeth", "Mila", "Ella",
    "Avery", "Sofia", "Camila", "Aria", "Scarlett"
]
n1=random.choice(boy_names)
n2=random.choice(girl_names)
n3=random.choice(boy_names)
f1='https://images.ctfassets.net/vztl6s0hp3ro/5l6tXP6NaoWULOqFDWoydh/34e9bb2cf490feeeff1439864c7995e3/7-types-of-employee-testimonials.jpg?fm=webp'
f2='https://cdn2.hubspot.net/hubfs/53/Customer-testimonial-page.jpg'
f3='https://image1.masterfile.com/getImage/NjQ5LTA3MjM4ODk3ZW4uMDAwMDAwMDA=AK-o9l/649-07238897en_Masterfile.jpg'
abc=0
data={}
brand_name=''
def api(msg):
        genai.configure(api_key="AIzaSyC-W-N66pCz04ysDN6EoNpfislOD0vaHsM")
        
        generation_config={"temperature":0.9,"top_p":1,"top_k":1,"max_output_tokens":2048}

        model=genai.GenerativeModel("gemini-pro",generation_config=generation_config)
        response=model.generate_content([msg])

        return response

def footer(request):
 global abc,h_head,h_sub,a_content,test1,test2,test3,data,brand_name,description,business_type,location
 brand_name = request.GET.get('brand_name')
 description = request.GET.get('description')
 business_type=request.GET.get('business_type')
 location = request.GET.get('location')

        # Store values in session
 request.session['brand_name'] = brand_name
 request.session['description'] = description
 request.session['business_type'] = business_type
 request.session['location'] = location
 global n1,n2,n3,logo,f1,f2,f3
  
 if brand_name:
    print(brand_name)
    print(description)
    print(business_type)
    print( location)
    n1=random.choice(boy_names)
    n2=random.choice(girl_names)
    n3=random.choice(boy_names)
    r =random.randint(1,15)
    
    print(r)

    logo='logo1'
    data = {
        'brand_name':brand_name,
        'n1':n1,
        'n2':n2,
        'n3':n3,
        'logo':"{% static '/images/logo.png' %}",
        'f1':'https://images.ctfassets.net/vztl6s0hp3ro/5l6tXP6NaoWULOqFDWoydh/34e9bb2cf490feeeff1439864c7995e3/7-types-of-employee-testimonials.jpg?fm=webp',
        'f2':'https://cdn2.hubspot.net/hubfs/53/Customer-testimonial-page.jpg',
        'f3':'https://image1.masterfile.com/getImage/NjQ5LTA3MjM4ODk3ZW4uMDAwMDAwMDA=AK-o9l/649-07238897en_Masterfile.jpg'
    }
    
    if(abc==1):
        dbnav(request)
        dbhome(request)
        dbcontact(request)
        dbtest(request)
        dbabt(request)
        abc=0
    if(abc==1):
      return render(request, 'n.html', data)
    return render(request, 'n.html', data)
 else:
    
     return render(request, 'n.html',data)
 

def homecontent(request):
    global data,brand_name,description,business_type,location
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    h_head=api(f"Generate a compelling title for our home page using the following variables:Brand Name: {brand_name} Description: {description}Business Type: {business_type}We're looking for a title that captures the essence of our brand, describes our business type, and highlights our unique style and location.")
    h_sub=api(f"Generate a compelling subtitle for our home page using the following variables:Brand Name: {brand_name} Description: {description}Business Type: {business_type}We're looking for a title that captures the essence of our brand, describes our business type, and highlights our unique style and location.")
    request.session['h_head'] = h_head.text
    request.session['h_sub'] = h_sub.text
    
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head.text,
        'h_sub': h_sub.text,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img3': img3,
        'img4':img4,})

def aboutcontent(request):
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    a_content=api(f"Craft engaging paragraph without subheadings content for our 'About Us' page using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We aim to create a captivating narrative that introduces visitors to our brand, highlights our unique style, showcases our business type")
    request.session['a_content'] = a_content.text
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content.text,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'img4':img4,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'img2': img2,
        'img3': img3,})

def testcontent(request):
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    
    test1=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    test2=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    test3=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    request.session['test1'] = test1.text
    request.session['test2'] = test2.text
    request.session['test3'] = test3.text
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1.text,
        'test2': test2.text,
        'test3': test3.text,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img4':img4,
        'img2': img2,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'img3': img3,})

def contentapi(brand_name,description,business_type,location,request):
    global h_head,h_sub,a_content,test1,test2,test3
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    h_head=api(f"Generate a compelling title for our home page using the following variables:Brand Name: {brand_name} Description: {description}Business Type: {business_type}We're looking for a title that captures the essence of our brand, describes our business type, and highlights our unique style and location.")
    h_sub=api(f"Generate a compelling subtitle for our home page using the following variables:Brand Name: {brand_name} Description: {description}Business Type: {business_type}We're looking for a title that captures the essence of our brand, describes our business type, and highlights our unique style and location.")
    a_content=api(f"Craft engaging paragraph without subheadings content for our 'About Us' page using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We aim to create a captivating narrative that introduces visitors to our brand, highlights our unique style, showcases our business type")
    test1=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    test2=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    test3=api(f"Generate 1 positive testimonials (each under 15 words) using the following variables:Brand Name: {brand_name}Description: {description}Business Type: {business_type}Location: {location}We're looking for short, impactful testimonials that reflect the satisfaction of our customers, emphasizing our brand, style, business type, and location.")
    context={
        'h_head': h_head.text,
        'h_sub': h_sub.text,
        'a_content':a_content.text,
        'test1':test1.text,
        'test2':test2.text,
        'test3':test3.text,
    }
    return context


    
def signup(request):
    if request.user.is_authenticated:
        return redirect('/signin')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
   
def home(request): 
    return render(request, 'home.html')


def profile(request): 
    return render(request, 'profile.html')

def output(request): 
    return render(request, 'output.html')
   
def form(request): 
    global abc
    if request.method == 'POST':
        abc=1
        brand_name = request.POST.get('brand_name', '')
        description = request.POST.get('description', '')
        return render(request, 'footer.html',abc)
    else:
        abc=1
        return render(request, 'form.html')
    

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #TrackImages()
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})
    
def signout(request):
    logout(request)
    return redirect('/profile')

def dbnav(request):
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    global data
    r =random.randint(1,5)
    print("random:",r)
    with connection.cursor() as cursor:
      cursor.execute("SELECT code FROM navbar1")
      for _ in range(r):
        html_code = cursor.fetchone()
    html_code=html_code[0]
    with open(r"myapp\templates\navbar.html", "w") as file:
      file.write(html_code)
    with open('myapp\\templates\\navbar.html', 'r') as template_file:
        template_content = template_file.read()
    with open('myapp\\templates\\navbar.html', 'w') as output_file:
        output_file.write(template_content)
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img4':img4,
        'img2': img2,
        'img3': img3,})

def dbhome(request):
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    global data
    r =random.randint(1,4)
    print("random:",r)
    with connection.cursor() as cursor:
      cursor.execute("SELECT code FROM home")
      for _ in range(r):
        html_code = cursor.fetchone()
    html_code=html_code[0]
    with open(r"myapp\templates\home.html", "w") as file:
      file.write(html_code)
    with open('myapp\\templates\\home.html', 'r') as template_file:
        template_content = template_file.read()
    with open('myapp\\templates\\home.html', 'w') as output_file:
        output_file.write(template_content)
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img4':img4,
        'img3': img3,})

def dbcontact(request):
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    
    global data
    r =random.randint(1,3)
    print("random:",r)
    with connection.cursor() as cursor:
      cursor.execute("SELECT code FROM contact")
      for _ in range(r):
        html_code = cursor.fetchone()
    html_code=html_code[0]
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    with open(r"myapp\templates\contact.html", "w") as file:
      file.write(html_code)
    with open('myapp\\templates\\contact.html', 'r') as template_file:
        template_content = template_file.read()
    with open('myapp\\templates\\contact.html', 'w') as output_file:
        output_file.write(template_content)
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img4':img4,
        'img1': img1,
        'img2': img2,
        'img3': img3,})

def dbtest(request):
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    global data
    r =random.randint(1,4)
    print("random:",r)
    with connection.cursor() as cursor:
      cursor.execute("SELECT code FROM test")
      for _ in range(r):
        html_code = cursor.fetchone()
    html_code=html_code[0]
    with open(r"myapp\templates\testimonals.html", "w") as file:
      file.write(html_code)
    with open('myapp\\templates\\testimonals.html', 'r') as template_file:
        template_content = template_file.read()
    #for key, value in data.items():
    #  placeholder = '{{' + key + '}}'
    #  template_content = template_content.replace(placeholder, value)
    with open('myapp\\templates\\testimonals.html', 'w') as output_file:
        output_file.write(template_content)
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img4':img4,
        'img1': img1,
        'img2': img2,
        'img3': img3,})

def dbabt(request):
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    global data
    r =random.randint(1,4)
    print("random:",r)
    with connection.cursor() as cursor:
      cursor.execute("SELECT code FROM about")
      for _ in range(r):
        html_code = cursor.fetchone()
    html_code=html_code[0]
    logo="D:\Final-Project\myproject\logo.png"
    with open(r"myapp\templates\about.html", "w") as file:
      file.write(html_code)
    with open('myapp\\templates\\about.html', 'r') as template_file:
        template_content = template_file.read()
    with open('myapp\\templates\\about.html', 'w') as output_file:
        output_file.write(template_content)
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
         'f1': f1,
    'f2': f2,
    'f3': f3,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'logo':'D:\Final-Project\myproject\logo.png',
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img3': img3,
        'img4':img4,})


def img(request):
    global imglist,n1,n2,n3,f1,f2,f3
    business_type = request.session.get('business_type')
    with connection.cursor() as cursor:
        if business_type == 'restaurant':
            cursor.execute("SELECT restaurant FROM imgs;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            img1 = fetch_random_image(cursor, 1, 15)
            img2 = fetch_random_image(cursor, 1, 15)
            img3 = fetch_random_image(cursor, 1, 15)
            img4 = fetch_random_image(cursor, 1, 15)
        elif business_type == 'bakery':
            cursor.execute("SELECT bakery FROM imgs;")
            r = random.randint(16, 25)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            
            img1 = fetch_random_image(cursor, 16, 25)
            img2 = fetch_random_image(cursor, 16, 25)
            img3 = fetch_random_image(cursor, 16, 25)
            img4 = fetch_random_image(cursor, 16, 25)
        elif business_type == 'clothing':
            cursor.execute("SELECT url FROM clothing;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            img1 = fetch_random_image(cursor, 1, 13)
            img2 = fetch_random_image(cursor, 1, 13)
            img3 = fetch_random_image(cursor, 1, 13)
            img4 = fetch_random_image(cursor, 1, 13)
        elif business_type == 'beauty':
            cursor.execute("SELECT url FROM beauty;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            
            img1 = fetch_random_image(cursor, 1, 13)
            img2 = fetch_random_image(cursor, 1, 13)
            img3 = fetch_random_image(cursor, 1, 13)
            img4 = fetch_random_image(cursor, 1, 13)
        elif business_type == 'cafe':
            cursor.execute("SELECT url FROM cafe;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            #img1 = fetch_random_image(cursor, 1, 10)
            img2 = fetch_random_image(cursor, 1, 10)
            img3 = fetch_random_image(cursor, 1, 10)
            img4 = fetch_random_image(cursor, 1, 10)
        elif business_type == 'mechanical_shop':
            cursor.execute("SELECT url FROM mech;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
   
            img1 = fetch_random_image(cursor, 1, 13)
            img2 = fetch_random_image(cursor, 1, 13)
            img3 = fetch_random_image(cursor, 1, 13)
            img4 = fetch_random_image(cursor, 1, 13)
        elif business_type == 'marketing_company':
            cursor.execute("SELECT url FROM market;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            
            img1 = fetch_random_image(cursor, 1, 10)
            img2 = fetch_random_image(cursor, 1, 10)
            img3 = fetch_random_image(cursor, 1, 10)
            img4 = fetch_random_image(cursor, 1, 10)
        elif business_type == 'photography':
            cursor.execute("SELECT url FROM photo;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            img1 = fetch_random_image(cursor, 1, 13)
            img2 = fetch_random_image(cursor, 1, 13)
            img3 = fetch_random_image(cursor, 1, 13)
            img4 = fetch_random_image(cursor, 1, 13)
        elif business_type == 'car_sales':
            cursor.execute("SELECT url FROM car;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            
            img1 = fetch_random_image(cursor, 1, 10)
            img2 = fetch_random_image(cursor, 1, 10)
            img3 = fetch_random_image(cursor, 1, 10)
            img4 = fetch_random_image(cursor, 1, 10)
        elif business_type == 'Gym & Fitness':
            cursor.execute("SELECT url FROM gym;")
            r = random.randint(1, 10)
            for _ in range(r):
              img = cursor.fetchone()
            img1 = img[0]
            img1 = fetch_random_image(cursor, 1, 10)
            img2 = fetch_random_image(cursor, 1, 10)
            img4 = fetch_random_image(cursor, 1, 10)
            img3 = fetch_random_image(cursor, 1, 10)
        else:
            cursor.execute("SELECT url FROM imgs;")
            img1 = fetch_random_image(cursor, 1, 15)
            img2 = fetch_random_image(cursor, 1, 15)
            img3 = fetch_random_image(cursor, 1, 15)
            img4 = fetch_random_image(cursor, 1, 15)
    
    request.session['img1'] = img1
    request.session['img2'] = img2
    request.session['img3'] = img3
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    location = request.session.get('location')
    return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img4':img4,
        'img3': img3,
         'f1': f1,
    'f2': f2,
    'f3': f3,
    })

def fetch_random_image(cursor, min_val, max_val):
    r = random.randint(min_val, max_val)
    for _ in range(r):
        img = cursor.fetchone()
        if img:
            image_url = img[0]
            return image_url
    return None



from django.shortcuts import render

def pallete(request):
    return render(request, 'pallete.html')

def n(request):
    return render(request, 'n.html')

def next_page(request):
    if request.method == 'POST':
        color1 = request.POST.get('color1')
        color2 = request.POST.get('color2')
        request.session['color1'] = color1
        request.session['color2'] = color2
        img1 = request.session.get('img1')
        img2 = request.session.get('img2')
        img3 = request.session.get('img3')
        brand_name = request.session.get('brand_name')
        description = request.session.get('description')
        business_type = request.session.get('business_type')
        h_head = request.session.get('h_head')
        h_sub = request.session.get('h_sub')
        a_content = request.session.get('a_content')
        test1 = request.session.get('test1')
        test2 = request.session.get('test2')
        test3 = request.session.get('test3')
        location = request.session.get('location')
        img4 = request.session.get('img4')
        
        return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'img4':img4,
         'f1': f1,
         'f2': f2,
    'f3': f3,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img3': img3,})
    

def logogen(request):
        global brand_name,logo
        img1 = request.session.get('img1')
        img2 = request.session.get('img2')
        img3 = request.session.get('img3')
        brand_name = request.session.get('brand_name')
        description = request.session.get('description')
        business_type = request.session.get('business_type')
        h_head = request.session.get('h_head')
        h_sub = request.session.get('h_sub')
        a_content = request.session.get('a_content')
        test1 = request.session.get('test1')
        test2 = request.session.get('test2')
        test3 = request.session.get('test3')
        location = request.session.get('location')
        color1 = request.session.get('color1')
        color2 = request.session.get('color2')
        img4 = request.session.get('img4')
        draw_shape_with_letter(brand_name)
        return render(request, 'n.html', {        
        'brand_name': brand_name,
        'description': description,
        'business_type': business_type,
        'location': location,
        'h_head': h_head,
        'h_sub': h_sub,
        'a_content': a_content,
        'test1': test1,
        'test2': test2,
        'test3': test3,
        'logo':logo,
        'img4':img4,
        'bg1_color': color1,
        'bg2_color': color2,
        'img1': img1,
        'img2': img2,
        'img3': img3,
        'f1': f1,
    'f2': f2,
    'f3': f3,})

def draw_shape_with_letter(letter):
    height, width = 400, 400
    image = np.ones((height, width, 3), dtype=np.uint8) * 255
    shape = random.choice(['circle', 'square'])
    color1, color2 = generate_random_gradient_color()

    if shape == 'circle':
        draw_gradient_circle(image, color1, color2)
    elif shape == 'square':
        draw_gradient_square(image, color1, color2)

    text_color = random.choice([(255, 255, 255), (0, 0, 0)])  

    font = random.choice([
        cv2.FONT_HERSHEY_SIMPLEX, 
        cv2.FONT_HERSHEY_PLAIN, 
        cv2.FONT_HERSHEY_DUPLEX,
        cv2.FONT_HERSHEY_COMPLEX,
        cv2.FONT_HERSHEY_TRIPLEX,
        cv2.FONT_HERSHEY_COMPLEX_SMALL,
        cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    ])

    text_size = cv2.getTextSize(letter[0], font, 5, 2)[0]
    text_x = int((width - text_size[0]) / 2)
    text_y = int((height + text_size[1]) / 2)
    cv2.putText(image, letter[0], (text_x, text_y), font, 5, text_color, 2, cv2.LINE_AA)
    filename ='D:\Final-Project\myproject\myapp\static\images\logo.png'
    cv2.imwrite(filename, image)

def generate_random_gradient_color():
    color1 = tuple(np.random.randint(0, 256, 3))
    color2 = tuple(np.random.randint(0, 256, 3))
    return color1, color2

def draw_gradient_circle(image, color1, color2):
    center = (200, 200)
    radius = 100
    for i in range(20):
        ratio = i / 20
        color = blend_colors(color1, color2, ratio)
        cv2.circle(image, center, radius - i * 4, color, -1)

def draw_gradient_square(image, color1, color2):
    top_left = (100, 100)
    bottom_right = (300, 300)
    for i in range(20):
        ratio = i / 20
        color = blend_colors(color1, color2, ratio)
        cv2.rectangle(image, top_left, bottom_right, color, -1)

def blend_colors(color1, color2, ratio):
    blended_color = tuple(int(round(c1 * (1 - ratio) + c2 * ratio)) for c1, c2 in zip(color1, color2))
    return blended_color



    

def save(request):
    global n1,n2,n3,logo,f1,f2,f3
    h_head = request.session.get('h_head')
    h_sub = request.session.get('h_sub')
    a_content = request.session.get('a_content')
    test1 = request.session.get('test1')
    test2 = request.session.get('test2')
    test3 = request.session.get('test3')
    brand_name = request.session.get('brand_name')
    description = request.session.get('description')
    business_type = request.session.get('business_type')
    location = request.session.get('location')
    color1 = request.session.get('color1')
    color2 = request.session.get('color2')
    img1 = request.session.get('img1')
    img2 = request.session.get('img2')
    img3 = request.session.get('img3')
    img4 = request.session.get('img4')
    data1 = {
    '{{brand_name}}': brand_name,
    '{{description}}': description,
    '{{business_type}}': business_type,
    '{{location}}': location,
    '{{h_head}}': h_head,
    '{{h_sub}}': h_sub,
    '{{a_content}}': a_content,
    '{{test1}}': test1,
    '{{test2}}': test2,
    '{{test3}}': test3,
    '{{bg1_color}}': color1,
    '{{bg2_color}}': color2,
    '{{img1}}': img1,
    '{{img2}}': img2,
    '{{img3}}': img3,
    '{{img4}}': img4,
    '{{n1}}': n1,
    '{{n2}}': n2,
    '{{n3}}': n3,
    '{{logo}}': logo,
    '{{f1}}': f1,
    '{{f2}}': f2,
    '{{f3}}': f3,
    }

    with open('myapp\\templates\\navbar.html', 'r') as template_file:
        nav_content = template_file.read()

    for key, value in data1.items():
        print(key)
        print(value)
        nav_content = nav_content.replace(key,str(value))
    
    with open('myapp\\templates\\home.html', 'r') as template_file:
        home_content = template_file.read()
    
    for key, value in data1.items():
        home_content = home_content.replace(key,str(value))
    
    with open('myapp\\templates\\about.html', 'r') as template_file:
        abt_content = template_file.read()

    for key, value in data1.items():
        abt_content = abt_content.replace(key,str(value))

    with open('myapp\\templates\\contact.html', 'r') as template_file:
        contact_content = template_file.read()

    for key, value in data1.items():
        contact_content = contact_content.replace(key,str(value))

    with open('myapp\\templates\\testimonals.html', 'r') as template_file:
        test_content = template_file.read()
    
    for key, value in data1.items():
        test_content = test_content.replace(key,str(value))

    with open('myapp\\templates\\faq.html', 'r') as template_file:
        faq_content = template_file.read()

    for key, value in data1.items():
        faq_content = faq_content.replace(key,str(value))

    with open('myapp\\templates\\serviceproduct.html', 'r') as template_file:
        s_content = template_file.read()

    for key, value in data1.items():
        s_content = s_content.replace(key,str(value))

    with open('myapp\\templates\\footer.html', 'r') as template_file:
        footer_content = template_file.read()

    for key, value in data1.items():
        footer_content = footer_content.replace(key,str(value))
    
    user_id = request.user.id
    user_name = request.user.username
    
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO projects(user_id, name, brand,navbar,home,services,aboutus,testimonals,contactus,footer,faqs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [user_id, user_name, brand_name,nav_content,home_content,s_content,abt_content,test_content,contact_content,footer_content,faq_content]
        )
        
    with connection.cursor() as cursor:
          # cursor.execute("UPDATE projects SET home = TRIM(home) where user_id=%s" ,(request.user.id,))
           query = "SELECT * FROM projects WHERE user_id = %s"
           cursor.execute(query, (request.user.id,))
           template_changes = cursor.fetchall()

    
    return render(request, 'history.html', {'template_changes': template_changes})



def preview(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        
        # Fetch data from the database and update 'home' content
        with connection.cursor() as cursor:
            cursor.execute("UPDATE projects SET home = TRIM(home) WHERE id = %s", (user_id,))
            connection.commit()
            
            query = "SELECT home FROM projects WHERE id = %s"  
            cursor.execute(query, (user_id,))
            projects_data = cursor.fetchall()
        
        if projects_data:
            home_content = projects_data[0][0]  
            print(home_content)
            
            file_path = os.path.join('myapp', 'templates', 'home.html')
            with open(file_path, "w") as file:
                file.write(str(home_content))

        with connection.cursor() as cursor:
            query = "SELECT navbar FROM projects WHERE id = %s"  
            cursor.execute(query, (user_id,))
            projects_data = cursor.fetchall()
        
        if projects_data:
            home_content = projects_data[0][0]  
            print(home_content)
            
            file_path = os.path.join('myapp', 'templates', 'navbar.html')
            with open(file_path, "w") as file:
                file.write(str(home_content))
                print('svz')

        with connection.cursor() as cursor:
            query = "SELECT aboutus FROM projects WHERE id = %s"  
            cursor.execute(query, (user_id,))
            projects_data = cursor.fetchall()
        
        if projects_data:
            home_content = projects_data[0][0]  
            print(home_content)
            
            file_path = os.path.join('myapp', 'templates', 'about.html')
            with open(file_path, "w") as file:
                file.write(str(home_content))

        with connection.cursor() as cursor:
            query = "SELECT contactus FROM projects WHERE id = %s"  
            cursor.execute(query, (user_id,))
            projects_data = cursor.fetchall()
        
        if projects_data:
            home_content = projects_data[0][0] 
            print(home_content)
            
            file_path = os.path.join('myapp', 'templates', 'contact.html')

            with open(file_path, "w") as file:
                file.write(str(home_content))

        with connection.cursor() as cursor:
            query = "SELECT testimonals FROM projects WHERE id = %s" 
            cursor.execute(query, (user_id,))
            projects_data = cursor.fetchall()
        
        if projects_data:
            home_content = projects_data[0][0]  
            print(home_content)
            
            file_path = os.path.join('myapp', 'templates', 'testimonals.html')
            with open(file_path, "w") as file:
                file.write(str(home_content))
            
            return render(request, 'preview.html')
        else:
            return HttpResponse("No data found")
    else:
        return render(request, 'preview.html')


def load(request):
    
    return render(request, 'n.html')