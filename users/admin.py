from django.contrib import admin
from users.api.fishing.models import Profile, Fish
from users.api.characters.models import Character, Character_Weapon, Character_Grasta, Character_Skill

admin.site.register(Profile)
admin.site.register(Fish)
admin.site.register(Character)
admin.site.register(Character_Weapon)
admin.site.register(Character_Skill)
admin.site.register(Character_Grasta)
