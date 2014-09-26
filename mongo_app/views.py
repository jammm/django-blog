# Create your views here.
from django.http import HttpResponse, Http404
from django import template
from django.shortcuts import render_to_response
from pymongo import MongoClient
import gridfs




def index(request):
	if request.method == "POST":
		client = MongoClient()
		db = client.test_database
		file_db = MongoClient().gridfs_images
		fs = gridfs.GridFS(file_db)
		file_obj = fs.put(request.FILES['image'].read())
		file = open("mongo_app/static/" + str(fs.get(file_obj)._id) + ".png","w")
		file.write(fs.get(file_obj).read())

		blog = ({"title":request.POST['title'], "content":request.POST['blog_content'], "image":file_obj})
		db.blogs.insert(blog)

		blogs = list()
		for i in db.blogs.find():
			file_name = str(fs.get(i['image'])._id)
			i['image'] = file_name
			blogs.append(i)



		return render_to_response("index.html",{"blogs":blogs})
	else:
		client = MongoClient()
		db = client.test_database
		file_db = MongoClient().gridfs_images
		fs = gridfs.GridFS(file_db)
		blogs = list()
		for i in db.blogs.find():
			file_name = str(fs.get(i['image'])._id)
			i['image'] = file_name
			blogs.append(i)

		return render_to_response("index.html",{"blogs":blogs})

def reset(request):
	client = MongoClient()
	db = client.test_database
	db.blogs.remove()
	return HttpResponse("Database has been reset")
