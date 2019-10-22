from bot.models import SearchHistory


def create_history(query):
    SearchHistory.objects.create(key=query)

def check_history(query):
    res = SearchHistory.objects.filter(key__icontains=query).order_by('-created')
    return res