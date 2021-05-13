var pwd = document.querySelector('#pwd');
var sfz = document.querySelector('#sfz');
var btn1 = document.querySelector('.btn1');
var load = document.querySelector('.load');
var ps = document.querySelectorAll('p');
var inputs = document.querySelectorAll('input');
var form = document.querySelector('form');
var sf;
var pd;
pawd.onblur = function() { //失去焦点判断密码
    if (this.value.length < 6 || this.value.length > 16) {
        this.className = "f";
        pd = false;
    } else {
        this.className = "r";
        pd = true;
    }
}

sfz.onblur = function() { //身份证号判断
    var reg = /^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/;

    function z(re, e) {
        if (re.test(e.value)) {
            e.className = "r";
            sf = true;
        } else {
            e.className = "f";
            sf = false;
        }
    }
    z(reg, this);
}

for (var i = 0; i < 2; i++) { //获得焦点
    inputs[i].index = i;
    inputs[i].onfocus = function() {
        ps[this.index].style.color = "#000";
        this.nextSibling.src = '';
    }
}

btn1.onclick = function() { //提交数据
    if (pd == true && sf == true) {
        if (xbox.offsetWidth == 280) {
            btn1.style.transform = 'scale(0)';
            btn1.nextElementSibling.style.transform = 'scale(1)';
            form.style.transform = 'scaleY(0)';
            setTimeout(function() {
                load.style.display = "block";
            }, 1000)
        } else {
            d.nextElementSibling.innerHTML = "验证失败";
            d.nextElementSibling.style.color = "#f00";
            d.style.border = '1px solid #f00';
        }
    } else {
        sfz.nextSibling.src = 'img/c.svg';
        pawd.nextSibling.src = 'img/c.svg';
        sfz.className = "f";
        pawd.className = "f";
        ps[sfz.index].style.color = "#f00";
        ps[pawd.index].style.color = "#f00";
        ps[sfz.index].innerText = "身份证或密码错误";
        ps[pawd.index].innerText = "身份证或密码错误";
    }


}