5.23 
* 首页改成跳转 &radic;
* 左上角加logo &radic;
* 主页和登录页改一下风格 &radic;
* 更新后页面需要调格式 &radic;
  http://127.0.0.1:8000/doctor/pendingDiagnosis/call
  http://127.0.0.1:8000/patient/makeAppointment/detail
* 加入结算功能
* 加人像图片
* 加入药品库管理人员
* 加入检查人员
* 预约挂号查看医生信息









5.19 ddl 5.23
* 挂号记录只显示最新10条
  * 患者只能同时有两个激活的挂号     &radic;(先改成10个了)
* 医生处理预约
  * 先叫号->去诊断，删除,返回 &radic;

* 医生查看待诊断信息 &radic;
  * 假如可以翻页，按时间分页
  * 不能的话，只显示今天

* 右上角用户名，登出 &radic;
* 登陆之后患者直接跳到预约挂号，医生跳到待诊断信息 &radic;
* 挂号显示是否已处理 &radic;

* 5.23-更新后发现bug
    * 诊断记录页面右上角欢迎有名字，诊断详情无名字，患者类似，二级页面无名字&radic;
    * 患者预约挂号失败，会报错&radic;
* 5.23-更新后页面需要调格式
  * http://127.0.0.1:8000/doctor/pendingDiagnosis/call
  * http://127.0.0.1:8000/patient/makeAppointment/detail