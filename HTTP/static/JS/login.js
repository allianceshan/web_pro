// 按钮点击事件提交用户登录数据
function myFunction()
{
	var  username = document.getElementById("recipient-name").value;		//获取输入框的值
	var  password = document.getElementById("message-text").value;    	//获取输入框的值
	console.log(username);
	console.log(password);
	if(username != "" && username != " " && password !="" && password !=" ")
	{
		var form1 = document.form1;										//获取表单
		form1.action="login_form";										//设置表单提交的容器
		form1.submit();
	}
	else
		console.log("用户名或密码不能为空");
}
