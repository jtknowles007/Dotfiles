#! /usr/bin/env python3

import getjson
import textwrap
url = 'https://api.quotable.io/quotes/random'

feed = getjson.getjson(url)
quote = feed[0]['content']
author = feed[0]['author']
quotewrap = textwrap.fill(quote,35)
print(quotewrap)
print("- " + author)
