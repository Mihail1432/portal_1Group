from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Comment
from .forms import ForumForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden



def forum_list(request):
    forums = Forum.objects.all()
    return render(request, 'forum/forum_list.html', {'forums': forums})

@login_required
def forum_detail(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    comments = Comment.objects.filter(forum=forum)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.forum = forum
            comment.user = request.user
            comment.save()
            return redirect('forum:forum_detail', forum_id=forum.id)

    return render(request, 'forum/forum_detail.html', {'forum': forum, 'comments': comments, 'form': form})



@login_required
def create_forum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.created_by = request.user
            forum.save()
            return redirect('forum:forum_list')  # Перенаправление на список форумов после создания
    else:
        form = ForumForm()
    
    return render(request, 'forum/create_forum.html', {'form': form})




@login_required
def edit_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)

    if request.user != forum.created_by:
        return redirect('forum:forum_detail', forum_id=forum.id)

    if request.method == 'POST':
        form = ForumForm(request.POST, instance=forum)
        if form.is_valid():
            form.save()
            return redirect('forum:forum_detail', forum_id=forum.id)
    else:
        form = ForumForm(instance=forum)

    return render(request, 'forum/edit_forum.html', {'form': form, 'forum': forum})

@login_required
def delete_forum(request, forum_id):
    forum = get_object_or_404(Forum, id=forum_id)
    
    # Проверка, является ли текущий пользователь создателем форума
    if request.user != forum.created_by:
        # Можно вернуть HTTP 403 или перенаправить на страницу с уведомлением
        return HttpResponseForbidden("You are not allowed to delete this forum.")
    
    if request.method == 'POST':
        forum.delete()
        return redirect('forum:forum_list')
    
    return render(request, 'forum/delete_forum.html', {'forum': forum})


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return redirect('forum:forum_detail', forum_id=comment.forum.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('forum:forum_detail', forum_id=comment.forum.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'forum/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.user:
        return redirect('forum:forum_detail', forum_id=comment.forum.id)

    if request.method == 'POST':
        comment.delete()
        return redirect('forum:forum_detail', forum_id=comment.forum.id)

    return render(request, 'forum/delete_comment.html', {'comment': comment})


