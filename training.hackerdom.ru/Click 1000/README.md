Task: http://2017.hackerdom.ru/tasks/open/7/
Flag at http://click1000.training.hackerdom.ru/b1aafd69b16f47e87eb700d9cc177c0f

Your flag is: JUSTCLICKTHOUSANDTIMES


How it solved:
1) Click.py - tried to use lxml lib to parse pages, and step through next link. Did not work, got an error "IOError: Error reading file 'http://click1000.training.hackerdom.ru/467c0cf0a7f70cd6fb3999e38cdfae69': failed to load HTTP resource"

2) So... I used subprocess to call curl to do this work (I think it does not work so fast)
