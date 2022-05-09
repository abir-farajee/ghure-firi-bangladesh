
import pyrebase
import json
import ast
from json import dumps,loads
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth






#---------------------------FIREBASE CONNECTION------------------------------

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


#-------SIGNUP FUNCTION WORKS HERE---------------------

def signup(request):

    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']

        user = authe.create_user_with_email_and_password(email,password)
        authe.send_email_verification(user['idToken'])
        message = "Verification mail Send to Your Email"

        uid=user['localId']
        data = {
        "username":name,
        'uid':uid,
        'email':email,
        
        }

        database.child('users').child(uid).set(data)

        if user is not None:
            return render(request,"login.html",{"v_message":message})
        else:
            messages.info(request,'invalid credentials')
            return redirect('signup')
    else:

            return render(request,'signup.html')
            

#-------LOGIN FUNCTION WORKS HERE---------------------
   

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['pass']

        user = authe.sign_in_with_email_and_password(email,password)
        new = authe.get_account_info(user['idToken'])
 
        for j in new['users']:
            print (j['emailVerified'])

            check_user = j['emailVerified']

            if check_user is False:
                message="Please check your Email Inbox and Verify your Account"
                return render(request,"login.html",{"message":message})



        if user is not None:
            print(user['localId'])
            session_id=user['localId']
            request.session['uid']=str(session_id)
            request.session['localid']=session_id

            user_name = database.child("users").child(session_id).child("username").get()
            user_photo = database.child("users").child(session_id).child("Image_Url").get().val()

            print(user_name.val())
            x=user_name.val()
            request.session['name']=str(x)
            request.session['photo']=user_photo

            return redirect("/main")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
 
         return render(request,'login.html')


#------------------------SIGN IN WITH GOOGLE-------------------------------------

def googlelogin(request):
    if request.method=='POST':
        email = request.POST['email']
        photo = request.POST['photo']
        uid = request.POST['uid']
        username = request.POST['username']
        
        data = {
        "username":username,
        'uid':uid,
        'email':email,
        'Image_Url':photo
        }

        database.child('users').child(uid).update(data)

        request.session['uid']=str(uid)
        request.session['localid']=uid

        return redirect("/main")

    else:
 
         return render(request,'login.html')

#------------------------PROFILE PICTURE UPLOAD-------------------------------------


def img(request):

    if request.method=='POST':
         url = request.POST['url']

         uid = request.session.get('uid')

         data = {'Image_Url':url}

         check = database.child('users').child(uid).update(data)

         if check is not None:

                return redirect("profile")
         else:
                messages.info(request,'invalid credentials')
                return redirect('/img')
    else:
        return render(request,'image.html')


#---------------------------USER PROFILE DATA------------------------------

def profile(request):
    
    uid = request.session.get('localid')
    print(uid)

    if uid is None:
        return redirect('login')
    else:
        uid = request.session.get('localid')

        postID = database.child("Post").order_by_child("uid").equal_to(uid).get().val()
      
        if postID is not None:

            postData=[]
            for i in postID:

                postData.append(i)
        
            postname = []
            image = []
            userid=[]
            text=[]
            datetime=[]
            postid=[]
            postby=[]
            for i in postData:
                

                wor=database.child('Post').child(i).child('postname').get().val()
                img=database.child('Post').child(i).child('post_image').get().val()
                uid=database.child('Post').child(i).child('uid').get().val()
                txt=database.child('Post').child(i).child('posttext').get().val()
                date=database.child('Post').child(i).child('datetime').get().val()
                pby=database.child('Post').child(i).child('username').get().val()
                pid=i
                postname.append(wor)
                image.append(img)
                userid.append(uid)
                text.append(txt)
                datetime.append(date)
                postid.append(pid)
                postby.append(pby)
            print(postname)

        

        

            comb_lis = zip(postname,postby,image,userid,text,datetime,postid)

        
        

            user_photo= database.child("users").child(uid).child("Image_Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

        


        
        
            return render(request,'profile.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})

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

            user_photo= database.child("users").child(uid).child("Image_Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'profile.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})



#---------------------------CURRENT USER'S BOOKING LIST------------------------------

def mybooking(request):
    
    uid = request.session.get('localid')
    print(uid)

    if uid is None:
        return redirect('login')
    else:
        uid = request.session.get('localid')

        bookingID = database.child("Orders").order_by_child("uid").equal_to(uid).get().val()
        
      
        if bookingID is not None:

            bookingData=[]
            for i in bookingID:

                bookingData.append(i)

            timeslot=[]
            pessenger=[]
            journeydate=[]
            get_hotel_name=[]
            get_hotel_price=[]
            get_place_name=[]
            get_ticket_price=[]
            get_type=[]
            get_trans_name=[]
            Payment=[]
            tamount=[]
            transtype=[]
            bookingid=[]
            for i in bookingData:
                

                tslot=database.child('Orders').child(i).child('Time_Slot').get().val()
                pssngr=database.child('Orders').child(i).child('Pessenger').get().val()
                date=database.child('Orders').child(i).child('Journey_Date').get().val()
                hname=database.child('Orders').child(i).child('Hotel_Name').get().val()
                rprice=database.child('Orders').child(i).child('Hotel_Price').get().val()
                ttype=database.child('Orders').child(i).child('Transportation_Type').get().val()
                tname=database.child('Orders').child(i).child('Transportaion_Company').get().val()
                pname=database.child('Orders').child(i).child('Place_Name').get().val()
                tprice=database.child('Orders').child(i).child('Ticket_Price').get().val()
                pymnt=database.child('Orders').child(i).child('Payment').get().val()
                tamnt=database.child('Orders').child(i).child('Total_Amount').get().val()
                typnme=database.child('Orders').child(i).child('Transportation_Name').get().val()

                bookid=i
                timeslot.append(tslot)
                pessenger.append(pssngr)
                journeydate.append(date)
                get_hotel_name.append(hname)
                get_hotel_price.append(rprice)
                get_place_name.append(pname)
                get_ticket_price.append(tprice)
                get_type.append(ttype)
                get_trans_name.append(tname)
                Payment.append(pymnt)
                tamount.append(tamnt)
                transtype.append(typnme)
                bookingid.append(bookid)
        else:
            timeslot=[]
            pessenger=[]
            journeydate=[]
            get_hotel_name=[]
            get_hotel_price=[]
            get_place_name=[]
            get_ticket_price=[]
            get_type=[]
            get_trans_name=[]
            Payment=[]
            tamount=[]
            transtype=[]
            bookingid=[]

            timeslot.append('n')
            pessenger.append('n')
            journeydate.append('n')
            get_hotel_name.append('n')
            get_hotel_price.append('n')
            get_place_name.append('n')
            get_ticket_price.append('n')
            get_type.append('n')
            get_trans_name.append('n')
            Payment.append('n')
            tamount.append('n')
            transtype.append('n')
            bookingid.append('n')

        mybookedlist = zip(tamount,transtype,bookingid,timeslot,pessenger,journeydate,get_hotel_name, get_hotel_price,get_place_name,get_ticket_price,get_type,get_trans_name,Payment)
         

        PackbookingID = database.child("PackageOrders").order_by_child("uid").equal_to(uid).get().val()
        if PackbookingID is not None:

            PackbookingData=[]
            for j in PackbookingID:

                PackbookingData.append(j)

            PackCovering_Spots=[]
            PackDining=[]
            PackHotel_name=[]
            PackJourney_Date=[]
            PackPackage_Description=[]
            PackPackage_Name=[]
            PackPayment=[]
            PackTotal_Amount=[]
            PackTransportation=[]
            packbookedid=[]

            for j in PackbookingData:
                

                spot=database.child('PackageOrders').child(j).child('Covering_Spots').get().val()
                dining=database.child('PackageOrders').child(j).child('Dining').get().val()
                hotelname=database.child('PackageOrders').child(j).child('Hotel_name').get().val()
                jdate=database.child('PackageOrders').child(j).child('Journey_Date').get().val()
                descp=database.child('PackageOrders').child(j).child('Package_Description').get().val()
                pckname=database.child('PackageOrders').child(j).child('Package_Name').get().val()
                pay=database.child('PackageOrders').child(j).child('Payment').get().val()
                totalamount=database.child('PackageOrders').child(j).child('Total_Amount').get().val()
                trans=database.child('PackageOrders').child(j).child('Transportation').get().val()
                packbookid=j


                PackCovering_Spots.append(spot)
                PackDining.append(dining)
                PackHotel_name.append(hotelname)
                PackJourney_Date.append(jdate)
                PackPackage_Description.append(descp)
                PackPackage_Name.append(pckname)
                PackPayment.append(pay)
                PackTotal_Amount.append(totalamount)
                PackTransportation.append(trans)
                packbookedid.append(packbookid)

        else:
            PackCovering_Spots=[]
            PackDining=[]
            PackHotel_name=[]
            PackJourney_Date=[]
            PackPackage_Description=[]
            PackPackage_Name=[]
            PackPayment=[]
            PackTotal_Amount=[]
            PackTransportation=[]
            packbookedid=[]

            PackCovering_Spots.append('n')
            PackDining.append('n')
            PackHotel_name.append('n')
            PackJourney_Date.append('n')
            PackPackage_Description.append('n')
            PackPackage_Name.append('n')
            PackPayment.append('n')
            PackTotal_Amount.append('n')
            PackTransportation.append('n')
            packbookedid.append('n')


        PackBookedList = zip(packbookedid,PackCovering_Spots,PackDining,PackHotel_name,PackJourney_Date,PackPackage_Description,PackPackage_Name,PackPayment,PackTotal_Amount,PackTransportation)

        user_photo= database.child("users").child(uid).child("Image_Url").get().val()
        user_email= database.child("users").child(uid).child("email").get().val()
        user_phone= database.child("users").child(uid).child("phone").get().val()
        user_name= database.child("users").child(uid).child("username").get().val()

        


        
        
        return render(request,'mybooking.html',{'PackBookedList':PackBookedList,'mybookedlist':mybookedlist,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})

 
#---------------------------TOUR TICKET PRINT------------------------------       

def ticket(request):

    if request.method=='POST':

        bookingid = request.POST['bookingid']
        uid = request.session.get('localid')

        tslot=database.child('Orders').child(bookingid).child('Time_Slot').get().val()
        pssngr=database.child('Orders').child(bookingid).child('Pessenger').get().val()
        date=database.child('Orders').child(bookingid).child('Journey_Date').get().val()
        hname=database.child('Orders').child(bookingid).child('Hotel_Name').get().val()
        rprice=database.child('Orders').child(bookingid).child('Hotel_Price').get().val()
        ttype=database.child('Orders').child(bookingid).child('Transportation_Type').get().val()
        tname=database.child('Orders').child(bookingid).child('Transportaion_Company').get().val()
        pname=database.child('Orders').child(bookingid).child('Place_Name').get().val()
        tprice=database.child('Orders').child(bookingid).child('Ticket_Price').get().val()
        pymnt=database.child('Orders').child(bookingid).child('Payment').get().val()
        tamnt=database.child('Orders').child(bookingid).child('Total_Amount').get().val()
        typnme=database.child('Orders').child(bookingid).child('Transportation_Name').get().val()

        user_phone= database.child("users").child(uid).child("phone").get().val()
        user_name= database.child("users").child(uid).child("username").get().val()


    return render(request,'ticket.html',{'user_phone':user_phone,'user_name':user_name,'tamount':tamnt,'actype':ttype,'bookingid':bookingid,'timeslot':tslot,'pessenger':pssngr,'journeydate':date,'get_hotel_name':hname,'get_hotel_price':rprice,'pname':pname,'tprice':tprice,'get_type':typnme,'tname':tname,'payment':pymnt})


#---------------------------PACKAGE TICKET PRINT------------------------------    

def packticket(request):

    if request.method=='POST':

        bookingid = request.POST['bookingid']
        uid = request.session.get('localid')

        spot=database.child('PackageOrders').child(bookingid).child('Covering_Spots').get().val()
        dining=database.child('PackageOrders').child(bookingid).child('Dining').get().val()
        hotelname=database.child('PackageOrders').child(bookingid).child('Hotel_name').get().val()
        jdate=database.child('PackageOrders').child(bookingid).child('Journey_Date').get().val()
        descp=database.child('PackageOrders').child(bookingid).child('Package_Description').get().val()
        pckname=database.child('PackageOrders').child(bookingid).child('Package_Name').get().val()
        pay=database.child('PackageOrders').child(bookingid).child('Payment').get().val()
        totalamount=database.child('PackageOrders').child(bookingid).child('Total_Amount').get().val()
        trans=database.child('PackageOrders').child(bookingid).child('Transportation').get().val()

        user_phone= database.child("users").child(uid).child("phone").get().val()
        user_name= database.child("users").child(uid).child("username").get().val()


    return render(request,'packticket.html',{'totalamount':totalamount,'spot':spot,'dining':dining,'hotelname':hotelname,'jdate':jdate,'descp':descp,'pckname':pckname,'pay':pay,'trans':trans,'user_phone':user_phone,'user_name':user_name})
#---------------------------USER PROFILE UPDATE------------------------------

def update_profile(request):

    if request.method=='POST':
         name = request.POST['username']
         phone = request.POST['phone']

         uid = request.session.get('localid')

         data = {'username':name, 'phone':phone}

         push = database.child('users').child(uid).update(data)

         if push is not None:

                return redirect("profile")
         else:
                messages.info(request,'invalid credentials')
                return redirect('profile')
    else:
        return redirect('/main')

def pass_reset(request):

    if request.method=='POST':
        email = request.POST['email']

        authe.send_password_reset_email(email)
        message="Email Send for password RESET. Check your inbox"
        return render(request,"login.html",{"pass_reset_message":message})
     
    else:
 
         return render(request,'forgotpass.html')


def deletepost(request):

    if request.method=='POST':
         pid = request.POST['postid']


         delete = database.child('Post').child(pid).remove()

         if delete is not None:

                return redirect("profile")
         else:
                messages.info(request,'invalid credentials')
                return redirect('profile')
    else:
        return redirect('/main')

    
def logout(request):
    del request.session['uid']
    del request.session['localid']
    auth.logout(request)
  
    return redirect("login")

