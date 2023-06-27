from django.http import HttpResponse
from django.template import loader
from .modules.geniuscards import createImage

def index(request):
    template = loader.get_template("geniuscards/index.html")
    encoded_image = createImage("C:\\Users\\Aitor\\Desktop\\surimi.jpg","Yo te cojo y te mato y te mando al carajo FAIL",
                "Space Surimi", "Romantic Bogavantic")
    context = {
        'encoded_image': encoded_image
    }
    text_file = open("C:\\Users\\Aitor\\Desktop\\encoding.txt", "w")
    n = text_file.write(encoded_image)
    text_file.close()
    return HttpResponse(template.render(context))
