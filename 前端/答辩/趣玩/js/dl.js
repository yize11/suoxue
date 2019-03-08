$function(){
	var error_name = false;
	var error_pwd = false;
	//失去焦点时验证用户名
	$('#username').blur(function(){
		check_username();
	})

	//获取焦点时隐藏提示信息
	$('#username').focus(function(){
		$(this).prev().hide();
	})

	//密码
	$('#password1').blur(function(){
		check_pwd();
	})
	$('#password1').focus(function(){
		$(this).prev().hide();
	})
	function check_username(){
		var val = $('#username').val();
		var re = /^\w{5,15}$/;//匹配数字字母下划线，5-15位

		if(val == ''){
			$('#username').prev().html('用户名不能为空！');
			$('#username').prev().show();
			error_name = true;
			return;
		}

		if(re.test(val)){//匹配上了就是正确的
			error_name = false;
		}else{
			$('#username').prev().html('用户名是包含数字、字母、下划线的5-15位字符');
			$('#username').prev().show();
			error_name = true;
			return;
		}
	}
	function check_pwd(){
		var val = $('#password1').val();
		var re = /^[a-zA-Z0-9\#\&\$]{6,16}$/;//[]表示范围，匹配数字字母特殊符号，6-16位

		if(val == ''){
			$('#password1').prev().html('密码不能为空！');
			$('#password1').prev().show();
			error_pwd = true;
			return;
		}

		if(re.test(val)){//匹配上了就是正确的
			error_pwd = false;
		}else{
			$('#password1').prev().html('密码是包含数字、字母、#&$的6-16位字符');
			$('#password1').prev().show();
			error_pwd = true;
			return;
		}
	}
	$('.form').submit(function() {
		//防止用户上来就直接点提交，上面验证都未执行，所以先执行一次
		check_username();
		check_pwd();
		if(error_name || error_pwd){
			return false;
			
		}

	});

}