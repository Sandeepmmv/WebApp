from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm ,ProfileForm
from django.contrib.auth.models import User 
from .models import *
from django.contrib import messages 
from  itertools import chain
# Create your views here.

@login_required(login_url='signin')
def home_view(request):
    user_obj = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user= request.user)
    post = Post.objects.all()

    user_following_list = []
    feed = []

    user_following = Follow.objects.filter(follower = request.user.username)

    for users in user_following:
        user_following_list.append(users.user)
    
    for usernames in user_following:
        feed_list = Post.objects.filter(user = usernames)
        feed.append(feed_list)
    
    feed_lists = list(chain(*feed))


    context = {'user_profile' : user_profile,'post':feed_lists}
    return render(request,'Myapp/home.html',context)

@login_required(login_url='signin')
def AccountSetting_view(request):
    user_profile = Profile.objects.get(user= request.user)
    # print(user_profile)
    form = request.POST
    if request.method == 'POST':
        if request.FILES.get('profileimage') == None:
            profileimage = user_profile.profileimage
            bio = request.POST['bio']
            location = request.POST['location']
            birth_date = request.POST['birth_date']
            print(form)
            if birth_date == '' :
                pass
            else:
                user_profile.birth_date = birth_date  
            user_profile.profileimage = profileimage
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('profileimage') != None:
            profileimage = request.FILES.get('profileimage')
            bio = request.POST['bio']
            location = request.POST['location']
            birth_date = request.POST['birth_date']
            if birth_date == '' :
                pass
            else:
                user_profile.birth_date =birth_date        
            user_profile.profileimage = profileimage
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        
        return redirect('home')
        # form = ProfileForm(request.POST)
        # # id_user = 
        # print(form)
        # if form.is_valid():
        #     form.save()
        
    context = {'user_profile' : user_profile}
    return render(request,'Myapp/account_setting.html',context)

@login_required(login_url='signin')
def search_view(request):
    user_obj = User.objects.get(username = request.user.username)
    user_profile =Profile.objects.get(user=user_obj)

    if request.method == "POST":
        username = request.POST['username']
        username_obj = User.objects.filter(username__icontains=username)

        username_profile = []
        username_profile_list = []

        for users in username_obj:
            username_profile.append(users.id)
        
        for ids in username_profile:
            profile_list = Profile.objects.filter(id_user = ids)
            username_profile_list.append(profile_list)
        
        username_profile_lists = list(chain(*username_profile_list))

        context ={
            'username_profile_lists':username_profile_lists,
            'username_obj':username_obj,
            'user_profile':user_profile,
        }
    return render(request,'Myapp/search.html',context)

@login_required(login_url='signin')
def follow_view(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if Follow.objects.filter(follower=follower,user=user).first():
            delete_follower = Follow.objects.get(follower=follower,user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower =Follow.objects.create(follower=follower,user=user)
            new_follower.save()

            return redirect('/profile/'+user)
    else:
        return redirect('home')
    
@login_required(login_url='signin')
def profile_view(request,pk):
    user_obj = User.objects.get(username = pk)
    user_profile = Profile.objects.get(user=user_obj)
    #taking a length of user post
    user_post = Post.objects.filter(user = pk)
    user_post_length =len(Post.objects.filter(user = pk))

    #FOLLOW BUTTON
    follower = request.user.username
    user = pk
    if Follow.objects.filter(follower=follower,user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_follower =len(Follow.objects.filter(user=pk))
    user_following =len(Follow.objects.filter(follower=pk))
    context ={
        'user_obj':user_obj,
        'user_profile':user_profile,
        'user_post':user_post,
        'user_post_length':user_post_length,
        'button_text':button_text,
        'user_follower':user_follower,
        'user_following':user_following,
    }
    return render(request,'Myapp/profile.html',context)

@login_required(login_url='signin')
def post_like_view(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    post = Post.objects.get(uid=post_id)
    print(post)
    like_filter = Like.objects.filter(post_id=post_id,username=username).first()

    if like_filter == None:
        new_like = Like.objects.create(post_id=post_id,username=username)
        new_like.save()
        post.nos_likes = post.nos_likes +1
        post.save()
        return redirect('home')
    else:
        like_filter.delete()
        post.nos_likes = post.nos_likes -1
        post.save()
        return redirect('home')

@login_required(login_url='signin')
def upload_view(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('post_photo')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user,image=image,caption=caption)
        new_post.save()
        return redirect('home')

    return render(request,'Myapp/home.html')

def SignUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        # print(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully register..")
            #log user in and redirect to settings page
            user_login = authenticate(username=username, password=password)
            login(request, user_login)

            #create a Profile object for the new user
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            return redirect('account_setting')

        else:
            if User.objects.filter(username = username).exists():
                messages.info(request,"User name is taken")
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email is taken")
                return redirect('signup')
            else:
                messages.info(request,"something is wrong")
                return render(request,'Myapp/signup.html')
            
    else:
        form =SignUpForm()
    context = {'form':form}
    return render(request,'Myapp/signup.html',context)

def SignIn_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username,password)
        user = authenticate(username=username,password=password)
        # print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Login')
            return redirect('home')
        else:
            messages.success(request,'Something is wrong')
            return redirect('signin')
    else:
        return render(request,'Myapp/signin.html')
# def SignIn_view(request):
    # if request.method == 'POST':
    #     password = request.POST['password']
    #     username = request.POST['username']

    #     if User.objects.filter(username=username).exists():
    #         if User.objects.filter(password=password):
    #             messages.success(request,'Loged Out')
    #             return redirect('home')
    #         else:
    #             messages.error(request,'Wrong emailid')
    #             return redirect('signin')
    #     else:
    #         messages.error(request,'wrong password')
    #         return redirect('signin')
    # else:
    #     return render(request,'Myapp/signin.html')

@login_required(login_url='signin')
def SignOut_view(request):
    logout(request)
    messages.info(request,"Successfully Logout...")
    return redirect('signin')

#geting user data
# def user_view(request):
    data=User.objects.all().values()
    post = Post.objects.all().values()
    profile = Profile.objects.all().values()
    profilepic = ProfilePic.objects.all().values()
    like = Like.objects.all().values()
    follow = Follow.objects.all().values()
    comment = Comment.objects.all().values()
    return render(request,'Myapp/user.html',{'data':data,'profilepic':profilepic,'profile':profile,'like':like,'follow':follow,'comment':comment,'post':post})