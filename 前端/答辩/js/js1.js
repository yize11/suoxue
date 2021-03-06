$(function(){
	var $li = $('.slide_pics li');
	var len = $li.length;//4张
	var $prev = $('.prev');//左按钮
	var $next = $('.next');//右按钮
	var nextli = 0;//将要运动过来的li
	var nowli = 0;//当前要离开的li
	var timer = null;


	//除第一个li，都定位到右侧
	$li.not(':first').css({left:600});

	//动态创建小圆点
	$li.each(function(index){
		//创建li
		var $sli = $('<li></li>');
		//第一个li添加选中样式
		if(index == 0){
			$sli.addClass('active');
		}
		//将小圆点的li添加到ul中
		$sli.appendTo('.points');
	})

	$points = $('.points li');
	// alert($points.length);//4个小圆点

	//小圆点的点击事件
	$points.click(function() {
		nextli = $(this).index();
		//当点击当前张的小圆点时，不做任何操作，防止跳变的Bug
		if(nextli == nowli){
			return;
		}
		move();
		$(this).addClass('active').siblings().removeClass('active');
	});

	//左按钮的点击事件
	$prev.click(function() {
		nextli--;
		move();
		//改变圆点样式
		$points.eq(nextli).addClass('active').siblings().removeClass('active');
	});

	//右按钮的点击事件
	$next.click(function() {
		nextli++;
		move();
		//改变圆点样式
		$points.eq(nextli).addClass('active').siblings().removeClass('active');
	});

	//针对外层的slide做鼠标进入和离开事件，因为鼠标指针有可能进入到左右翻页和小圆点的范围
	//mouseenter使鼠标进入子元素也能清除定时器
	$('.slide').mouseenter(function() {
		clearInterval(timer);
	});
	$('.slide').mouseleave(function() {
		timer = setInterval(autoplay, 3000);
	});

	//定时器循环自动播放
	timer = setInterval(autoplay, 3000);

	//自动播放的逻辑与点击下一张是相同的
	function autoplay(){
		nextli++;
		move();
		//改变圆点样式
		$points.eq(nextli).addClass('active').siblings().removeClass('active');
	}

	function move(){
		//向右走到第一张，再继续走时
		if(nextli < 0){
			nextli = len - 1;//将要来的是最后一张
			nowli = 0;//要离开的是第一张
			$li.eq(nextli).css({left:-498});//把最后一张定位到左侧，准备进入
			$li.eq(nowli).stop().animate({left: 498});//离开的第一张走到右侧
			$li.eq(nextli).stop().animate({left: 0});//马上要进来的最后一张走进来
			nowli = nextli;//要离开的赋值为刚进入的最后一张
			return;//下边是正常情况的，不执行，直接返回
		}
		//向左走到最后一张，再继续走时
		if(nextli > len - 1){
			nextli = 0;//将要来的是第一张
			nowli = len - 1;//要离开的是最后一张
			$li.eq(nextli).css({left:498});//把第一张定位到右侧，准备进入
			$li.eq(nowli).stop().animate({left: -498});//离开的最后一张走到左侧
			$li.eq(nextli).stop().animate({left: 0});//马上要进来的第一张走进来
			nowli = nextli;//要离开的赋值为刚进入的第一张
			return;//下边是正常情况的，不执行，直接返回
		}

		if(nextli > nowli){
			//马上要进来的这张瞬间移动到右边
			$li.eq(nextli).css({left:498});
			//当前这张离开
			$li.eq(nowli).stop().animate({left: -498});
		}else{
			//马上要进来的这张瞬间移动到左边
			$li.eq(nextli).css({left:-498});
			//当前这张离开
			$li.eq(nowli).stop().animate({left: 498 });
		}
		//马上要进来的这张走到0的位置
		$li.eq(nextli).stop().animate({left: 0});
		nowli = nextli;
	}
})
/***********************************************type选项卡*****************************************************/
//闭包做选项卡
		window.onload = function(){
			var aBtn = document.getElementById('btns').getElementsByTagName('input');
			var aCon = document.getElementById('contents').getElementsByTagName('div');
			// alert(aCon.length);

			//循环所有的选项卡按钮
			for(var i=0; i<aBtn.length; i++){
				(function(i){
					//给每个选项卡按钮添加点击事件
					aBtn[i].onclick = function(){
						//遍历所有选项卡按钮
						for(var j=0; j<aBtn.length; j++){
							//将每个选项卡按钮都设为灰色
							aBtn[j].className = '';
							//将每个内容区都隐藏
							aCon[j].className = '';
						}
						//this代表当前点击的Button对象
						this.className = 'cur';//当前点击的按钮为金色

						// alert(i);//不加闭包时，不管点哪个按钮，i都等于3

						//加闭包保存了索引值才有效
						aCon[i].className = 'active';//当前点击的按钮对应的内容显示
					}
				})(i);
			}
		}
		/***************************************type选项卡******************************************************/
		window.onload = function(){
			var aBtn = document.getElementById('btn').getElementsByTagName('input');
			var aCon = document.getElementById('content').getElementsByTagName('div');
			// alert(aCon.length);

			//循环所有的选项卡按钮
			for(var i=0; i<aBtn.length; i++){
				(function(i){
					//给每个选项卡按钮添加点击事件
					aBtn[i].onclick = function(){
						//遍历所有选项卡按钮
						for(var j=0; j<aBtn.length; j++){
							//将每个选项卡按钮都设为灰色
							aBtn[j].className = '';
							//将每个内容区都隐藏
							aCon[j].className = '';
						}
						//this代表当前点击的Button对象
						this.className = 'curs';//当前点击的按钮为金色

						// alert(i);//不加闭包时，不管点哪个按钮，i都等于3

						//加闭包保存了索引值才有效
						aCon[i].className = 'actives';//当前点击的按钮对应的内容显示
					}
				})(i);
			}
		}