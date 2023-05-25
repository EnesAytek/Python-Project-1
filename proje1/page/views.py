from django.shortcuts import render
from django.http import HttpResponse, Http404
from .fake_db.pages import FAKE_DB_PAGES


# FAKE_DB_PROJECTS = [
#     f"https://picsum.photos/id/{id}/100/80" for id in range (21, 29)
    
# ] 

FAKE_DB_CAROUSEL = [
        f"https://picsum.photos/id/{id}/1200/400" for id in range (24, 28)
    ]



def home_view(request):
    context = dict(
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL = FAKE_DB_CAROUSEL,
    )
    return render(request, "pages/home_page.html", context)



def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque facilisis lobortis varius. Pellentesque convallis, tortor ac lobortis laoreet, magna ante vulputate arcu, id convallis ante sapien eu nisl. Integer pretium leo quis fringilla fringilla. In interdum dapibus massa sed consectetur. Fusce vel orci pellentesque dui fringilla euismod. Quisque fermentum nunc id hendrerit posuere. Cras elit ex, sollicitudin quis imperdiet non, tincidunt eget quam. Nullam ultrices egestas ex sed pretium. Cras porta odio id risus mattis malesuada. Donec porta non nisl eu facilisis. Ut nec velit sit amet eros facilisis sagittis. Duis sapien odio, vestibulum cursus dolor id, sollicitudin posuere orci. Fusce id imperdiet ex.'
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        )
    return render(request, "pages/about_us.html", context)



def vision_view(request):
    page_title = "Vizyonumuz"
    hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque facilisis lobortis varius. Pellentesque convallis, tortor ac lobortis laoreet, magna ante vulputate arcu, id convallis ante sapien eu nisl. Integer pretium leo quis fringilla fringilla. In interdum dapibus massa sed consectetur. Fusce vel orci pellentesque dui fringilla euismod. Quisque fermentum nunc id hendrerit posuere. Cras elit ex, sollicitudin quis imperdiet non, tincidunt eget quam. Nullam ultrices egestas ex sed pretium. Cras porta odio id risus mattis malesuada. Donec porta non nisl eu facilisis. Ut nec velit sit amet eros facilisis sagittis. Duis sapien odio, vestibulum cursus dolor id, sollicitudin posuere orci. Fusce id imperdiet ex.'
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        )
    return render(request, "pages/vision.html", context)



def contact_us_view(request):
    page_title = "İletişim"
    hero_content = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque facilisis lobortis varius. Pellentesque convallis, tortor ac lobortis laoreet, magna ante vulputate arcu, id convallis ante sapien eu nisl. Integer pretium leo quis fringilla fringilla. In interdum dapibus massa sed consectetur. Fusce vel orci pellentesque dui fringilla euismod. Quisque fermentum nunc id hendrerit posuere. Cras elit ex, sollicitudin quis imperdiet non, tincidunt eget quam. Nullam ultrices egestas ex sed pretium. Cras porta odio id risus mattis malesuada. Donec porta non nisl eu facilisis. Ut nec velit sit amet eros facilisis sagittis. Duis sapien odio, vestibulum cursus dolor id, sollicitudin posuere orci. Fusce id imperdiet ex.'
    context = dict(
        page_title = page_title,
        hero_content = hero_content,
        # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
        )
    return render(request, "pages/contact_us.html", context)



def page_view(request, slug):
    result = list(filter(lambda x: (x['url'] == slug ), FAKE_DB_PAGES))
    if result:
        context = dict(
            # FAKE_DB_PROJECTS = FAKE_DB_PROJECTS,
            page_title = result[0]["title"],
            detail=result[0]['detail'],
        )
        return render(request, "pages/page_detail.html", context)
    raise Http404
    
    