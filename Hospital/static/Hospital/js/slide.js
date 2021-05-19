var box=document.getElementById('verify_box');
var xbox=document.getElementById('verify_xbox');
var element=document.getElementById('btn2');
var d=document.querySelector('.verify');
var b=box.offsetWidth;
var o=element.offsetWidth;
element.ondragstart = function() {
    return false;
};
element.onselectstart = function() {
    return false;
};
element.onmousedown = function(e) {
    var disX = e.clientX - element.offsetLeft;
    document.onmousemove = function (e) {
        var l = e.clientX - disX +o;
        if(l<o){
            l=o
        }
        if(l>b){
            l=b
        }
        xbox.style.width = l + 'px';
    };
    document.onmouseup = function (e){
        var l = e.clientX - disX +o;
        if(l<b){
            l=o;
            d.nextElementSibling.innerText="验证失败";
            d.nextElementSibling.style.color="#f00";
            d.style.border='1px solid #f00'
        }else{
            l=b;
            xbox.innerHTML='<div id="btn2"><img style="margin-top:2px" class="img" src="/static/Hospital/img/d.svg"/></div>'
            d.nextElementSibling.innerText="验证通过";
            d.style.border='none';
            d.nextElementSibling.style.color="#090";
        }
        xbox.style.width = l + 'px';
        document.onmousemove = null;
        document.onmouseup = null;
    };
}