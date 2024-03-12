from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
posts=[
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Shivam kumar Jha",
        "date": date(2023, 3,12),
        "title":"Mountain Hiking",
        "excerpt":"Moutain is the best thing for the human kind",
        "content":"""<p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Inventore, dignissimos earum? Tenetur odio vel aut eos fuga maiores suscipit omnis ex ab magni, facilis distinctio laborum rem voluptates porro repellendus.
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Accusantium natus ipsam, corrupti ducimus quis consectetur nobis voluptas. Iste quod et cupiditate atque commodi libero veniam earum, natus reprehenderit, voluptas nemo?
        
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Voluptatibus ipsam recusandae eaque accusantium nam quia dolore at veniam qui blanditiis, illum neque tenetur soluta veritatis perferendis facere, minima sed fugiat!</p>
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit voluptates libero, exercitationem inventore, deserunt nemo eius rem aut ex, reprehenderit accusantium dolores laudantium. Impedit aut nulla ex facilis obcaecati soluta.</p>"""
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):    
    return render(request,"blog/all-posts.html")
def post_detail(request, slug):
    return render(request, "blog/post-detail.html")