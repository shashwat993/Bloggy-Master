# this file is made with the purose of creating forms for our model.. so that then views.py can import and then make dictionary and finally able to send to the 
#template!

from django import forms  # module will help us to make form
from .models  import Article #is module ka form bnana h jaise

class Create_article(forms.ModelForm):  #This syntax things.. waise it tells it inhereting forms.Modelform class.. U can remember it by like.. Make form for class smthing


    class Meta:         # this is syntax.. u cant change name.!:-(  Meta, model and fields goota be same !
        model=Article   # storing the Article in variable model... deep copy!  # hafta keep name as model only 
        fields=['title','body','slug','thumb_pic']  # ok Now model ka form created with this line .. Now import in vews and then send to template 


#we wont add Created_by field in fields..cuz we dont want user to choose it... it shd be auomatic !