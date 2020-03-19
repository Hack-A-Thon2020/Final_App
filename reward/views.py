from django.shortcuts import render
from books.models import count

# Create your views here.
def user_reward(request, user_id):
    user = count.objects.get(user_id_id=user_id)
    return render(request, 'user_reward.html', {'user_det': user})