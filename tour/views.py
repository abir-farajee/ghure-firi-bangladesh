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
from django.core.mail import send_mail
import requests 
import random 
from random import randint
from django.urls import reverse
import urllib.request
import urllib.parse
import pdfkit
from django.utils.crypto import get_random_string



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

#---------------------------All Tour Place View------------------------------

def all(request):
    
    uid = request.session.get('uid')

    if uid is None:
        return redirect('login')
    else:

        
        postID = database.child('Tour').child('Place').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            postData.sort(reverse=True)

            
            tour_name = []
            tour_image = []
            
            place_id=[]


            for i in postData:


                pack_img = database.child('Tour').child('Place').child(i).child('place_img').get().val()
                pack_name = database.child('Tour').child('Place').child(i).child('place_name').get().val()
                

                id = i


                tour_name.append(pack_name)
                tour_image.append(pack_img)


                place_id.append(id)
            print(tour_name)


     

     
            
            comb_lis = zip(tour_name,tour_image,place_id)
        
            uid = request.session.get('localid')
            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()

        
    

        
            return render(request,'tour.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        else:
            tour_name = []
            tour_image = []  
            place_id=[]
            

            tour_name.append('n')
            tour_image.append('n')
            
            comb_lis = zip(tour_name,tour_image,place_id)

            user_photo= database.child("users").child(uid).child("Image Url").get().val()
            user_email= database.child("users").child(uid).child("email").get().val()
            user_phone= database.child("users").child(uid).child("phone").get().val()
            user_name= database.child("users").child(uid).child("username").get().val()
            return render(request,'tour.html',{'comb_lis':comb_lis,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})


#---------------------------Single Tour Details------------------------------

def tourdetails(request):
    
  uid = request.session.get('uid')

  if uid is None:
        return redirect('login')
  else:
    if request.method=='POST':
        placeID = request.POST['placeid']

        
        postID = database.child('Tour').child('Place').child(placeID).child('Hotels').shallow().get().val()
        if postID is not None:
            postData=[]
            for i in postID:

                postData.append(i)

            hotelname = []
            hotelimage = []
            price=[]
            desc=[]
            hotelid=[]
       
            for i in postData:

                hotel_name = database.child('Tour').child('Place').child(placeID).child('Hotels').child(i).child('hotel_name').get().val()
                hotel_price = database.child('Tour').child('Place').child(placeID).child('Hotels').child(i).child('room_price').get().val()
                hotel_img = database.child('Tour').child('Place').child(placeID).child('Hotels').child(i).child('hotel_img').get().val()
                hotel_desc = database.child('Tour').child('Place').child(placeID).child('Hotels').child(i).child('hotel_descr').get().val()
                hotel_place = database.child('Tour').child('Place').child(placeID).child('place_name').get().val()
                hotel_id=i
                

                
                
                hotelname.append(hotel_name)
                hotelimage.append(hotel_img)
                price.append(hotel_price)
                desc.append(hotel_desc)
                hotelid.append(hotel_id)
            
        else:
            hotelname = []
            hotelimage = []
            price=[]
            desc=[]
            hotelid=[]

            hotelname.append('n')
            hotelimage.append('n')
            price.append('n')
            desc.append('n')
            hotelid.append('n')
            hotel_place = database.child('Tour').child('Place').child(placeID).child('place_name').get().val()
       

            
        comb_lis = zip(hotelname,hotelimage,price,desc,hotelid)
        hotel_list= zip(hotelname,hotelimage,price,desc,hotelid)


        transID = database.child('Tour').child('Place').child(placeID).child('Transportation').shallow().get().val()
        if transID is not None:
            transData=[]
            for i in transID:

                transData.append(i)

            trans_type = []
            trans_image = []
            ticket_price=[]
            trans_name=[]
            ac_type=[]
            seatnumber=[]
            transid=[]
            time_one=[]
            time_two=[]
            time_three=[]
    
            for i in transData:

                trans = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('trans').get().val()
                tprice = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('ticket_price').get().val()
                transimg = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('trans_img').get().val()
                transname = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('trans_name').get().val()
                actype = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('type').get().val()
                seats = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('seats').get().val()
                timeone = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('time_one').get().val()
                timetwo = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('time_two').get().val()
                timethree = database.child('Tour').child('Place').child(placeID).child('Transportation').child(i).child('time_three').get().val()
                tid=i
                
                
                
                trans_type.append(trans)
                trans_image.append(transimg)
                trans_name.append(transname)    
                ticket_price.append(tprice)
                ac_type.append(actype)
                seatnumber.append(seats)
                time_one.append(timeone)
                time_two.append(timetwo)
                time_three.append(timethree)
                transid.append(tid)
    
        else:
            trans_type = []
            trans_image = []
            ticket_price=[]
            trans_name=[]
            ac_type=[]
            seatnumber=[]
            transid=[]
            time_one=[]
            time_two=[]
            time_three=[]

            trans_type.append('n')
            trans_image.append('n')
            trans_name.append('n')   
            ticket_price.append('n')
            ac_type.append('n')
            seatnumber.append('n')
            time_one.append('n')
            time_two.append('n')
            time_three.append('n')
            transid.append('n')
    
            
        trans_list = zip(trans_type,trans_image,trans_name,ticket_price,ac_type,seatnumber,transid)
        trans_list_for_book = zip(trans_type,trans_image,trans_name,ticket_price,ac_type,seatnumber,transid)
        time_slot = zip(transid,time_one,time_two,time_three)


        
        uid = request.session.get('localid')
        user_photo= database.child("users").child(uid).child("Image Url").get().val()
        user_email= database.child("users").child(uid).child("email").get().val()
        user_phone= database.child("users").child(uid).child("phone").get().val()
        user_name= database.child("users").child(uid).child("username").get().val()


      
        return render(request,'tour_details.html',{'placeid':placeID,'time_slot':time_slot,'comb_lis':comb_lis,'hotel_list':hotel_list,'trans_list':trans_list,'trans_list_for_book':trans_list_for_book,"placename":hotel_place,"name":user_name,"photo":user_photo,"email":user_email,"phone":user_phone})
        

def booking(request):
    
  uid = request.session.get('uid')

  if uid is None:
        return redirect('login')
  else:
    if request.method=='POST':
        hotelid = request.POST['hotelid']
        transid = request.POST['transid']
        timeslot = request.POST['timeslot']
        pessenger = request.POST['pessenger']
        journeydate = request.POST['journeydate']
        placeid = request.POST['placeid']


        get_place_name = database.child('Tour').child('Place').child(placeid).child('place_name').get().val()

        get_hotel_name = database.child('Tour').child('Place').child(placeid).child('Hotels').child(hotelid).child('hotel_name').get().val()
        get_hotel_price = database.child('Tour').child('Place').child(placeid).child('Hotels').child(hotelid).child('room_price').get().val()
        get_hotel_info = database.child('Tour').child('Place').child(placeid).child('Hotels').child(hotelid).child('hotel_descr').get().val()

        get_trans_name = database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).child('trans_name').get().val()
        get_ticket_price = database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).child('ticket_price').get().val()
        get_type = database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).child('type').get().val()
        get_tname = database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).child('trans').get().val()
        get_seat = database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).child('seats').get().val()

        ticketprice = int(pessenger)*int(get_ticket_price)
        total= int(get_hotel_price) + ticketprice

        booking_data={
            'Time_Slot': timeslot,
            'Pessenger': pessenger,
            'Journey_Date': journeydate,
            'Hotel_Name': get_hotel_name,
            'Hotel_Price': get_hotel_price,
            'Place_Name': get_place_name,
            'Ticket_Price': get_ticket_price,
            'Transportation_Type':get_type,
            'Transportation_Name':get_tname,
            'Total_Amount':str(total),
            'Transportation_Company': get_trans_name,
            'Payment':"Unpaid",
            'uid': uid
        }


        set_booking = database.child('Orders').push(booking_data)

        newseats= int(get_seat)-int(pessenger)

        data={
            'seats':str(newseats)
        }

        database.child('Tour').child('Place').child(placeid).child('Transportation').child(transid).update(data)


        if set_booking is not None:


            bookedID=set_booking['name']
            message = "Booking successfully done. Now complete your payment."
            

            

            return render(request,'payment.html',{'success_msg':message,'bookedID':bookedID,'Time_Slot':timeslot,'Pessenger':pessenger,'Journey_Date':journeydate,'Hotel_Name':get_hotel_name,'Hotel_Info':get_hotel_info,'Hotel_Price':get_hotel_price,'Place_Name':get_place_name,'Ticket_Price':get_ticket_price,'Total':total,'Transportaion_Company':get_trans_name,'Transportation_Type':get_type})


        

def sendmsg(request):

    uid = request.session.get('uid')

    if uid is None:
            return redirect('login')
    else:
        if request.method=='POST':
            phonenumber = request.POST['phone']
            bookingid = request.POST['bookedID']


            r1 = randint(100000,999999)
            transaction = get_random_string(8)
            request.session['verification_code']=r1

            print(r1)





          #  api = "http://api.greenweb.com.bd/api.php"

          #  token = "3fa8287141f334db97c7bb32c9de68d3"

           

          # data = {'token':token, 
          #          'to':phonenumber, 
          #          'message':'Your verification code for GhureFiri Bangladesh is - '+ str(r1)} 
          #  
          #  responses = requests.post(url = api, data = data) 

          #  response = responses.text 
          #  print(response)
            tourname = database.child('Orders').child(bookingid).child('Place_Name').get().val()
            amount = database.child('Orders').child(bookingid).child('Total_Amount').get().val()

            data={
                'Order_ID':bookingid,
                'uid':uid,
                'Amount':amount,
                'Tour_Name':tourname,
                'TransactionID':transaction
            }

            database.child("Transaction").child(bookingid).update(data)

            print(transaction)


            return render(request,"tour_pay_verify.html",{'phone':phonenumber,'bookingid':bookingid})
        else:
            return redirect('all')



             

def tourpaymentverify(request):

    uid = request.session.get('uid')

    if uid is None:
            return redirect('login')
    else:

            code = int(request.POST['code'])
            bookingid = request.POST['bookedID']
            transactionid = request.POST['transactionid']
            systemcode=int(request.session.get('verification_code'))
            

            if code==systemcode:
                message = "Payment verification Successfull"
                request.session['message']=message
                del request.session['verification_code']
                data={
                    'Payment':"Processing",
                    'TransactionID':transactionid
                }

                database.child('Orders').child(bookingid).update(data)


                return render(request,"tour_pay_verify.html",{'messg':message,'type':"success"})

                

            else:
                message = "Not Match"
                print(systemcode)
                print(code)


                return render(request,"tour_pay_verify.html",{'messg':message,'type':"error"})
                

def mail(request):

    
  test= get_random_string(8)

  print(test)



