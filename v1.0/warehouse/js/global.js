var global_url = 'http://127.0.0.1:3621';
function getUrlParam(name) {
  var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
  if (reg.test(location.search.substr(1))) {
    return decodeURIComponent(RegExp.$2);
  } else if (
    reg.test(location.hash.substr(location.hash.indexOf("?") + 1))
  ) {
    return decodeURIComponent(RegExp.$2);
  } else {
    return "";
  }
}
