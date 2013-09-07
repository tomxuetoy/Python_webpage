import urllib2
 
def get_content(url):
    return urllib2.urlopen(url).read()
 
def write_content(content, path):
    f = open(path, 'w')  #写模式
    f.write(content)
    f.close()
 
content = get_content('http://www.baidu.com')
write_content(content, 'baidu.html')
