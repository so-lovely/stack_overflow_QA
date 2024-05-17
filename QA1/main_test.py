
from stack_overflow_QA.QA1.linkbot import Linkbot
if __name__ == '__main__':
    start_url =  'https://arxiv.org/'
    print(start_url)
    Linkbot = Linkbot(start_url) # start_url = https://arxiv.org/
    Linkbot.startpoint_load()
    Linkbot.find_elements_by_tag('a', filter=False)
    Linkbot.filter_hrefs(2, 'list')
    print(Linkbot.current_data)


