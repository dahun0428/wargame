from django.shortcuts import render




def probs_list (request):
  return render (request, 'probs/probs_list.html', {})
