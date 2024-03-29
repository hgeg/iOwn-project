#!/usr/bin/python2.4
# -*- coding: utf-8 -*-
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""Full text search query against the shopping search API"""

import pprint

from discovery import build


SHOPPING_API_VERSION = 'v1'
DEVELOPER_KEY = 'AIzaSyC7BnxpiiFqTV6GLyztM0qQ0pvlgDlDQdQ'


def main():
  """Get and print a feed of all public products matching the search query
  "digital camera".

  This is achieved by using the q query parameter to the list method.

  The "|" operator can be used to search for alternative search terms, for
  example: q = 'banana|apple' will search for bananas or apples.

  Search phrases such as those containing spaces can be specified by
  surrounding them with double quotes, for example q='"mp3 player"'. This can
  be useful when combining with the "|" operator such as q = '"mp3
  player"|ipod'.
  """
  client = build('shopping', SHOPPING_API_VERSION, developerKey=DEVELOPER_KEY)
  resource = client.products()
  # Note the 'q' parameter, which will contain the value of the search query
  request = resource.list(source='public', country='US', q=u'ipad 2')
  response = request.execute()
  pprint.pprint(response)


if __name__ == '__main__':
    main()
