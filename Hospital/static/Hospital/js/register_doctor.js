var na = document.querySelector('#na'); //姓名
var sfz = document.querySelector('#sfz'); //身份证
var pwd = document.querySelector('#pwd'); //确认密码
var btn1 = document.querySelector('.btn1'); //立即注册
var load = document.querySelector('.load');
var pawd = document.getElementById('pawd'); //密码
var ruo = document.getElementById('ruo'); //弱
var zo = document.getElementById('zo'); //中
var department = document.getElementById('department'); //科室
var title = document.getElementById('title'); //职称
var qiang = document.getElementById('qiang'); //强
var oY = document.getElementById("year"); //年
var oM = document.getElementById("month"); //月
var oD = document.getElementById("day"); //日
var ps = document.querySelectorAll('p');
var inputs = document.querySelectorAll('input');
var form = document.querySelector('form');
var me;
var ad;
var pd;
var sf;

//设置科室、职称
window.onload = function() {
        instr(department, title); //科室
    }
    //上传科室
function instr(y, z) {
    var arr1 = ['内科', '外科', '儿科', '妇产科', '中医科', '皮肤科', '口腔科'];
    var arr2 = ['主任医师', '副主任医师', '医师'];
    for (var i = 0; i < arr1.length; i++) {
        y.appendChild(new Option(arr1[i]));
    }
    for (var i = 0; i < arr2.length; i++) {
        z.appendChild(new Option(arr2[i]));
    }
}


na.onblur = function() { //姓名正则表达式判断
    var reg = /^[\u2E80-\u9FFF,\w]{1,20}$/; //中文字符
    function z(re, e) { //封装函数判断传入的数据
        if (e.value != '') {
            if (re.test(e.value)) {
                e.className = "r";
                e.nextSibling.src = 'img/d.svg';
                ps[e.index].style.color = "#04f014";
                ps[e.index].innerHTML = "";
                me = true;
            } else {
                e.className = "f";
                e.nextSibling.src = 'img/c.svg';
                ps[e.index].style.color = "#f00";
                ps[e.index].innerText = "至少1个中文字符或字母组合";
                me = false;
            }
        } else {
            e.className = "f";
            e.nextSibling.src = 'img/c.svg';
            ps[e.index].style.color = "#f00";
            ps[e.index].innerText = "不能为空";
            me = false;
        }
    }
    z(reg, this);
}
pawd.onblur = function() { //失去焦点判断密码
    if (this.value.length < 6 || this.value.length > 16) {
        this.nextSibling.src = 'img/c.svg';
        this.className = "f";
        ps[this.index].style.color = "#f00";
        ps[this.index].innerText = "密码长度应为6~16个字符";
        ruo.style.display = "none";
        zo.style.display = "none";
        qiang.style.display = "none";
        ad = false;
    } else {
        this.className = "r";
        this.nextSibling.src = "img/d.svg";
        ps[this.index].innerHTML = "密码强度：" + state;
        ps[this.index].style.color = "#090";
        ruo.style.display = "none";
        zo.style.display = "none";
        qiang.style.display = "none";
        ad = true;
    }
}
pwd.onblur = function() { //二次输入密码
    if (this.value != '') {
        if (this.value != pawd.value) {
            ps[this.index].innerText = "两次密码不一致";
            ps[this.index].style.color = "#f00";
            this.className = "f";
            this.nextSibling.src = 'img/c.svg';
            pd = false;
        } else {
            this.className = "r";
            this.nextSibling.src = 'img/d.svg';
            ps[this.index].style.color = "#04f014";
            ps[this.index].innerText = "";
            pd = true;
        }
    } else {
        this.className = "f";
        this.nextSibling.src = 'img/c.svg';
        ps[this.index].innerText = "不能为空";
        ps[this.index].style.color = "#f00";
        pd = false;
    }
}

sfz.onblur = function() { //身份证号判断
    var reg = /^[1-9]\d{5}(18|19|20)\d{2}((0[1-9])|(1[0-2]))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$/;

    function z(re, e) {
        if (e.value != '') {
            if (re.test(e.value)) {
                e.className = "r";
                e.nextSibling.src = 'img/d.svg';
                ps[e.index].style.color = "#04f014";
                ps[e.index].innerHTML = "";
                sf = true;
            } else {
                e.className = "f";
                e.nextSibling.src = 'img/c.svg';
                ps[e.index].style.color = "#f00";
                ps[e.index].innerText = "请填写正确的身份证号";
                sf = false;
            }
        } else {
            e.className = "f";
            e.nextSibling.src = 'img/c.svg';
            ps[e.index].style.color = "#f00";
            ps[e.index].innerText = "不能为空";
            sf = false;
        }
    }
    z(reg, this);
}

for (var i = 0; i < 5; i++) { //获得焦点
    inputs[i].index = i;
    inputs[i].onfocus = function() {
        ps[this.index].style.color = "#000";
        this.nextSibling.src = '';
    }
}
var state = '弱'; //模拟密码强度判断
pawd.onkeyup = function() {
    var regStr = /[a-zA-Z]/; //所有字母
    var regNum = /[0-9]/; //所有数字
    var sup = /\W/; //所有非字母数字
    if (this.value.length >= 6) {
        ruo.style.display = "inline-block";
        ruo.className = "ruo";
        ruo.innerHTML = "弱";
        zo.style.display = "inline-block";
        zo.className = "";
        qiang.style.display = "inline-block";
        qiang.className = "";
        state = "弱";
    }
    var sn = this.value.length >= 6 && regStr.test(this.value) && regNum.test(this.value);
    var sp = this.value.length >= 6 && regStr.test(this.value) && sup.test(this.value);
    var np = this.value.length >= 6 && regNum.test(this.value) && sup.test(this.value);
    if (sn || sp || np) {
        ruo.className = "zo";
        ruo.innerHTML = "&nbsp;";
        zo.className = "zo";
        zo.innerHTML = "中";
        state = "中";
    }
    if (this.value.length >= 6 && regStr.test(this.value) && regNum.test(this.value) && sup.test(this.value)) {
        ruo.className = "qiang";
        ruo.innerHTML = "&nbsp;";
        zo.className = "qiang";
        zo.innerHTML = "&nbsp;";
        qiang.className = "qiang";
        qiang.innerHTML = "强";
        state = "强";
    }
    if (this.value.length < 6) {
        ruo.style.display = "none";
        zo.style.display = "none";
        qiang.style.display = "none";
    }
}

btn1.onclick = function() { //提交数据
    if (me) {
        if (ad) {
            if (pd) {
                if (sf) {
                    btn1.style.transform = 'scale(0)';
                    btn1.nextElementSibling.style.transform = 'scale(1)';
                    form.style.transform = 'scaleY(0)';
                    setTimeout(function() {
                        load.style.display = "block";
                    }, 1000)
                } else {
                    sfz.className = "f";
                    sfz.nextSibling.src = 'img/c.svg';
                    ps[sfz.index].style.color = "#f00";
                    ps[sfz.index].innerText = "请填写正确的身份证号";
                }
            } else {
                ps[pwd.index].innerText = "两次密码不一致";
                ps[pwd.index].style.color = "#f00";
                pwd.className = "f";
                pwd.nextSibling.src = 'img/c.svg';
            }
        } else {
            pawd.nextSibling.src = 'img/c.svg';
            pawd.className = "f";
            ps[pawd.index].style.color = "#f00";
            ps[pawd.index].innerText = "密码长度应为6~16个字符";
        }
    } else {
        na.className = "f";
        na.nextSibling.src = 'img/c.svg';
        ps[na.index].style.color = "#f00";
        ps[na.index].innerText = "至少1个中文字符或字母组合";
    }
}