from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from  .models import Article
from django.contrib import messages


def comment(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = article
            comment.save()
            return redirect("index")
    else:
        form = CommentForm()  # POST isteği değilse boş bir form oluşturun

    context = {
        "form": form,
        "articles": [article],  # Eğer makaleleri göstermeyi planlıyorsanız burada listeye eklemelisiniz
    }

    return render(request, "articles.html", context)




