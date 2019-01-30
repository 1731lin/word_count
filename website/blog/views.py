from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	return render(request, 'left.html')

#count 
def count(request):
	return render(request,'count.html')

#count result
def count_result(request):
	user_text=request.GET['text']
	value_result=len(user_text)

	word_dict={}

	#词频统计
	for word in user_text:
		if word not in word_dict:
			word_dict[word]=1
		else:
			word_dict[word]+=1

	#字典排序
	sorted_dict=sorted(word_dict.items(),key=lambda w:w[1],reverse=True)
	
	return render(request,'count_result.html',
			{'key_result1': value_result,'text1': user_text,
			'word_dict1':word_dict,'sorted_dict1': sorted_dict,
			'f1':sorted_dict[0]})