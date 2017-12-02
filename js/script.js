var questionCount = 10;
var currentIndex = 0;
var questions = [];
var score = 0;

$(function(argument) {
	String.prototype.format = function() {
		var formatted = this;
		for (var i = 0; i < arguments.length; i++) {
			var regexp = new RegExp('\\{'+i+'\\}', 'gi');
			formatted = formatted.replace(regexp, arguments[i]);
		}
		return formatted;
	};

	function hideall() {
		$("#intro").hide();
		$("#quiz").hide();
		$("#result").hide();
	}

	function showWidget(widget) {
		hideall();
		$(widget).fadeIn();
	}


	function shuffle(c) {
		var o = new Array();
		for (var i = 0; i < c.length; i++) {
			var n = c[Math.floor(Math.random()*c.length)];
			if( jQuery.inArray(n, o) > 0 ) --i;
			else o.push(n);
		}
		return o;
	}

	function showQuestion() {
		var question = questions[currentIndex];
		$("#quiz").hide();
		$("#quiz").html("");
		$("#quiz").append("<p class='progress'>Question {0} of {1}</p>".format(currentIndex + 1, questionCount));
		$("#quiz").append("<p class='question'>{0}</p>".format(question.question));
		$.each(question.options, function(index, option) {
			$("#quiz").append("<div class='option'>{0}</div>".format(option));
		});
		$("#quiz").show();
	}

	$("#quiz").on("click", ".option", function() {
		var question = questions[currentIndex];
		if (question.done) return;
		question.done = true;
		
		if (question.answer == $(this).text()) {
			$(this).addClass("correct");
			score += 1;
		} else {
			$(this).addClass("incorrect");
			$.each($(".option"), function(index, option) {
				if (question.answer == $(this).text()) {
					$(this).addClass("correct");
				} 
			});
		}
		$("#quiz").append("<div id='next' class='btn'>Continue</div>");
	});

	$("#quiz").on("click", "#next", function() {
		currentIndex += 1;
		if (currentIndex < questionCount) {
			showQuestion();
		} else {
			$("#score").text("You scored {0}% by correctly answering {1} of total {2} questions"
				.format(score * 100.0 / questionCount, score, questionCount)
				);
			showWidget("#result");
		}
	});

	$("#reset").on("click", function(){
		currentIndex = 0;
		questions = [];
		score = 0;
		$("#start").click();
	});

	// Show intro
	showWidget('#intro');

	$("#start").on("click", function() {
		$.getJSON("data/data.json", function(data) {
			data = shuffle(data);
			$.each(data, function(index, question) {
				questions.push(question);
			});
			questions = questions.splice(0, questionCount);
			showQuestion();
			showWidget('#quiz');
		});
		
	});

	
});