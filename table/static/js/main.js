$(document).ready(function(){
	var $doc = $(document)
	$doc.on('click', '.dropdown', function(e){
		$(this).toggleClass('is_active');
		e.stopPropagation();
	});

	$doc.on('click', function() {
	    $('.dropdown').removeClass('is_active');
	});
	$doc.on('click', 'td', function() {
	    $('tr').removeClass('is_active');
	    $(this).parent().toggleClass('is_active');
	});

	$doc.scroll(function() {
  		if ($doc.scrollTop() >2){
  			$('#header').addClass('fixed');
  			}else{
  			$('#header').removeClass('fixed');

  		}
	});

	$('.search-input').on('change', function(){
		if ($(this).val() == ""){
			$(this).removeClass('input-mark');
			location.href = '/';

		}else{
			$('.filter-input').val('');
			$(this).closest('form').submit();

		}
	});

	$('.js-input').on('change', function(){
		$(this).closest('form').submit();
	});


////////////////

	var urlParams = new URLSearchParams(window.location.search);

	var params = {
		sort: urlParams.get('sort'),
	 	transmission: urlParams.get('transmission'),
	 	volume: urlParams.get('volume'),
	 	fuel: urlParams.get('fuel'),
	 	};

	 	for (let key in params) {
	 		$('select[name="' + key + '"]').find('option[value="' + params[key] + '"]').attr("selected", "selected");

	 		if (params[key] && params[key] !=''){
	 			$('select[name="' + key + '"]').addClass('in_search');
	 		}else{
	 			$('select[name="' + key + '"]').removeClass('in_search');
	 		}
	 	}

	var color = urlParams.get('reliability_color');

	if(color){
		$('input[name="reliability_color"]').prop("checked", true);
		$('.rating-row').addClass("js-color");
	} else{

		$('.rating-row').removeClass("js-color");
	}

/////////////////

	    var thElm;
	    var startOffset;

	    Array.prototype.forEach.call(
	      document.querySelectorAll(".js-table-resize .td-title"),
	      function (th) {

	        var grip = document.createElement('div');
	        grip.innerHTML = "&nbsp;";
	        grip.style.top = 0;
	        grip.style.right = 0;
	        grip.style.bottom = 0;
	        grip.style.width = '5px';
	        grip.style.position = 'absolute';
	        grip.style.cursor = 'col-resize';
	        grip.addEventListener('mousedown', function (e) {
	            thElm = th;
	            startOffset = th.offsetWidth - e.pageX;
	        });

	        th.appendChild(grip);
	      });

	    document.addEventListener('mousemove', function (e) {
	      if (thElm) {
	        thElm.style.width = startOffset + e.pageX + 'px';
	      }
	    });

	    document.addEventListener('mouseup', function () {
	        thElm = undefined;
	    });

});