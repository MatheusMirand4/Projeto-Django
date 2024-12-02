from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all()  
    return render(request, 'blog/home.html', {'posts': posts})

# Função criar post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = PostForm()  

    return render(request, 'blog/create_post.html', {'form': form})

# Função exibir detalhes de post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id) 
    return render(request, 'blog/post_detail.html', {'post': post})

# Função editar post
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save() 
            return redirect('home') 
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

# Função excluir post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete() 
        return redirect('home') 
    return render(request, 'blog/delete_post.html', {'post': post})
