import comments
from django.shortcuts import redirect, render ,HttpResponse ,get_object_or_404
from comments.models import Page , UserComment
from django.contrib.auth.models import User
from django.shortcuts import redirect
from comments.templatetags import extras
from .serializers import commentSerializer
from django.http import HttpResponseRedirect, Http404, HttpResponse
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

#for basic html
def home(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request,'index.html',context)

def getpage(request , slug):
    page = Page.objects.filter(slug=slug).first()
    comments = UserComment.objects.filter(page=page , parent=None)
    replies= UserComment.objects.filter(page=page).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.id not in replyDict.keys():
            replyDict[reply.parent.id]=[reply]
        else:
            replyDict[reply.parent.id].append(reply)

    context = {'page': page ,'comments':comments ,'user': request.user ,'replyDict': replyDict}
    return render(request,'page.html',context)

#funtion for posting new comments
def post_comment(request):
    if request.method == "POST":
        comment=request.POST.get("comment")
        user = request.user
        pageid =request.POST.get('pageid')
        page = Page.objects.get(id=pageid)
        parentid= request.POST.get('parentid')
        if parentid=="":
            comment=UserComment(comment= comment, user=user, page=page)
            comment.save()
        else:
            parent= UserComment.objects.get(id=parentid)
            comment=UserComment(comment= comment, user=user, page=page , parent=parent)
            comment.save()

    return redirect(f"/{page.slug}")


#funtion to get all comment list in a page 
@login_required   #API URL = '/comment/'
def comment_list(request):
    try:
        all_comments = UserComment.objects.all()
    except:
        raise Http404
    serializer = commentSerializer(all_comments, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


#funtion to delete a comment or thread of comments
def comment_delete(request, id):
    try:
        obj = UserComment.objects.get(id=id)
    except:
        raise Http404
    if request.method == "POST":
        parent_obj_url = obj.content_object.get_absolute_url()
        obj.delete()
        return HttpResponseRedirect(parent_obj_url)
    context = {"object": obj }
    return render(request, "confirm_delete.html", context)

