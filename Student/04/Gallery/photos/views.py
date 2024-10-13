from pathlib import Path
from typing import Any
from django.views.generic import TemplateView


def photo_list():
    def photo_details(i, f):
        caption = f'Caption for Photo {i}' 
        name = f'{i}'
        if i == 0:
            caption = f'BeastBoy: He can transform into any animal but is always green.'
            name = f'BeastBoy'
        if i == 1:
            caption = f'Cyborg: Has all the best technology, but would not reccomend getting wet'
            name = f'Cyborg'
        if i == 2:
            caption = f'Raven: Magical abilites with wild power but has daddy issues'
            name = f'Raven'
        if i == 3: 
            caption = f'Robin: Seasoned acrobat with plenty of training, but he has no powers'
            name = f'Robnin'
        if i == 4:
            caption = f'Starfire: Super strong alien with lazers, but very gulible'
            name = f'Starfire'
        return dict(id=i, file=f, caption=caption, name=name)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos    

class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)

class DetailListView(TemplateView):
    template_name = 'list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return super().get_context_data(**kwargs)
