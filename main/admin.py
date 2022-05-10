from django.contrib import admin
from . models import (Author,About,Album,Skill,Fact,
                    Testimonials,Summary,Experience,
                    Education,Service,Category,Contact,Contact)
 

class AlbumAdmin(admin.ModelAdmin):
	list_display=('category','image_tag','album_title','album_subtitle') 
admin.site.register(Album,AlbumAdmin)       

admin.site.register(Author)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Fact)
admin.site.register(Testimonials)
admin.site.register(Summary)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Service)
admin.site.register(Category)


class ContactAdmin(admin.ModelAdmin):
 	list_display=('conatact_name','contact_email','contact_message') 
admin.site.register(Contact,ContactAdmin)      