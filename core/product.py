import urllib2,json
key = 'AIzaSyC7BnxpiiFqTV6GLyztM0qQ0pvlgDlDQdQ'

def query(q):
  url = "https://www.googleapis.com/shopping/search/v1/public/products?key=%s&country=US&q=%s&crowdBy=brand:1&alt=json"%(key,q)
  return json.loads(urllib2.urlopen(url).read())['items'][0]['product']

