

$(document).ready(function () {
        var label = {
                'button1': 'LED A',
                'button2': 'LED B',
                'button3': 'LED C',
                'button4': 'LED D',
            };
        $('#button1').jqxSwitchButton({ height: 27, width: 81,  checked: false });
        $('#button2').jqxSwitchButton({ height: 27, width: 81,  checked: false });
        $('#button3').jqxSwitchButton({ height: 27, width: 81,  checked: false });
        $('#button4').jqxSwitchButton({ height: 27, width: 81,  checked: false });

        $('.jqx-switchbutton').on('unchecked', function (event) {
            var led = label[event.target.id];
            Z.call("set_led",[led,"ON"]);
        });
        $('.jqx-switchbutton').on('checked', function (event) {
            var led = label[event.target.id];
            Z.call("set_led",[led,"OFF"]);
        });
  
    


      Z.init({
        on_connected:  function(){$("#status").html("CONNECTED")},
        on_error:  function(){$("#status").html("ERROR")},
        on_disconnected:  function(){$("#status").html("DISCONNECTED"); return true},
        on_online:  function(evt){$("#status").html("ONLINE");},
        on_offline:  function(evt){$("#status").html("OFFLINE");},
        on_event:  function(evt){
            console.log(evt.payload.data)
            $("#text1").after("TESTO: ", evt.payload.data);     // Append new element
            $("#text1").after("<br>");
        }
      })
});