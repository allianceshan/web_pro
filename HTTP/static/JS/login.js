// 按钮点击事件提交用户登录数据

function ajaxLogin()
{
	console.log("点击函数");
	$("#div_edit").hide();	
	$.post("resource.shtml", 
	{
		action : "delete",
		id : id,
		},
		function(data)
		{
			var obj = new Function("return" + data)();
			if(obj.result=="ok")  
			{
				location.reload();
			}
			else {
				$.noty.consumeAlert(
				{
					layout: 'topCenter', type: 'error', dismissQueue: true});	
					alert(obj.message);
					}	
				});	
}

function myFunction(){
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			console.log(xmlhttp.responseText);
			console.log(xmlhttp.responseText.length);
			// if(xmlhttp.responseText.length < 20)
			document.getElementById("login_error_message").innerHTML=xmlhttp.responseText;
			// else
				// window.location.href ="/";
				{
					// $('#login_pan').modal('hide');									//将登录框隐藏并且更新登录按钮为注销，以及显示登录的账号用户名
				}
		}
	}
	var tohttp = "/login_form";
	xmlhttp.open("POST",tohttp,true);
	var  username = document.getElementById("recipient-name");						//获取输入框的值
	var  password = document.getElementById("message-text");    					//获取输入框的值
	//var  error_mess = document.getElementById("login_error_message").innerHTML;    	//获取错误信息的值
	console.log(username.value);
	console.log(password.value);
	//console.log(error_mess);

	//document.getElementById("login_error_message").innerHTML = "";
	if(username.value != "" && username != " " && password.value !="" && password.value !=" ")
	{
		var form1 = document.form1;		
		console.log(form1)
		var formdata = 	new	FormData(form1);
		console.log(formdata)
		xmlhttp.send(formdata);
	}
	//else
		//var login_err =  document.getElementById("login_error_message").value;
		//document.getElementById("login_error_message").innerText= "用户名或者密码错误"
		//console.log(login_err);
}

function myFunction1()
{
	var  username = document.getElementById("recipient-name");	//获取输入框的值
	var  password = document.getElementById("message-text");    	//获取输入框的值
	var  error_mess = document.getElementById("login_error_message").innerHTML;    	//获取输入框的值
	console.log(username.value);
	console.log(password.value);
	console.log(error_mess);
	document.getElementById("login_error_message").innerHTML = "";
	if(username.value != "" && username != " " && password.value !="" && password.value !=" ")
	{
		var form1 = document.form1;										//获取表单
		form1.action="login_form";										//设置表单提交的容器
		form1.submit();
	}
	else
		var login_err =  document.getElementById("login_error_message").value;
		document.getElementById("login_error_message").innerText= "用户名或者密码错误"
		console.log(login_err);
}

function login_load()
{
	document.getElementById("login_error_message").innerText= ""
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