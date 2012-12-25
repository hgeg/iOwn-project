from pprint import pprint
import urllib2,json
key = 'AIzaSyC7BnxpiiFqTV6GLyztM0qQ0pvlgDlDQdQ'

def query(q):
  url = "https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=%s&restrictBy=condition:new&thumbnails=*:200&alt=json"%(key,q)
  data = json.loads(urllib2.urlopen(url).read())
  #print data
  try:
    return [e['product'] for e in data['items'] if 'images' in e['product']]
  except: return []