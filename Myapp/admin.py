from django.contrib import admin
from . models import *
admin.site.register(Profile )
admin.site.register(Post )
admin.site.register(Posts )
admin.site.register(Like )
admin.site.register(Follow)

# Register your models here.
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = [
#         'username',
#         'first_name',
#         'last_name',
#         'email',
#         'password',
#     ]

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'bio', 'location', 'birth_date')

# admin.site.register(Post)


# @admin.register(ProfilePic)
# class ProfilePicAdmin(admin.ModelAdmin):
#     list_display = ('user','post','profile', 'pic')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = [
#         'post',
#         'user',
#         'text',
#         'created_at',       
#    ]

# @admin.register(Follow)
# class FollowAdmin(admin.ModelAdmin):
#     list_display = [
#         'follower',
#         'following',        
#         'created_at',        
#     ]

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
    # list_display = [
    #     'user',
    #     'post',        
    #     'created_at',        
    # ]