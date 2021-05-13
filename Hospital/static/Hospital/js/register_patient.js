var na = document.querySelector('#na'); //姓名
var phone = document.querySelector('#phone'); //手机号
var sfz = document.querySelector('#sfz'); //身份证
var pwd = document.querySelector('#pwd'); //确认密码
var btn1 = document.querySelector('.btn1'); //立即注册
var load = document.querySelector('.load');
var pawd = document.getElementById('pawd'); //密码
var ruo = document.getElementById('ruo'); //弱
var zo = document.getElementById('zo'); //中
var btn = document.getElementById('btn'); //获取验证码
var qiang = document.getElementById('qiang'); //强
var ps = document.querySelectorAll('p');
var inputs = document.querySelectorAll('input');
var form = document.querySelector('form');
var oY = document.getElementById("year"); //年
var oM = document.getElementById("month"); //月
var oD = document.getElementById("day"); //日
var me;
var ad;
var ph;
var pd;
var sf;
//设置年龄
window.onload = function() {
        //oY.options.add(new Option(1970));
        //oY.appendChild(new Option(1971));
        ini(oY, oM, oD);
        oY.onchange = function() {
            ref(oY, oM, oD);
        }
        oM.onchange = function() {
            ref(oY, oM, oD);
        }
    }
    //任务一：初始化年月日列表框
function ini(y, m, d) {
    for (var i = 1970; i < 2051; i++) {
        y.appendChild(new Option(i));
    }
    for (var i = 1; i < 13; i++) {
        m.appendChild(new Option(i));
    }
    for (var i = 1; i < 32; i++) {
        d.appendChild(new Option(i));
    }
}
//任务二：当年、月列表框内容改变时，刷新日列表框
function ref(y, m, d) {
    var yv = y.value;
    var mv = m.value;
    var dv;
    switch (parseInt(mv)) {
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12:
            dv = 31;
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            dv = 30;
            break;
        case 2:
            if ((yv % 4 == 0 && yv % 100 != 0) || (yv % 400 == 0)) {
                dv = 29;
            } else {
                dv = 28;
            }
            break;
    }
    d.length = 0; //清空日列表
    for (var i = 1; i < dv + 1; i++) {
        d.appendChild(new Option(i));
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

phone.onblur = function() { //手机号判断
    var reg = /^1[3|4|5|7|8]\d{9}$/;

    function z(re, e) { //封装函数判断传入的数据
        if (e.value != '') {
            if (re.test(e.value)) {
                e.className = "r";
                e.nextSibling.src = 'img/d.svg';
                ps[e.index].style.color = "#04f014";
                ps[e.index].innerHTML = "";
                ph = true;
            } else {
                e.className = "f";
                e.nextSibling.src = 'img/c.svg';
                ps[e.index].style.color = "#f00";
                ps[e.index].innerText = "请填写正确的手机号码";
                ph = false;
            }
        } else {
            e.className = "f";
            e.nextSibling.src = 'img/c.svg';
            ps[e.index].style.color = "#f00";
            ps[e.index].innerText = "不能为空";
            ph = false;
        }
    }
    z(reg, this);
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

for (var i = 0; i < 6; i++) { //获得焦点
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

btn.onclick = function() { //获取验证码
    if (ph) {
        var t = 59;
        btn.disabled = 'true';
        btn.style.opacity = '0.5';
        btn.style.cursor = "not-allowed";
        phone.readOnly = 'true';
        var y = setInterval(function() {
            btn.innerText = t + 'S';
            t--;
            if (t == -1) {
                phone.readOnly = '';
                btn.innerText = '获取验证码';
                btn.disabled = '';
                btn.style.opacity = '1';
                btn.style.cursor = "pointer";
                clearInterval(y);
            }
        }, 1000)
    } else {
        phone.className = "f";
        phone.nextSibling.src = 'img/c.svg';
        ps[phone.index].style.color = "#f00";
        ps[phone.index].innerText = "请填写正确的手机号码";
        return false;
    }
}

btn1.onclick = function() { //提交数据
    if (me) {
        if (ad) {
            if (pd) {
                if (ph) {
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
                    phone.className = "f";
                    phone.nextSibling.src = 'img/c.svg';
                    ps[phone.index].style.color = "#f00";
                    ps[phone.index].innerText = "请填写正确的手机号码";
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