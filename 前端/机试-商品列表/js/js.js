$.ajax({
			url: 'js/data.json',
			type: 'get',
			dataType: 'json'
		})
		.done(function(data) {
			// alert(data.code);
			// console.log("success");
			if(data.code == 200){
			    $('.list').empty();
			    for(var i=0; i<data.data.length; i++){
			        var $li = $('<li><img src="' +data.data[i].imgUrl+'"><c1>'+data.data[i].price+'</c1><a href="#"><span>'+data.data[i].name+'</span></a> <button>立即抢购</button></li>');
			        $li.appendTo('.list');
                }
			}
		})
		.fail(function() {
			alert('连接超时！请重试');
		});