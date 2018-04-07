var jq = jQuery.noConflict();
jq( document ).ready(function() {
	jq('.selectbox').on('mouseover',hover)
	jq('.selectbox').on('mouseout',hoverout)
	
	jq('.options').on('click',getValue);
    var ele = jq("<div></div>").text('China').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
	  var ele = jq("<div></div>").text('North Korea').addClass("options").on('click',getValue)
  	jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('South Korea').addClass("options").on('click',getValue)
  	jq('#scroll_bar').append(ele)
  	var ele = jq("<div></div>").text('Japan').addClass("options").on('click',getValue)
  	jq('#scroll_bar').append(ele)
  	var ele = jq("<div></div>").text('Hong Kong').addClass("options").on('click',getValue)
  	jq('#scroll_bar').append(ele)
  	var ele = jq("<div></div>").text('Taiwan').addClass("options").on('click',getValue)
  	jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('Singapore').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('Vietnam').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('Thailand').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('Philippines').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
    jq('#scroll_bar').append(ele)
    var ele = jq("<div></div>").text('New Zealand').addClass("options").on('click',getValue)
    jq('#scroll_bar').append(ele)
  	jq('.submit').on('click',submit)
  	
    jq('.btn').on('click',changeimg)
    jq('#my_img').attr('src',dict["1"])
});

var dict={
  "1":"img/cn_2017.png",
  "2":"img/cn_2008.png",
  "3":"img/cn_2007.png",
  "4":"img/jp_2017.png",
  "5":"img/jp_2007.png",
  "6":"img/hk_2017.png",
  "7":"img/nz_2017.png",
  "8":"img/de_2017.png",
  "9":"img/Philippines_2017.png"
}

var getValue = function(e){
	var text = jq(e.target).text()
	jq('.cur_selected').text(text)
	 jq('.selectbox').removeClass('selectbox-list')
}
var hover = function(e){
	
    jq('.selectbox').addClass('selectbox-list')
}
var hoverout = function(e){
        jq('.selectbox').removeClass('selectbox-list')
}
var submit = function(e){
	jq(e.target).unbind('click')
    jq(e.target).addClass('onclick')
	var country = jq('.cur_selected').text()
	var request = jq.ajax({
       url: "/index.php",
       timeout:0,
       method: "GET",
       data:{
       	 country:country
       },
       dataType: "text",
       beforeSend:function(xhr){
          jq('.result').text('Running... Please wait for 1 minute... :)')
          console.log('Running')

    }
    });
 
request.done(function( msg ) {
	  binding()
	  jq('.result').text(msg)
      console.log(msg)
  });

}

var binding = function(){
	jq('.submit').removeClass('onclick')
	jq('.submit').bind('click',submit)
}

var changeimg = function(e){
 jq('.btn-on-click').removeClass('btn-on-click')

  cur_btn = e.target
  jq(e.target).addClass('btn-on-click')
  var key = jq(e.target).data('myvalue')
  jq('#my_img').attr('src',dict[key])
}