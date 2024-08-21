from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Comment
from .forms import ForumForm, CommentForm
from django.contrib.auth.decorators import login_required

def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

@login_required
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.created_by = request.user
            comment.save()
            return redirect('forum:forum_detail', forum_id=forum.id)
    else:
        form = CommentForm()
    
    comments = forum.comments.all()
    return render(request, 'forum/forum_detail.html', {'forum': forum, 'comments': comments, 'form': form})

@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum:forum_list')
    else:
        form = ForumForm()
    
    return render(request, 'forum/create_forum.html', {'form': form})
