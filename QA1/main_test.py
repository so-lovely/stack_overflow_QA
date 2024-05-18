
from linkbot import Linkbot
from pprint import pprint
if __name__ == '__main__':
    start_url =  'https://arxiv.org/'
    print(start_url)
    Linkbot = Linkbot(start_url) # start_url = https://arxiv.org/
    Linkbot.startpoint_load()
    Linkbot.find_elements_by_tag('a', filter=False)
    Linkbot.filter_hrefs(2, 'list')
    pprint(Linkbot.past_data)

    


