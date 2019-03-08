(function (){ 
        $('#zhuce').click(function() { 
          $('#regis').show(); 
          return false; 
        }); 
        $('#of').click(function () { 
          $('#regis').hide(); 
        }); 
      
         
      $('#zhuce').click(function() { 
          return false; 
        }); 
         
        //阻止默认行为（原来超链接可跳转到百度，阻止后无法跳转） 
        $('#zhuce').click(function () { 
          return false; 
        }); 
      }); 
