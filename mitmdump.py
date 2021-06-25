import mitmproxy.http

t1 = """
// 改写 `languages` 
Object.defineProperty(navigator, "languages", {
  get: function() {
    return ["en", "es"];
  }
});

//改写 `plugins`
Object.defineProperty(navigator, "plugins", {
  get: () => new Array(Math.floor(Math.random() * 6) + 1),
});

// 改写`webdriver`
Object.defineProperty(navigator, "webdriver", {
  get: () => false,
});
"""
class Tb(object):
    def response(slef,flow: mitmproxy.http.HTTPFlow):
        if 'http://bj.gsxt.gov.cn/index.html' == flow.request.url:
                flow.response.text = "<script>"+t1+"</script>" + flow.response.text
                print('注入成功')

addons = [
    Tb()
]