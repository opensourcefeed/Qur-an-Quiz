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
		$("#topics-section").hide();
	}

	function showWidget(widget) {
		hideall();
		$(widget).fadeIn();
	}


	/**
	 * Randomize array element order in-place.
	 * Using Durstenfeld shuffle algorithm.
	 */
	 function shuffle(array) {
	 	for (var i = array.length - 1; i > 0; i--) {
	 		var j = Math.floor(Math.random() * (i + 1));
	 		var temp = array[i];
	 		array[i] = array[j];
	 		array[j] = temp;
	 	}
	 	return array;
	 }


	function showQuestion() {
		var question = questions[currentIndex];
		$("#quiz").hide();
		$("#quiz").html("");
		$("#quiz").append("<p class='progress'>Question {0} of {1}</p>".format(currentIndex + 1, questionCount));
		$("#quiz").append("<p class='question'>{0}</p>".format(question.question));
		$.each(shuffle(question.options), function(index, option) {
			$("#quiz").append("<div class='option'>{0}</div>".format(option));
		});
		$("#quiz").show();
	}

	$("#topics-section").on("click", ".topic", function() {
		var id = $(this).data("id");
		$.getJSON("data/"+id+".json", function(data) {
			data = shuffle(data.questions);
			$.each(data, function(index, question) {
				questions.push(question);
			});
			questions = questions.splice(0, questionCount);
			showQuestion();
			showWidget('#quiz');
		});
		
	});

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
		$("#choose-topic").click();
	});

	// Show intro
	showWidget('#intro');

	$("#choose-topic").on("click", function() {
		$.getJSON("data/topics.json", function(data) {
			var topics = "";
			$.each (data, function(index, topic) {
				topics += "<div class='btn topic' data-id='{1}'>{0}</div>".format(topic.title, topic.id);
			});
			$("#topic-list").html(topics);

			showWidget('#topics-section');
		}, function(e) {
			console.log(e);
		});
		
	});



	
});