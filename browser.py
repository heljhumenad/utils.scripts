#! /usr/bin/python3

import webbrowser as wb


class Browser:

    def __init__(self):
        self.https = 'https://www.'
        self.link = {
                    'facebook': 'facebook.com/jhum.enad',
                    'twitter':  'twitter.com/kuro_arashi101',
                    'linkedin': 'linkedin.com/in/heljhum-enad/',
                    'roadmap-backend': 'roadmap.sh/backend'
                    }
        self.main()

    def main(self):
        for  links in self.link.values():
            wb.open_new_tab(self.https + links)
            wb.get('firefox')


if __name__ == '__main__':
    browser = Browser()
