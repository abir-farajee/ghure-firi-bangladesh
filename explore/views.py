from django.shortcuts import render


import pyrebase
import json
import ast
from json import dumps,loads
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from datetime import datetime,timezone
import pytz




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

authe = firebase.auth()
database=firebase.database()

#---------------------------EXPLORE POST UPLOAD------------------------------

def addexplore(request):
   uid = request.session.get('uid')

   if uid is None:
    return redirect('login')
   else:
    if request.method=='POST':
         postname = request.POST['post_name']
         posttext = request.POST['post_text']
         post_img = request.POST['post_img']
           

         tz = pytz.timezone('Asia/Dhaka')
         time_now = datetime.now(timezone.utc).astimezone(tz).strftime('%H:%M %d-%m-%Y')
        
        
         uid = request.session.get('localid')
         username = request.session.get('name')

         data = {'uid':uid,
                 'postname':postname,
                 'posttext':posttext,
                 'post_image':post_img,
                 'datetime':time_now,
                 'username':username


                 }
         database.child('Post').push(data)
         check = database.child('users').child(uid).child('Explore').push(data)

         if check is not None:

                return redirect("addexplore")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/img')
    else:
        return render(request,'add_explore.html')



#---------------------------EXPLORE POST LIST------------------------------

def explore(request):
    
    uid = request.session.get('uid')

    if uid is None:
        return redirect('login')
    else:

        
        postID = database.child('Post').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postname = []
            image = []
            userid=[]
            username=[]
            postid=[]
            countlike=[]

            for i in postData:

                check=database.child('Likes').child(i).shallow().get().val()
                if check is None:
                    count="0"
                else:
                 count=len(database.child('Likes').child(i).shallow().get().val())

                wor = database.child('Post').child(i).child('postname').get().val()
                img = database.child('Post').child(i).child('post_image').get().val()
                uid = database.child('Post').child(i).child('uid').get().val()
                name = database.child('Post').child(i).child('username').get().val()
                id = i

                postname.append(wor)
                image.append(img)
                userid.append(uid)
                username.append(name)
                postid.append(id)
                countlike.append(count)
            


            comb_lis = zip(postname,image,userid,username,postid,countlike)
        
            uid = request.session.get('localid')
            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

            return render(request,'explore.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        else:
            postname = []
            image = []
            userid=[]
            text=[]
            datetime=[]

            postname.append('n')
            image.append('n')
            userid.append('n')
            text.append('n')
            datetime.append('n')
            comb_lis = zip(postname,image,userid,text,datetime)

            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'explore.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})


#---------------------------SINGLE EXPLORE POST------------------------------

def post_check(request):

    if request.method=='POST':
        postid = request.POST['postid']

        a = request.session['localid']


        postID = database.child('Likes').child(postid).child(a).get().val()
        if postID is not None:
            like = "true"
        else:
            like = "false"


        post_img =database.child('Post').child(postid).child('post_image').get().val()
        post_title =database.child('Post').child(postid).child('postname').get().val()
        post_desc =database.child('Post').child(postid).child('posttext').get().val()
        username =database.child('Post').child(postid).child('username').get().val()

        name = database.child('Post').child(postid).child('username').get().val()

        uid = request.session.get('uid')
        username= database.child("users").child(uid).child("username").get().val()

        print(like)
        print(postID)

        return render(request,'post_check.html',{'w':post_title,'p':post_desc,'name':username,'e':name,'img':post_img,'postid':postid,'checklike':like})

    else:
        return render(request,'check.html')


#---------------------------POST LIKE ------------------------------

def addlike(request):

    if request.method=='POST':
        
        postid = request.POST['postid']

        a = request.session['localid']

        data = {a:"RValues"
                 }


        database.child('Likes').child(postid).update(data)

    
        post_img =database.child('Post').child(postid).child('post_image').get().val()
        post_title =database.child('Post').child(postid).child('postname').get().val()
        post_desc =database.child('Post').child(postid).child('posttext').get().val()

        name = database.child('Post').child(postid).child('username').get().val()

        uid = request.session.get('uid')
        username= database.child("users").child(uid).child("username").get().val()

        return render(request,'post_check.html',{'w':post_title,'p':post_desc,'name':username,'e':name,'postid':postid,'img':post_img})




#---------------------------POST UNLIKE ------------------------------

def unlike(request):

    if request.method=='POST':
        
        postid = request.POST['postid']

        a = request.session['localid']

       
        database.child('Likes').child(postid).child(a).remove()

        
        post_img =database.child('Post').child(postid).child('post_image').get().val()
        post_title =database.child('Post').child(postid).child('postname').get().val()
        post_desc =database.child('Post').child(postid).child('posttext').get().val()

        name = database.child('Post').child(postid).child('username').get().val()

        

        return render(request,'post_check.html',{'w':post_title,'p':post_desc,'e':name,'img':post_img,'postid':postid,'checklike':"false"})










       




