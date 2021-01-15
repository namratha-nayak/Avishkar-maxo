function submitAnswers(){
	var total = 80;
	var score = 0;
	
	
	var q1 = document.forms["quizForm"]["q1"].value;
	var q2 = document.forms["quizForm"]["q2"].value;
	var q3 = document.forms["quizForm"]["q3"].value;
	var q4 = document.forms["quizForm"]["q4"].value;
	var q5 = document.forms["quizForm"]["q5"].value;
	var q6 = document.forms["quizForm"]["q6"].value;
	var q7 = document.forms["quizForm"]["q7"].value;
	var q8 = document.forms["quizForm"]["q8"].value;
	var q9 = document.forms["quizForm"]["q9"].value;
	var q10 = document.forms["quizForm"]["q10"].value;
	var q11 = document.forms["quizForm"]["q11"].value;
	var q12 = document.forms["quizForm"]["q12"].value;
	var q13 = document.forms["quizForm"]["q13"].value;
	var q14 = document.forms["quizForm"]["q14"].value;
	var q15 = document.forms["quizForm"]["q15"].value;
	var q16 = document.forms["quizForm"]["q16"].value;
	var q17 = document.forms["quizForm"]["q17"].value;
	var q18 = document.forms["quizForm"]["q18"].value;
	var q19 = document.forms["quizForm"]["q19"].value;
	var q20 = document.forms["quizForm"]["q20"].value;
	var q21 = document.forms["quizForm"]["q21"].value;
	var q22 = document.forms["quizForm"]["q22"].value;
	var q23 = document.forms["quizForm"]["q23"].value;
	var q24 = document.forms["quizForm"]["q24"].value;
	var q25 = document.forms["quizForm"]["q25"].value;
	var q26 = document.forms["quizForm"]["q26"].value;
	var q27 = document.forms["quizForm"]["q27"].value;
	var q28 = document.forms["quizForm"]["q28"].value;
	var q29 = document.forms["quizForm"]["q29"].value;
	var q30 = document.forms["quizForm"]["q30"].value;
	var q31 = document.forms["quizForm"]["q31"].value;
	var q32 = document.forms["quizForm"]["q32"].value;
	var q33 = document.forms["quizForm"]["q33"].value;
	var q34 = document.forms["quizForm"]["q34"].value;
	var q35 = document.forms["quizForm"]["q35"].value;
	var q36 = document.forms["quizForm"]["q36"].value;
	var q37 = document.forms["quizForm"]["q37"].value;
	var q38 = document.forms["quizForm"]["q38"].value;
	var q39 = document.forms["quizForm"]["q39"].value;
	var q40 = document.forms["quizForm"]["q40"].value;
	var q41 = document.forms["quizForm"]["q41"].value;
	var q42 = document.forms["quizForm"]["q42"].value;
	var q43 = document.forms["quizForm"]["q43"].value;
	var q44 = document.forms["quizForm"]["q44"].value;
	var q45 = document.forms["quizForm"]["q45"].value;
	var q46 = document.forms["quizForm"]["q46"].value;
	var q47 = document.forms["quizForm"]["q47"].value;
	var q48 = document.forms["quizForm"]["q48"].value;
	var q49 = document.forms["quizForm"]["q49"].value;
	var q50 = document.forms["quizForm"]["q50"].value;
	var q51 = document.forms["quizForm"]["q51"].value;
	var q52 = document.forms["quizForm"]["q52"].value;
	var q53 = document.forms["quizForm"]["q53"].value;
	var q54 = document.forms["quizForm"]["q54"].value;
	var q55 = document.forms["quizForm"]["q55"].value;
	var q56 = document.forms["quizForm"]["q56"].value;
	var q57 = document.forms["quizForm"]["q57"].value;
	var q58 = document.forms["quizForm"]["q58"].value;
	var q59 = document.forms["quizForm"]["q59"].value;
	var q60 = document.forms["quizForm"]["q60"].value;
	var q61 = document.forms["quizForm"]["q61"].value;
	var q62 = document.forms["quizForm"]["q62"].value;
	var q63 = document.forms["quizForm"]["q63"].value;
	var q64 = document.forms["quizForm"]["q64"].value;
	var q65 = document.forms["quizForm"]["q65"].value;
	var q66 = document.forms["quizForm"]["q66"].value;
	var q67 = document.forms["quizForm"]["q67"].value;
	var q68 = document.forms["quizForm"]["q68"].value;
	var q69 = document.forms["quizForm"]["q69"].value;
	var q70 = document.forms["quizForm"]["q70"].value;
	var q71 = document.forms["quizForm"]["q71"].value;
	var q72 = document.forms["quizForm"]["q72"].value;
	var q73 = document.forms["quizForm"]["q73"].value;
	var q74 = document.forms["quizForm"]["q74"].value;
	var q75 = document.forms["quizForm"]["q75"].value;
	var q76 = document.forms["quizForm"]["q76"].value;
	var q77 = document.forms["quizForm"]["q77"].value;
	var q78 = document.forms["quizForm"]["q78"].value;
	var q79 = document.forms["quizForm"]["q79"].value;
	var q80 = document.forms["quizForm"]["q80"].value;
    
		
	for(i = 1; i <= total;i++){
		if(eval('q'+i) == null || eval('q'+i) == ''){
			alert('you missed question '+ i);
		    return false;
		}
	}
	
	
	var answers = ["a","c","a","b","a","d","c","b","a","d","b","c","b","b","c","c","b","d","d","c","a","d","c","b","d","a","c","d","c","d","a","b","d","d","d","b","b","a","d","a","c","b","c","a","c","c","c","d","d","b","a","b","b","a","b","a","b","b","b","d","b","a","c","c","d","b","d","c","a","b","a","d","b","c","b","c","b","a","b","c"];
	
	
	for(i = 1; i <= total;i++){
		if(eval('q'+i) == answers[i - 1]){
			score++;
		}
	}
	
	
	var results = document.getElementById('results');
	results.innerHTML = '<h3>you scored <span>'+score+'</span> out of <span>'+total+'</span></h3>';
	alert('you scored '+score+' out of ' +total);
	
	return false;
}