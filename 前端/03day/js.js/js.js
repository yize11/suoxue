$(function(){
			//绑定增加按钮的点击事件
			$('#btn1').click(function() {
				//获取文本框的内容
				var txt = $('#txt1').val();
				//清空文本框的内容
				$('#txt1').val('');

				//判断文本框的内容不允许为空
				if(txt == ''){
					alert('请输入内容！');
					return;
				}

				//按照用户输入的内容准备好一个li列表项（从结构中复制，并替换其中的文字）
				var $li = $('<li><span>' + txt + '</span><a href="javascript:;" class="up"> ↑ </a><a href="javascript:;" class="down"> ↓ </a><a href="javascript:;" class="del">删除</a></li>');
				//把li追加到ul中
				$li.appendTo('#list');
			});

			/*
			//删除的点击监听（这种方式绑定会导致后增加的条目无法删除，因为监听在页面ready的时候绑定，还没有产生后增加的条目，所以无法实现动态绑定）
			$('.del').click(function() {
				$(this).parent().remove();
			});
			*/

			//使用事件委托可以实现动态绑定，并且性能更高
			$('#list').delegate('a', 'click', function() {
				//获取点击元素的class属性的值
				var handler = $(this).attr('class');

				//根据class属性的值判断点的是删除还是排序
				switch(handler){
					case 'del'://删除
						var txt = $(this).parent().children(':first').html();
						if(confirm('你确定要删除"'+txt+'"吗？')){
							$(this).parent().remove();
						}
						break;
					case 'up'://向上
						//如果当前元素之前的元素长度为0，说明前边没有其它元素了
						if($(this).parent().prev().length == 0){
							alert('到顶了！');
							return;
						}
						//把当前li插到前边，谁的前边？它前一个元素的前边
						$(this).parent().insertBefore($(this).parent().prev());
						break;
					case 'down'://向下
						//如果当前元素之后的元素长度为0，说明后边没有其它元素了
						if($(this).parent().next().length == 0){
							alert('到底了！');
							return;
						}
						//把当前li插到后边，谁的后边？它后一个元素的后边
						$(this).parent().insertAfter($(this).parent().next());
						break;
				}
			});
		})