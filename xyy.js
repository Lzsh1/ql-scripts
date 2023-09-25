
/**
 * @fileoverview Example to compose HTTP request
 * and handle the response.
 *
 */

ck =$request.headers.Cookie
url = '小阅阅'
console.log(ck)
$notify(decodeURI(url), "小阅阅ck获取成功", ck);
    $done();
