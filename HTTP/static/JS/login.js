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

// function getCartData()
// {
// 	var temp = document.createElement("form");
//     temp.action ="/somedata" ;
//     temp.method = "get";
//     temp.style.display = "none";
 
//     document.body.appendChild(temp);
//     var tettt = temp.submit();
// 	document.getElementById("card_div").innerHTML="测试传递值是否合理" + tettt;
// }

function getCartData(name)
{
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		// IE6, IE5 浏览器执行代码
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			console.log(xmlhttp.responseText);
			document.getElementById("card_div").innerHTML=xmlhttp.responseText;
		}
	}
	var tohttp = "/somedata?name=" + name;
	console.log(name)
	xmlhttp.open("GET",tohttp,true);
	xmlhttp.send();
}