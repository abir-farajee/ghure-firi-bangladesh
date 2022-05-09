from django.shortcuts import render
import pyrebase
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth


config = {

  'apiKey': "AIzaSyAPBXBYOuClJop3F3aDEOhfF1kZjhUxGFA",
  'authDomain': "ghurefiribangladesh-e7ef2.firebaseapp.com",
  'databaseURL': "https://ghurefiribangladesh-e7ef2.firebaseio.com",
  'projectId': "ghurefiribangladesh-e7ef2",
  'storageBucket': "ghurefiribangladesh-e7ef2.appspot.com",
  'messagingSenderId': "198487718440",
  'appId': "1:198487718440:web:ab16558cabb12902c7931d",
  'measurementId': "G-B8PY09CQDG"
  }


firebase = pyrebase.initialize_app(config)

database=firebase.database()
storage = firebase.storage()


def index(request):
    uid = request.session.get('uid')
    user_name= database.child("users").child(uid).child("username").get().val()
    user_photo= database.child("users").child(uid).child("Image Url").get().val()

    if uid is None:
        return render(request,'index.html')
    else:
        return render(request,'main.html',{"name":user_name,'photo':user_photo})

    



def main(request):
    
    uid = request.session.get('uid')
    user_name= database.child("users").child(uid).child("username").get().val()
    user_photo= database.child("users").child(uid).child("Image Url").get().val()

    if uid is None:
        return redirect('login')
    else:
        return render(request,'main.html',{"name":user_name,'photo':user_photo})



def img(request):

    if request.method=='POST':
         url = request.POST['url']

       

         data = {'Image Url':url}

         check = database.child('CompressedImage').update(data)

         if check is not None:

                return redirect("img")
         else:
                messages.info(request,'invalid credentials')
                return redirect('img')
    else:
        return render(request,'image.html')






    



