from typing import Any
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'



class DeadPool(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Deadpool',
            'body': 'My name is Wade Wilson. My Strength is being invincible, so im weak to nothing',
            'image': '/static/images/deadpool.jpg'
        }
    
class SpiderMan(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': 'My name is Peter Parker. I am as strong as a spider and weak to family loss',
            'image': '/static/images/spiderman.jpg'
        }

class SuperMan(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Superman',
            'body': 'My name is Clark Kent. Im the strongest hero ever, but become weak with green rocks',
            'image': '/static/images/superman.jpg'
        }
    
class BatMan(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'BatMan',
            'body': 'My name is Bruce Wayne. I am extremely rich and am weak to emotions and commitment',
            'image': '/static/images/batman.jpg'
        }