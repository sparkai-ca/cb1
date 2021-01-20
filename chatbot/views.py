from django.http import JsonResponse
from chatbot.utils.googlesearcher import scraper
from chatbot.utils.chatter import chatbot_response
import re
from django.views.decorators.csrf import csrf_exempt



replacables = [
 'i', 'we', 'you', 'he', 'she', 'it',
 'they', 'me', 'us', 'her', 'him', 'will',
 'them', 'mine', 'ours', 'yours', 'was',
 'hers', 'his', 'theirs', 'my', 'is', 'not'
 'our', 'your', 'their', 'myself', 'are',
 'yourself', 'herself', 'himself', 'were',
 'itself', 'ourselves', 'yourselves', 'do',
 'themselves', 'all', 'another', 'any',
 'anybody', 'anyone', 'anything', 'both',
 'each', 'either', 'everybody', 'everyone',
 'everything', 'few', 'many', 'most', 'shall',
 'neither', 'nobody', 'none', 'no one', 'can'
 'nothing', 'one', 'other', 'others', 'should',
 'several', 'some', 'somebody', 'someone', 'where',
 'something', 'such', 'what', 'whatever', 'about',
 'which', 'whichever', 'who', 'whoever', 'could',
 'whom', 'whomever', 'whose', 'how', 'when',
]


# Create your views here.
@csrf_exempt
def index(request):
    response = ''
    if request.method == 'POST':
        _input = request.POST.get('input_cb1')
        _input = str(_input)
        print('input:', _input)

        res, ints = chatbot_response(_input)

        if len(ints)==1 and float(ints[0]['probability'])>0.8:
            response = res
            print('output:', response)
        else:
            _input = _input.lower()
            _input = ''.join(re.findall('[a-zA-Z\n0-9 ]', _input))
            _input = _input.split(' ')
            input_ = ''
            for i in _input:
                if i in replacables:
                    pass
                else:
                    input_ = input_ + ' ' + i
            input_ = input_.replace('  ', ' ').strip()
            print('input: ', input_)
            response = scraper.searchQuery(input_)
            print('output:', response)

    return JsonResponse({ 'output_cb1': response })

