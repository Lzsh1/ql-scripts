ck =$request.headers.Cookie
var CookieValue = ck.match(/ysmuid=.+?;/)
console.log(ck)
$notify(decodeURI(url), "小阅阅ck获取成功", "ysmuid="+CookieValue);
    $done();